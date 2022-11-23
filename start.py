from crypt import methods
from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index",methods=["POST","GET"])
def index():
    lista=[]
    item = {
    "title": "Unical",
    "description": "descrizione dell'università",
    "fun":1,
    "security":1,
    "overall":2,
   "cost":4
    }


    item2 = {
    "title": "Unimi",
    "description": "descrizione dell'università",
    "fun":1,
    "security":1,
    "overall":2,
    "cost":4
    }
    
    lista.append(item)
    lista.append(item2)
    lista.append(item)
    lista.append(item2)
    lista.append(item2)
    lista.append(item)
    lista.append(item2)   
    lista.append(item2)
    lista.append(item)
    lista.append(item2)
    return render_template("index.html",items=lista)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
