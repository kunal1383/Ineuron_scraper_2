import pymongo
import json
import dns
import logging
import os
from utils import MONGO_USERNAME ,MONGO_PASSWORD ,MONGO_DB

class MongoDBHandler:
    def __init__(self):
        self.client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.thebkor.mongodb.net/")
        self.db = self.client[MONGO_DB]
        
        log_directory = 'MongoDB'
        log_file = 'mongodb.log'
        os.makedirs(log_directory, exist_ok=True)
        
        # Create a new logger
        self.logger = logging.getLogger('MongoDBHandler')
        self.logger.setLevel(logging.INFO)
        
        # Create a file handler for the logger
        file_handler = logging.FileHandler(os.path.join(log_directory, log_file))
        file_handler.setLevel(logging.INFO)
        
        # Create a formatter and set it for the file handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

        

    def insert_courses_into_collection(self, collection_name, courses_json):
        self.logger.info(f'connecting to mongodb')
        self.logger.info(f'{self.db}')

        try:
            if collection_name in self.db.list_collection_names():
                self.logger.info(f'Collection : {collection_name}')
                collection = self.db[collection_name]
            else:
                self.logger.info(f'{collection_name} creating new collection')
                collection = self.db.create_collection(collection_name)
                
            self.logger.info('Inserting into collection')
            courses = json.loads(courses_json)
            collection.insert_many(courses)
            self.logger.info(f"Inserted {len(courses)} courses into the collection '{collection_name}'")
            self.logger.info(f"Completed inserting data into mongodb")
               
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            raise Exception 