# The Daily Writer

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

![general_news](https://i.ibb.co/M6wWPG0/general-news.jpg)

## Languages / Frameworks

* HTML, CSS, SCSS
* Flask 1.0.3
* Python 3.6.7
* Bootstrap 4.3.1 / 'Clean Blog' theme via startbootstrap.com
* Google Fonts (Exo 2, Open Sans Condensed, Fjalla One)

## Deployment & Contributions

The source code for this project is deloyed on GitHub.com; The working app is deployed on Heroku.


