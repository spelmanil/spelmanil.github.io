# spelmanil.github.io
Spelman Innovation Lab

Use the python script frame_gdoc_html.py one time to create the index.html file.

index.html by default references the 4 images in the img directory.  These are the images for the 'back' button, the logo in the header and the two images in the footer.  The filenames indicate which image is which.

Pass a Google Doc weblink to the index.hmtl file via a URL search query to display the doc in the customized index.html webpage.

For example, if this webpage is index.html, and you wish to view a Google doc at `https://docs.google.com/abcxyz123`, then construct the following URL:
            `http://index.html?https://docs.google.com/abcxyz123`
            
Because `index.html` is the default html page, it can be omitted.  The following will also work: `spelmanil.github.io?https://docs.google.com/abcxyz123`.  This is the preferred method.


You can customize the output frame through a number of URL parameters besides 'src'.  Here is the complete list:



`backgroundColor` sets the background color of the display.  Use either standard web color names or a hexidecimal value in the form #rrggbb.  Note that you must escape the '#' in the URI.  So, to set the background color to a hex value of 0xaabbcc, for example, the correctly formatted parameter would be
`backgroundColor=%23aabbcc`
because the '#' has character code %23.

`themeColor}` sets the color of the display theme.  See the description of `backgroundColor` for details on how to set this value.

`backURL` is the URL we will navigate to when the user clicks the 'back' arrow.  By default, this value is set to `javascript:history.back()`, but you can override that value and set it to any URL.  Set `backURL` to an empty string to prevent the button from being drawn 
(`backURL=` on the URL argument list).

`forwardURL` is similar to `backURL` except this is a reference to the URL we will travel to when the user clicks the 'forward' button.  The default value is an empty string, which causes the button to not be rendered.   `javascript:history.forward()` is possibly a good choice for this parameter.

`bodyWidth` the width of the main display.  This can be a fraction of the screen or an absolute pixel value.  Note that you will have to escape the '%' character with its ASCII representation (%25) to set the value as a percentage.  To set the width to 80%, use the parameter `bodyWidth=80%25`.  To set the width to 400 pixels, use the parameter `bodyWidth=400px`.