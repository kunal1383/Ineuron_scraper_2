
# Ineuron Scraper

Ineuron Scraper is a web scraping tool that extracts course details from the iNeuron website and stores them in a SQLite database and MongoDB. It also generates a PDF containing the course details and download links for each course.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

Ineuron Scraper is built to scrape course details from the iNeuron website using web scraping techniques. It extracts course information such as course name, instructors, curriculum, and other details. The data is then stored in a SQLite database and MongoDB for further analysis and retrieval.

## Features

- Web scraping of course details from iNeuron website.
- Storage of course details in a SQLite database and MongoDB.
- Generation of a PDF file containing course details and download links.
- Logging of activities and errors for debugging and monitoring.

## Requirements

To run the Ineuron Scraper, you need the following:

- Python 3.8
- Required Python packages (listed in `requirements.txt`)

**Important Note:** Please make sure you have MongoDB Atlas account with a username and password. You need to provide the MongoDB username and password in the `utils.py`.

## Installation

1. Clone the project repository:

```bash
git clone https://github.com/kunal1383/Ineuron-Scraper.git
```

2. Change to the project directory:

```bash
cd Ineuron-Scraper
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To use the Ineuron Scraper, follow these steps:

1. Run the main script to start the web scraping process:

```bash
python application.py
```

2. Enter the category name you want to scrape course details for.

3. The script will fetch course details, create a PDF, and store the data in both the SQLite database and MongoDB.

4. You can find the generated PDF in the `courses_pdf` directory.



## License

The Ineuron Scraper is open-source and available under the [MIT License](LICENSE).

---











