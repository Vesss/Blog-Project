import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "blog_project"
app.config["MONGO_URI"] = "mongodb+srv://root:maniac93@myfirstcluster-ilypv.mongodb.net/blog_project?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
@app.route("/publish_article")
def publish_article():
    return render_template("articles.html", articles=mongo.db.articles.find())
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

