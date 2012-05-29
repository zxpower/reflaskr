###################################################################
# reflaskr
# --------
# Minimal blog engine based on Python's Flask Tutorial
# http://flask.pocoo.org/docs/tutorial/
# 
# Created by: digiBlink - http://digibling.eu/
################################################################### 

# all the imports
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
	
# create our little application :)
app = Flask(__name__)
app.config.from_pyfile('app.cfg')

# let's connect to DB
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# let's initialize it if it's not already done
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

@app.route('/')
def show_entries():
	cur = g.db.execute('select id, title, text from entries order by id desc')
	entries = [dict(id=row[0], title=row[1], text=row[2]) for row in cur.fetchall()]
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	g.db.execute('insert into entries (title, text) values (?, ?)',
					[request.form['title'], request.form['text']])
	g.db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/edit/<int:articleid>', methods=['GET', 'POST'])
def edit_entry(articleid):
	return redirect(url_for('show_entries'))

@app.route('/delete/<int:articleid>', methods=['GET', 'POST'])
def delete_entry(articleid):
	if not session.get('logged_in'):
		abort(401)
	return "Article ID:" + str(articleid)
#	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
	app.run()