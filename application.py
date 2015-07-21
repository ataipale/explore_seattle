import json, requests
from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from bson import json_util

client = MongoClient()
db = client.restaurants
coll = db.seattle_only_meta

user_agent = request.headers.get('User-Agent')

app = Flask(__name__)

@app.route('/')
def homepage():

    if "Mozilla" in user_agent:
        return render_template('index_mozilla.html')
    else:
        return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/contact')
def contact():

    return redirect("http://www.alextaipale.com/about", code=302)


@app.route('/search')
def search():
    data = coll.find({'reviews': {'$exists' : True}}, {'reviews': 0})
    return json_util.dumps(data)


# run the app.
if __name__ == "__main__":

    app.run(host='0.0.0.0')
