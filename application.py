import json, requests
from flask import Flask, request, render_template
from pymongo import MongoClient
from bson import json_util
# from flask.ext.pymongo import PyMongo

client = MongoClient()
db = client.restaurants
coll = db.seattle_only_meta

# EB looks for an 'application' callable by default.
app = Flask(__name__)
# mongo = PyMongo(restaurants)

@app.route('/')
def homepage():

    print 'homepage!'
    return render_template('index.html')
    # return header_text + say_hello() + instructions + footer_text

@app.route('/search')
def search():
    data = coll.find({'reviews': {'$exists' : True}}, {'reviews': 0})
    return json_util.dumps(data)


    # return open("yelp_no_rev.json", "r")
    # return mongo.db.seattle_only_meta.find()
    # with open("./data/seattle_no_rev.json", "r") as f:
        # return json.load(f)
    
# add a rule for the index page.
# app.add_url_rule('/', 'index', (lambda: )

# add a rule when the page is accessed with a name appended to the site
# URL.
# app.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
