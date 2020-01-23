from app import app


@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    content = """<!DOCTYPE html>
    <html>
      <head>
        <title>Nuffle Nuffle</title>
        <link rel="stylesheet" href="/static/styles.css">
        <link href="https://fonts.googleapis.com/css?family=Cute+Font&display=swap" rel="stylesheet">
        <style>
          .img-container { text-align: center; display: block; } </style>
        </head>
      <body style="background-color:#66b3ff; foreground-color:#ffffff">
        <span class="img-container" style="font-family: 'Cute Font';font-weight:bold;color:#ffffff"><br/><br/>
           <img src="static/bunny.png" width=300 alt=""><br/>
           <form action="" method="post" novalidate>
             <input id="csrf_token" name="csrf_token" type="hidden" value="ImRjNTMzOTIxMWQxODRmNWNjODk4ODM5OTM1MWRkYzViZmNlOTJmNmIi.XikHXw.uxhoesBGUlE7H8TKFL7S5OY0bH8">
             <div class="container">
               <br><br>
               <div class="row"><div class="col-25">
                 <label for="name">Username</label></div><div class="col-75">  <input id="name" name="username" required type="text" value="">
               </div>
             </div>
             <div class="row"><div class="col-25"> <label for="password">Password</label> </div>
             <div class="col-75"> <input id="password" name="password" required size="50" type="password" value=""></div></div>
             <br/>
             <div class="row"><div class="col-75"></div><input id="submit" name="submit" type="submit" value="Login" size="32"></div>
           </form>
        </span>
      </body>
    </html>"""
    return content


