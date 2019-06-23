# The Daily Writer

**LINK to the active application:** https://blog-project-flask-mongo.herokuapp.com/

The Daily Writer is my third milestone project as part of my Full Stack Web Development course at Code Institute.

The project is a blog / news site where anyone can post an article.

The site has been built using HTML, CSS, Bootstrap 4 and a free Bootstrap theme from startbootstrap.com, called 'Clean Blog.'

Flask has been used for the back-end technology, and Flask's use of Jinja templating was implemented in the HTML to save the need to write additional code and to copy-paste the base / index of the blog.

Due to the fact that Flask is a Python micro web framework, Python programming logic has been implemented.

The contents of the blog (the articles) are saved on a datastore. For this project MongoDB is used to collect new data in the form of new documents.

## Features

* Any visitor can see the entire content.
* Any visitor can submit an article, no registration required.
    * Upon submitting an article, the user (visitor) must mandatorily submit a title, category, image, content (actual article), and submit their name (or the name of the author, if they have copied someone else's content) in the 'Author' section.
* As mentioned above, the user must choose a category when submitting new content. Each category represents a separate collection in the MongoDB datastore for this project.

## Design 

The website uses a Bootstrap theme - downloaded from startbootstrap.com, called 'Clean Blog.' This project has a mobile-first design, hence why both a Bootstrap theme, as well as additional Bootstrap 4 were used for the creating of the front-end.

The design is not in it's original form - some things have been changed. Additional fonts have been added from Google Fonts.

Menu items have been renamed to fit the purpose of this project.

## UX

The implementation of a blogging bootstrap theme was inspired by the saying "Don't recreate the wheel", also considering the fact that this is a back-end and data-centric focused project.

Regardless, the site has intuitive features.

The latest article for each category (five categories in total) is displayed on the Home Page.

When the user goes to the 'POST' page, they are taken to a submission form. There they have to:

**1. Give the article a title:**
![article_title](https://i.ibb.co/kQD764N/article-title.jpg "Article title")

**2. Select a category:**
![select_category](https://i.ibb.co/D4fzdsw/select-category.jpg "Select category")

**3. Provide an image URL:**
![image_link](https://i.ibb.co/9bT21XV/image-link.jpg "User image url")

**4. Write the article:**
![article_content](https://i.ibb.co/vhtzvNW/article-content.jpg "Article content")

**5. Submit author's name:**
![author_name](https://i.ibb.co/1L04TGD/author.jpg "Author")

**6. Click submit button:**  
![submit_button](https://i.ibb.co/2M8FyzF/submit.jpg "Submit")  

After submitting the article, the user gets redirected to the home page, where he will see his article posted as the latest content in his section (whichever section they chose).

## Database Schema

The uploaded contents (articles) are stored in a datastore - in MongoDB, divided into 5 collections:

**1. general_news**
**2. health**
**3. sports**
**4. technology**
**5. travel**

These collections have been wired in the application's back-end:

```
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
		
		return redirect('/')
	else:
		return render_template('post.html')
```

## Languages / Frameworks

* HTML, CSS, SCSS
* Flask 1.0.3
* Python 3.6.7
* Bootstrap 4.3.1 / 'Clean Blog' theme via startbootstrap.com
* Google Fonts (Exo 2, Open Sans Condensed, Fjalla One)

## Deployment

The source code for this project is deloyed on GitHub.com; The working app is deployed on Heroku.

## Testing

All of the site's features have been tested manually, due to the simplicity of the Flask framework.

The users may upload an article to each one of the categories (collections).

## Contributions

**ATTENTION!**
As mentioned above, this project was built using a Boostrap theme. This means that there are default files and folders NOT created by me and NOT written by me.
Those 'default' files include:
* Vendor folder, including the folders inside of it and their contents:
    * bootstrap
    * fontawesome-free
    * jquery
* SCSS folder and ALL of its contents
* JS folder
* CSS folder and two of its contents:
    * clean-blog.css
    * clean-blog-min.css
    * (this does NOT include the style.css file - this is a custom file, with custome styles, created by me)
* mail folder

*The menu items - each one a separate html file - have been edited, and some of them renamed, to suit the nature of the project. Additional pages have been added - the ones that represent the different categories (with underscores in their names).*

*The templates folder is a custom creation, required by Flask and its Jinja templating feature.*





