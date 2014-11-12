from flask import Flask, request, redirect, render_template
import datetime
import md5
import json
import urllib2
app=Flask(__name__)
#marvel requirements
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
    crowded_list=[]
    final_dict=[]
    final_dict2=[]
    url=geturl()
    request=urllib2.urlopen(url)
    result=request.read()
    d=json.loads(result)
	#
    extra_data=d['data']
    data=extra_data['results']
    for key in data:
        crowded_list.append(key)
    x=0
    for value_dict in crowded_list:
        for value in value_dict:
            if value=='title': #or value=='prices':
                final_dict.append(value_dict[value])
                x=x+1
    for value_dict in crowded_list:
        for value in value_dict:
            if value=='prices': #or value=='prices':
                final_dict2.append(value_dict[value])
                x=x+1
	m = zip(final_dict,final_dict2)
	k= dict(m)
    return k

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
