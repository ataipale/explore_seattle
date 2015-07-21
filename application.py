import json, requests
from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from bson import json_util
# from flask.ext.pymongo import PyMongo

client = MongoClient()
db = client.restaurants
coll = db.seattle_only_meta

browser = request.headers.get('User-Agent')
print browser

# EB looks for an 'application' callable by default.
app = Flask(__name__)
# mongo = PyMongo(restaurants)

@app.route('/')
def homepage():

    print 'homepage!'
    return render_template('index.html')
    # return header_text + say_hello() + instructions + footer_text

@app.route('/about')
def about():

    print 'about!'
    return render_template('about.html')

@app.route('/contact')
def contact():

    print 'contact!'
    return redirect("http://www.alextaipale.com/about", code=302)


@app.route('/search')
def search():
    data = coll.find({'reviews': {'$exists' : True}}, {'reviews': 0})
    return json_util.dumps(data)


# run the app.
if __name__ == "__main__":

    app.run(host='0.0.0.0')
