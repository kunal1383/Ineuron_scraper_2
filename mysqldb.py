import sqlite3
import os
import logging
import json

class SQLiteHandler:
    def __init__(self):
        self.db_file = 'courses.db'
        self.connection = None
        self.cursor = None
        log_directory = 'MYSQLdb'
        log_file = 'sqldb.log'
        os.makedirs(log_directory, exist_ok=True)
        
        # Create a new logger
        self.logger = logging.getLogger('SQLiteHandler')
        self.logger.setLevel(logging.INFO)
        
        # Create a file handler for the logger
        file_handler = logging.FileHandler(os.path.join(log_directory, log_file))
        file_handler.setLevel(logging.INFO)
        
        # Create a formatter and set it for the file handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add the file handler to the logger
        self.logger.addHandler(file_handler)
        
        if not os.path.exists(self.db_file):
            self.create_database()
    
    def create_database(self):
        try:
            self.connection = sqlite3.connect(self.db_file)  
            self.cursor = self.connection.cursor()
            self.logger.info(f'Successfully connected to SQLite database: {self.db_file}')
        except Exception as e:
            self.logger.error(f'Failed to connect to SQLite database: {e}')
            raise Exception 
        
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
        except Exception as e:
            self.logger.error(f'Failed to connect to SQLite database: {e}')
            raise Exception    
    
    def create_table(self, table_name):
        try:
            table_name = table_name.replace(' ', '_')
            query = f"""
             CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    instructors TEXT,
                    curriculum TEXT
                );
            """  
            self.cursor.execute(query)
            self.logger.info(f"Created table: {table_name}")
        except Exception as e:
            self.logger.error(f"An error occurred while creating table: {table_name}: {e}")
            
    def insert_course(self, title, instructors, curriculum, course):
        course = course.replace(' ', '_')
        try:
            query = f'INSERT INTO `{course}` (`title`, `instructors`, `curriculum`) VALUES (?, ?, ?)'
            instructors_json = json.dumps(instructors)
            topics_json = json.dumps(curriculum)
            values = (title, instructors_json,  topics_json)
            self.cursor.execute(query, values)
            self.logger.info('Data inserted successfully')
        except Exception as e:
            self.logger.error(f'Failed to insert data into the table: {e}')


    def commit(self):
        try:
            self.connection.commit()
            self.logger.info("Committed changes to the database")
        except Exception as e:
            self.logger.error(f"An error occurred while committing changes to the database: {e}")

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
            self.logger.info(f"Closed database connection: {self.db_file}")
        except Exception as e:
            self.logger.error(f"An error occurred while closing the database connection: {e}")
