function postToURL(url, values)
{
    values = values || {};
    
    $.post(url, values, function(e){
    
    	console.log(e);
    
    })
    
    /*

    var form = document.createElement("form", {action: url,
                                      method: "POST",
                                      style: "display: none"});
    for (var property in values)
    {
        if (values.hasOwnProperty(property))
        {
            var value = values[property];
            if (value instanceof Array)
            {
                for (var i = 0, l = value.length; i < l; i++)
                {
                    form.appendChild(document.createElement("input", {type: "hidden",
                                                             name: property,
                                                             value: value[i]}));
                }
            }
            else
            {
                form.appendChild(document.createElement("input", {type: "hidden",
                                                         name: property,
                                                         value: value}));
            }
        }
        
    }
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
    
    */
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