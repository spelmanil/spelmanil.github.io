#---------- define the html_template ----------
html_template = '''
<html>
    <head>
        <title>Innovation Lab Docs</title>
    </head>
    <style>

    body {
        background-color: {backgroundColor};
        width:{bodyWidth};
        min-width: 400px;
        margin-left: auto;
        margin-right:auto;
        overflow: hidden;
        margin-top: 1%;
        margin-bottom: 1%;
    }

    #container {
        background-color: {themeColor};
        width:100%;
        min-width:100%;
        height:100%;
        min-height:100%;
        margin-left:auto;
        margin-right:auto;
        padding:0px;
    }

    #header {
        height:10%;
        min-height:10%;
        padding:0px 30px 0px 30px;
        margin-top:auto;
        margin-bottom:auto;
    }

    #content {
      width:100%;
      min-width:100%;
      /* 78% = 80% - top_margin - bottom_margin */
      height:78%;
      min-height:78%;
      padding:0px;
    }

    #footer {
        height:10%;
        min-height:10%;
        text-align: left;
        margin-top:auto;
        margin-bottom:auto;
        padding:0px 30px 0px 30px;
    }
    
    #footer img {
      margin-top:2%; /* ~ of 2.5% */
    }

    </style>
    <body>
        <div id="container">
            <div  id="header">
                <a href="{backURL}"><img style="height:100%;" src="img/back.png" /></a><img style="height:100%;" src="img/logo.png"></img>
            </div>

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

                }

                var GDocWebLink = '<embed id="content" src="' + src + '?embedded=true"></embed>';
                window.document.write(GDocWebLink);
            </script>
            
            <div id="footer">
              <img style="float:left;height:90%;" src="img/lower_left_image.png"></img>
              <img style="float:right;height:90%;" src="img/lower_right_image.png"></img>

            </div>

        </div>

    </body>

</html>

'''

INPUT_REQUIRED = 'INPUT REQUIRED'

#---------- define the placeholders & defaults ----------
placeholders = dict();

placeholders['{backgroundColor}'] = '#eeeeee'
placeholders['{themeColor}'] = '#2d76d8'
placeholders['{backURL}'] = 'javascript:history.back()'
#placeholders['{GDocWebLink}'] = INPUT_REQUIRED
#placeholders['{GDocWebLink}'] = 'https://docs.google.com/document/d/e/2PACX-1vTwkcjKQmjb7W0U2Yq0zZVR9VRzVbM_kOgYdLyMnQFthEKDO-jiYaCF-ucA83yhfVE24oVaEnQhPnhR/pub'
placeholders['{bodyWidth}'] = '80%'


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
    
    #upate the html template string
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