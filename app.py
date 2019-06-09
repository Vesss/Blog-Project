import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "blog_project"
app.config["MONGO_URI"] = "mongodb+srv://root:maniac93@myfirstcluster-ilypv.mongodb.net/blog_project?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html", about=mongo.db.about_information.find())
    
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/post")
def post():
    return render_template("post.html")
    
@app.route("/articles")
def articles():
    return render_template("articles.html")
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

