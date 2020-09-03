from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Configuring mongo connection with flask_pymongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_mongo = mongo.db.mars_mongo.find_one()
    return render_template("index.html", mars_mongo=mars_mongo)



@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({},mars_data,upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
