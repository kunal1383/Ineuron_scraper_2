import logging
import os
from ineuron_scrapper import IneuronScraper
from createPDF import PDFCreator
from mysqldb import SQLiteHandler
import json
from mongodb import MongoDBHandler

os.makedirs('Main_scraper', exist_ok=True)

# Configure logger for ineuron_scrapper module
ineuron_scraper_logger = logging.getLogger('main_scrapper_logger')
ineuron_scraper_logger.setLevel(logging.INFO)
ineuron_scraper_handler = logging.FileHandler('Main_scraper/main_scraper.log')
ineuron_scraper_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ineuron_scraper_handler.setFormatter(ineuron_scraper_formatter)
ineuron_scraper_logger.addHandler(ineuron_scraper_handler)

class Scrapper:
    def __init__(self):
        self.scraper = IneuronScraper()
        self.pdf_creator = PDFCreator()
        self.db_handler = SQLiteHandler()
        self.mongo_handler = MongoDBHandler()
        

    def scrape_course_details(self, category_name):
        try:
            content = self.scraper.get_page_content()
            self.scraper.get_course_data(content)
            course_details = self.scraper.get_course_details(category_name)
            #print(course_details)
            self.pdf_creator.create_pdf(course_details, category_name)
            download_links = self.pdf_creator.generate_download_link(course_details, category_name)
            
            self.db_handler.connect()
            self.db_handler.create_table(category_name)
            for course in course_details:
                # print("=="*50)
                
                course_name = course['course']
                # Get instructors if present, otherwise None
                instructors = course.get('instructors')  
                topics = course.get('topics') 
                # print(f"""coursse : {course['course']},
                #       instructor: {instructors},
                #       topics :{topics}
                #       """)
                self.db_handler.insert_course(course_name, instructors, topics ,category_name)

            self.db_handler.commit()
            self.db_handler.close()

            
            # Convert course_details to a JSON string
            courses_json = json.dumps(course_details)
            self.mongo_handler.insert_courses_into_collection(category_name, courses_json)
            
           
            return course_details ,download_links

        except Exception as e:
            logging.error("An error occurred while scraping course details: " + str(e))
            return None, None