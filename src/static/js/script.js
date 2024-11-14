function postToURL(url, values)
{
    values = values || {};
    
    $.post(url, values, function(e){
      $('ul').find('#article_'+e).remove();
			if( $('div.flash').length == 0 ) {
				$( 'div.notice' ).append( '<div class="flash"></div>' );
			}
			$( 'div.flash' ).text( 'Article with ID:' + e + ' was deleted succesfully!' );
			if( $( 'ul' ).children().length == 0 ) {
				$( 'ul' ).append( '<li><em>Unbelievable. No entries here so far!</em></li>' );
			}
    })
}

function confirmation(question, location, post, values)
{
	var answer = confirm(question);
	if (answer)
	{
		if (post)
		{
			postToURL(location, values);
		}
		else
		{
			window.location = location;
		}
	}
}
