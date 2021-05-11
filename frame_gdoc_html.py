#---------- define the html_template ----------
html_template = '''
<html>
    <head>
        <title>Spelman Innovation Lab</title>
        <link rel="icon" href="img/il.ico">
    </head>
    <style>

    body {
        background-color: {backgroundColor};
        width:{bodyWidth};
        min-width: 300px;
        margin-left: auto;
        margin-right:auto;
        overflow: hidden;
        margin-top: 0%;
        margin-bottom: 0%;
    }

    #container {
        background-color: {themeColor};
        width:100%;
        max-width:{maxWidth};
        height:100%;
        min-height:100%;
        margin-left:auto;
        margin-right:auto;
        padding:0px;
    }

    #header {
        height:10%;
        min-height:10%;
        padding:0px 1% 0px 1%;
        margin-top:auto;
        margin-bottom:auto;
    }

    #content {
      width:100%;
      min-width:100%;
      height:80%;
      min-height:80%;
      padding:0px;
    }

    #footer {
        height:10%;
        min-height:10%;
        text-align: left;
        margin-top:auto;
        margin-bottom:auto;
        padding:0px;
    }

    #header img {
      margin: 0.5% 0% 0% 0%;
      height: 90%;
    }

    #footer img {
      margin: 0.5% 2% 0% 2%;
      height: 90%;
    }

    </style>
    <body>
        <div id="container">

            <!-- publish your Google doc to the web.  Then, pass the
            weblink as a 'src' query parameter by appending it to the URL
            for this html page.  For example, if
            this webpage is index.html, and you wish to view a Google
            doc at https://docs.google.com/abcxyz123, then construct
            the following URL:
            http://index.html?src=https://docs.google.com/abcxyz123 -->

            <script>
                /* set default values here */
                var src = "default.html";

                var urlParams = new URLSearchParams(window.location.search);
                var keys = urlParams.keys();
                for(key of keys) {
                  val = urlParams.get(key);
                  //console.log(">>"+key+"="+val+"<<");

                  if (key == "src") {
                    src = val;
                  }

                  if (key == "themeColor"){
                    //raw hex values used for colors are formatted ad #rrggbb.  In the URL parameter, encode this as %23rrggbb as use of the '#' character is reserved.
                    document.getElementsByTagName('style')[0].innerHTML += "#container {background-color: " + val + ";}";
                  }

                  if (key == "backgroundColor"){
                    document.getElementsByTagName('style')[0].innerHTML += "body {background-color: " + val + ";}";
                  }

                  if (key == "bodyWidth"){
                    //bodyWidth can be in % or in px.  For URL parameters, encode the '%' symbol as %25.  So 80% body width should be encoded as 'bodyWidth=80%25' in the URL parameters list.
                    document.getElementsByTagName('style')[0].innerHTML += "body {width: " + val + ";}";
                  }

                  if (key == "maxWidth"){
                    document.getElementsByTagName('style')[0].innerHTML += "#container {max-width: " + val + ";}";
                  }

                }

                window.document.write('<div  id="header">');

                if (urlParams.has("backURL")) //a URL parameter was provided, override the default
                {
                  if (urlParams.get("backURL") == ''){
                    backURL = '';
                  }
                  else {
                    backURL = '<a href="' + urlParams.get("backURL") + '"><img src="img/back.png" /></a>';
                  }
                }
                else //no URL parameter was provided, use the default set with the python script
                {
                  if ('{backURL}' == '') {
                    backURL = '';
                  }
                  else {
                    backURL = '<a href="{backURL}"><img src="img/back.png" /></a>';
                  }
                }
                window.document.write(backURL);

                //draw the logo
                window.document.write('<img src="img/logo.png"></img>');

                if (urlParams.has("forwardURL")) //a URL parameter was provided, override the default
                {
                  if (urlParams.get("forwardURL") == ''){
                    forwardURL = '';
                  }
                    else {
                      forwardURL = '<a href="' + urlParams.get("forwardURL") + '"><img style="float:right" src="img/forward.png" /></a>';
                    }
                }
                else //no URL parameter was provided, use the default set with the python script
                {
                  if ('{forwardURL}' == '') {
                    forwardURL = '';
                  }
                  else {
                   forwardURL = '<a href="{forwardURL}"><img style="float:right" src="img/forward.png" /></a>';
                   }
                }
                window.document.write(forwardURL);
                window.document.write('</div>');

                var GDocWebLink = '<embed id="content" src="' + src + '?embedded=true"></embed>';
                window.document.write(GDocWebLink);
            </script>

            <div id="footer">
              <img style="float:left" src="img/lower_left_image.png"></img>
              <img style="float:right" src="img/lower_right_image.png"></img>

            </div>

        </div>

    </body>

</html>

'''

INPUT_REQUIRED = 'INPUT REQUIRED'

#---------- define the placeholders & defaults ----------
placeholders = dict();

placeholders['{backgroundColor}'] = 'black'
placeholders['{themeColor}'] = '#2d76d8'
placeholders['{backURL}'] = 'javascript:history.back()'
placeholders['{forwardURL}'] = ''   #'javascript:history.forward()'
#placeholders['{GDocWebLink}'] = INPUT_REQUIRED
#placeholders['{GDocWebLink}'] = 'https://docs.google.com/document/d/e/2PACX-1vTwkcjKQmjb7W0U2Yq0zZVR9VRzVbM_kOgYdLyMnQFthEKDO-jiYaCF-ucA83yhfVE24oVaEnQhPnhR/pub'
placeholders['{bodyWidth}'] = '100%'
placeholders['{maxWidth}'] = '1100px';

def updateHtmlParameter(placeholder):
    prompt = 'Enter value for '+placeholder+' ['+placeholders[placeholder]+']: '
    x = input(prompt)
    if x!='':
        #if the user entered a value, update the dictionary.  Otherwise, do nothing
        placeholders[placeholder] = x.strip()

#---------- get placeholder parameters from user ----------
for placeholder in placeholders:
    if placeholders[placeholder] == INPUT_REQUIRED:
        #loop until the user enters a value
        while placeholders[placeholder] == INPUT_REQUIRED:
            updateHtmlParameter(placeholder)
    else:
        updateHtmlParameter(placeholder)

    #update the html template string
    html_template = html_template.replace(placeholder, placeholders[placeholder])


#Get the name of the output ifle
outFile = 'index.html'
prompt = 'Enter output file name ['+outFile+']: '

x = input(prompt)
if x!='':
    outFile = x.strip()

outFile = open(outFile, 'wt')
outFile.write(html_template)
outFile.close()


#----------  ----------
#----------  ----------
