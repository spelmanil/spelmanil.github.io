# spelmanil.github.io
Spelman Innovation Lab

Use the python script frame_gdoc_html.py one time to create the index.html file.

index.html by default references the 4 images in the img directory.  These are the images for the 'back' button, the logo in the header and the two images in the footer.  The filenames indicate which image is which.

Pass a Google Doc weblink to the index.hmtl file via a URL search query to display the doc in the customized index.html webpage.

For example, if this webpage is index.html, and you wish to view a Google doc at `https://docs.google.com/abcxyz123`, then construct the following URL:
            `http://index.html?https://docs.google.com/abcxyz123`
            
Because `index.html` is the default html page, it can be omitted.  The following will also work: `spelmanil.github.io?https://docs.google.com/abcxyz123`.  This is the preferred method.