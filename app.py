from flask import Flask, request, redirect, render_template
import datetime
import md5
import json
import urllib2
app=Flask(__name__)
#retarded marvel requirements
def geturl():
    publickey= "2c49b90d137cb226046b577231833d6c"
    privatekey="578b4b42482e490057616a9e4ca204033d1206eb"
    i=datetime.datetime.now()
    timestamp=str(i.second)
    hash2=md5.new(timestamp+privatekey+publickey).hexdigest()
    basepoint="http://gateway.marvel.com/v1/public/comics?"
    url=basepoint+"apikey="+publickey+"&ts="+timestamp+"&hash="+hash2
    #print(url)
    return url
def getdict():
    url=geturl()
    request=urllib2.urlopen(url)
    result=request.read()
    d=json.loads(result)
    return d

#api dictionary
apid=getdict()
#api dictionary



@app.route("/",methods = ["GET","POST"])
def index():
    return render_template("home.html")
@app.route("/coolstuff",methods = ["GET","POST"])
def coolstuff():
    return render_template("coolstuff.html",dict=apid)

if __name__=="__main__":
    app.debug=True
    app.run()
