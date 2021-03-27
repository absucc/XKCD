# Settings
utterances_repo = "absucc/c-xkcd"
host = "0.0.0.0"
port = "8080"


__version__ = "2.1.1"
from flask import Flask, render_template, request
import urllib3
import json
import os
import random
app = Flask("XKmodern")
http = urllib3.PoolManager()

def clean():
  os.system("cls" if os.name=="nt" else "clear")
clean()

@app.route("/", methods=["GET"])
def xkcdreader():
  clean()
  if request.method == "GET":
    lastcomic = http.request('GET', 'https://xkcd.com/info.0.json')
    lccode = json.loads(lastcomic.data.decode('utf-8'))
    numberz = request.args.get("num")
    if numberz is not None:
      clean()
      return "<meta http-equiv=\"refresh\" content=\"0;url=/" + numberz + "\">"
    else:
      clean()
      #return render_template("reader.html", **locals(), numcomic=str(lccode["num"]), title=lccode["title"], comic=lccode["img"], booktitle="", not_the_last=lccode["num"] - 1, its_the_last="#", alt=lccode["alt"], thiscomic=str(lccode["num"]), thedate=lccode["month"]+"/"+lccode["day"]+"/"+lccode["year"], urlbase=request.base_url, ogurl=request.base_url)
      return "<meta http-equiv=\"refresh\" content=\"0;url=/" + str(lccode["num"]) + "\">"

@app.route("/<path:num>")
def numreal(num):
    clean()
    lastcomic = http.request('GET', 'https://xkcd.com/info.0.json')
    lccode = json.loads(lastcomic.data.decode('utf-8'))
    numberz = num
    @app.errorhandler(500)
    def err5002(error):
      clean()
      return render_template("error.html", **locals(), numcomic=str(lccode["num"]), random_num=str(random.randint(1, lccode["num"])), booktitle="This comic wasn't found"),500
    clean()
    jdat = http.request("GET", "https://xkcd.com/" + numberz + "/info.0.json")
    jsdata = json.loads(jdat.data.decode("utf-8"))
    if jsdata["num"] == lccode["num"]: last = "/" + str(lccode["num"]) + "#"
    else: last = "/" + str(jsdata["num"] + 1)
    if jsdata["num"] == 1: back="1#"
    else: back=jsdata["num"] - 1
    if jsdata["num"] == 1608: fimage = "No image"
    else: fimage = jsdata["img"]
    return render_template("reader.html", **locals(), numcomic=str(lccode["num"]), comic=fimage, title=jsdata["title"], booktitle=jsdata["title"] + " | ", not_the_last=back, the_last=last, alt=jsdata["alt"], thiscomic=str(jsdata["num"]), thedate=jsdata["month"]+"/"+jsdata["day"]+"/"+jsdata["year"], urlbase=request.base_url, random_num=str(random.randint(1, lccode["num"])), utes_repo=utterances_repo, search_action="/")

#@app.route("/num/<numberz>")
#def numreader():
  #clean()
  #lastcomic = (http.request('GET', 'https://xkcd.com/info.0.json'))
  #lccode = (json.loads(lastcomic.data.decode('utf-8')))
  #if numberz is not None:
    #@app.errorhandler(500)
    #def err5002(error):
      #clean()
      #return render_template("error.html", **locals(), numcomic=str(lccode["num"]),  booktitle="This comic wasn't found"),500
    #clean()
    #jdat = (http.request("GET", "https://xkcd.com/" + numberz + "/info.0.json"))
    #jsdata = (json.loads(jdat.data.decode("utf-8")))
    #if jsdata["num"] == lccode["num"]:
      #last="?num="+str(lccode["num"])+"#"
    #else:
      #last_plus=jsdata["num"] + 1
      #last="?num=" + str(last_plus)
    #if jsdata["num"] == 1: back="1#"
    #else: back=jsdata["num"] - 1
    #return render_template("reader.html", **locals(), numcomic=str(lccode["num"]), comic=jsdata["img"], title=jsdata["title"], booktitle=jsdata["title"] + " | ", not_the_last=back, its_the_last=last, alt=jsdata["alt"], thiscomic=str(jsdata["num"]), thedate=jsdata["month"]+"/"+jsdata["day"]+"/"+jsdata["year"], urlbase=request.base_url)

@app.route("/script", methods=["GET"])
def scriptreader():
  clean()
  if request.method == "GET":
    lastcomic = (http.request('GET', 'https://xkcd.com/info.0.json'))
    lccode = (json.loads(lastcomic.data.decode('utf-8')))
    numberz = request.args.get("num")
    if numberz is not None:
      @app.errorhandler(500)
      def err5002(error):
        clean()
        return render_template("error.html", **locals(), numcomic=str(lccode["num"]),  booktitle="This comic wasn't found"),500
      clean()
      jdat = (http.request("GET", "https://xkcd.com/" + numberz + "/info.0.json"))
      jsdata = (json.loads(jdat.data.decode("utf-8")))
      if jsdata["num"] == lccode["num"]:
        last="?num="+str(lccode["num"])+"#"
      else:
        last_plus=jsdata["num"] + 1
        last="?num=" + str(last_plus)
      if jsdata["num"] == 1: back="1#"
      else: back=jsdata["num"] - 1
      return render_template("scriptreader.html", **locals(), numcomic=str(lccode["num"]), comic=jsdata["img"], title=jsdata["title"], booktitle=jsdata["title"] + " | ", not_the_last=back, its_the_last=last, alt=jsdata["alt"], thiscomic=str(jsdata["num"]), thedate=jsdata["month"]+"/"+jsdata["day"]+"/"+jsdata["year"], search_action="/script")
    else:
      clean()
      return render_template("scriptreader.html", **locals(), numcomic=str(lccode["num"]), title=lccode["title"], comic=lccode["img"], booktitle="", not_the_last=lccode["num"] - 1, its_the_last="#", alt=lccode["alt"], thiscomic=str(lccode["num"]), thedate=lccode["month"]+"/"+lccode["day"]+"/"+lccode["year"], search_action="/script")

@app.route("/random")
def randomcomic():
  clean()
  lastcomic = (http.request('GET', 'https://xkcd.com/info.0.json'))
  lccode = (json.loads(lastcomic.data.decode('utf-8')))
  return """<meta http-equiv="refresh" content="0;url=/?num=""" + str(random.randint(1, lccode["num"])) + """\">"""

@app.route("/script/random")
def randomscript():
  clean()
  lastcomic = (http.request('GET', 'https://xkcd.com/info.0.json'))
  lccode = (json.loads(lastcomic.data.decode('utf-8')))
  return """<meta http-equiv="refresh" content="0;url=/script?num=""" + str(random.randint(1, lccode["num"])) + """\">"""

if __name__ == "__main__":
  clean()
  app.run(debug=False, host=host, port=port)
  clean()
