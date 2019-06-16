import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_mail import Mail
from flask_mail import Message


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "blog_project"
app.config["MONGO_URI"] = "mongodb+srv://root:maniac93@myfirstcluster-ilypv.mongodb.net/blog_project?retryWrites=true&w=majority"
app.config["DEBUG"] = True
app.config["TESTING"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
# app.config["MAIL_DEBUG"] = True
app.config["MAIL_USERNAME"] = None
app.config["MAIL_PASSWORD"] = None
app.config["MAIL_DEFAULT_SENDER"] = "blitzermann4@gmail.com"
app.config["MAIL_MAX_EMAILS"] = 5
app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_ASCII_ATTACHMENTS"] = False

mail = Mail(app)

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
    
@app.route("/post", methods=["GET", "POST"])
def post():
	if request.method == 'POST':
		#get all the data sent up
		data = request.form.to_dict()
		#print it out to see it got sent properly
		print(data)
		# will look at adding to database next if data is sent up ok
		
		# dict to store new entry to database  
		# will need to use keys you have in collection .. i named them title category etc
		new_item = {
			'title': request.form.get('title'),
			'author': request.form.get('author'),
			'url': request.form.get('url'),
			'content': request.form.get('content')
		}
		print(new_item)
		# need to get the category so can create the database string below
		category=request.form.get('category')
		print("category", category)
		# this should insert into the right collection eg sport health
		# if not will have to use if statements or switch
		mongo.db[category].insert_one(new_item)
		
		return redirect('articles')
	else:
		return render_template('post.html')
    
# @app.route("/add_article")
# def add_article():
    
@app.route("/articles")
def articles():
    return render_template("articles.html")
    
@app.route("/sports")
def sports():
	return render_template("sports.html")
	
@app.route("/general_news")
def general_news():
	return render_template("general_news.html")

@app.route("/technology")
def technology():
	return render_template("technology.html")
	
@app.route("/fashion")
def fashion():
	return render_template("fashion.html")

@app.route("/health")
def health():
	return render_template("health.html")
    
@app.route("/send", methods=["GET", "POST"])
def send():
    msg = Message("Hi there", recipients=["ves.dimitrov121@gmail.com"])
    mail.send(msg)
    if request.method == "POST":
        return 'Form posted.'
    elif request.method == "GET":
        return render_template('contact.html')
        
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

