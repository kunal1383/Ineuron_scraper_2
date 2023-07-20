import requests
from bs4 import BeautifulSoup as bs
import json
import os
import logging
from utils import URL
from createPDF import PDFCreator

os.makedirs('ineuron_scraper', exist_ok=True)

# Configure logger for ineuron_scrapper module
ineuron_scrapper_logger = logging.getLogger('ineuron_scrapper_logger')
ineuron_scrapper_logger.setLevel(logging.INFO)
ineuron_scrapper_handler = logging.FileHandler('ineuron_scraper/ineuron_scraper.log')
ineuron_scrapper_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ineuron_scrapper_handler.setFormatter(ineuron_scrapper_formatter)
ineuron_scrapper_logger.addHandler(ineuron_scrapper_handler)


class IneuronScraper:
    def __init__(self):
        self.ineuron_url = URL
        self.course_json = None

    def get_page_content(self):
        try:
            ineuron_scrapper_logger.info("Getting page content")
            response = requests.get(self.ineuron_url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.HTTPError as e:
            ineuron_scrapper_logger.error("HTTP Error: " + str(e))
        except requests.exceptions.RequestException as e:
            ineuron_scrapper_logger.error("Error: " + str(e))
        except Exception as e:
            ineuron_scrapper_logger.error("An error occurred: " + str(e))

    def get_course_data(self, content):
        try:
            ineuron_scrapper_logger.info("Extracting course data")
            soup = bs(content, "html.parser")
            course_data = soup.find("script", {'id': "__NEXT_DATA__"})
            self.course_json = json.loads(course_data.text)
        except Exception as e:
            ineuron_scrapper_logger.error("An error occurred while extracting course data: " + str(e))

    def get_course_details(self, category_name):
        course_details_list = []
        
        try:
            ineuron_scrapper_logger.info(f"Getting course details for category: {category_name}")
            if self.course_json is None:
                return course_details_list

            courses = self.course_json['props']['pageProps']['initialState']['init']['courses']
            slug = list(courses.keys())

            for course in slug:
                if category_name.lower() in course.lower():
                    course_details = courses[course]
                    description = course_details['description']
                    timing = course_details.get('classTimings', {}).get('timings')
                    price = str(course_details.get('mobilePricing', {}).get('IN'))
                    topics = course_details['courseMeta'][0]['overview']['learn']
                    requirements = course_details['courseMeta'][0]['overview']['requirements']
                    instructors = course_details['instructorsDetails']
                    instructors_list = self.get_instructors_list(instructors)

                    course_info = {
                        'course': course,
                        'description': description,
                        'timing': str(timing),
                        'price': str(price),
                        'topics': topics,
                        'requirements': requirements,
                        'instructors': instructors_list
                    }
                    course_details_list.append(course_info)

                    ineuron_scrapper_logger.info("Fetching course details of: " + course)
                    ineuron_scrapper_logger.info("=" * 50)
                    

        except KeyError as e:
            ineuron_scrapper_logger.error("KeyError: " + str(e))
        except Exception as e:
            ineuron_scrapper_logger.error("An error occurred while getting course details: " + str(e))
        
        return course_details_list


    def get_instructors_list(self, instructors):
        instructors_list = []

        for instructor in instructors:
            instructor_details = {}
            instructor_details['instructor_name'] = instructor['name']
            instructor_details['instructor_description'] = instructor['description']
            if 'social' in instructor:
                instructor_details['instructor_social'] = instructor['social']
            instructors_list.append(instructor_details)

        return instructors_list