from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

client = pymongo.MongoClient('mongodb://localhost:27017/')

app = Flask(__name__)

db=client.mars_db
mars_data_db=db.mars

@app.route("/")
def index():
    mars = mars_data_db.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    
    mars = scrape_mars.scrape()
    mars_data_db.update({},mars, upsert=True)
    return redirect ("/")

 
if __name__ == "__main__":
    app.run(debug=True)