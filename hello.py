from flask import Flask, render_template

'''
safe
capitalize
lower
upper
title
trim
striptags
'''

#create a Flask Instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#    return "<h1>Hello World!</h1>"


def index():
    first_name = 'Mohamed'
    stuff = 'This is <strong>Bold</strong> text'

    favorite_pizza=['Pepperoni', 'Cheeze', '41']
    return render_template("index.html", name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)




@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)


# invalid url
@app.errorhandler(404)
def page_not_found(e):
    render_template("404.html"), 404

# server error
@app.errorhandler(500)
def page_not_found(e):
    render_template("500.html"), 500


