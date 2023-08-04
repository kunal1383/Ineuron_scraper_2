from flask import Flask, render_template, request,jsonify ,send_file
from flask import Response
#from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse
from urllib.request import urlopen as uReq
from scrapper import Scrapper

application = Flask(__name__)

app = application

@app.route('/' ,methods = ['POST' ,'GET'])
def homePage():
    return render_template("index.html")

@app.route('/search' ,methods = ['POST' ,'GET'])
def search():
     if request.method == "POST":
        scraper = Scrapper()
        search_query = request.form.get("search_query")
        category = request.form.get("category")
        
        if search_query:
            
            course_details ,download_links = scraper.scrape_course_details(search_query)
            
            return render_template("index.html" ,course_details = course_details ,download_links = download_links )
        elif category:
            
            course_details ,download_links= scraper.scrape_course_details(category)
            
            return render_template("index.html" ,course_details = course_details ,download_links = download_links )
        else:
            return "No search query provided."
     else:
        return "Method not allowed."
    

@app.route('/download', methods=['GET'])
def download_file():
    file_path = request.args.get('file')
    decoded_file_path = urllib.parse.unquote(file_path)
    return send_file(decoded_file_path, as_attachment=True)    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)