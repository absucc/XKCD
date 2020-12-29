__version__ = "1.0.2"
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
      return render_template("reader.html", **locals(), numcomic=str(lccode["num"]), comic=jsdata["img"], title=jsdata["title"], booktitle=jsdata["title"] + " | ", not_the_last=back, its_the_last=last, alt=jsdata["alt"], thiscomic=str(jsdata["num"]), thedate=jsdata["month"]+"/"+jsdata["day"]+"/"+jsdata["year"])
    else:
      clean()
      return render_template("reader.html", **locals(), numcomic=str(lccode["num"]), title=lccode["title"], comic=lccode["img"], booktitle="", not_the_last=lccode["num"] - 1, its_the_last="#", alt=lccode["alt"], thiscomic=str(lccode["num"]), thedate=lccode["month"]+"/"+lccode["day"]+"/"+lccode["year"])

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
      return render_template("scriptreader.html", **locals(), numcomic=str(lccode["num"]), comic=jsdata["img"], title=jsdata["title"], booktitle=jsdata["title"] + " | ", not_the_last=back, its_the_last=last, alt=jsdata["alt"], thiscomic=str(jsdata["num"]), thedate=jsdata["month"]+"/"+jsdata["day"]+"/"+jsdata["year"])
    else:
      clean()
      return render_template("scriptreader.html", **locals(), numcomic=str(lccode["num"]), title=lccode["title"], comic=lccode["img"], booktitle="", not_the_last=lccode["num"] - 1, its_the_last="#", alt=lccode["alt"], thiscomic=str(lccode["num"]), thedate=lccode["month"]+"/"+lccode["day"]+"/"+lccode["year"])

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
  app.run(debug=False, host="0.0.0.0", port="8080")
  clean()
