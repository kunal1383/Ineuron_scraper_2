
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

Please make sure you have MongoDB Compass installed and have a MongoDB account with a username and password. You need to provide the MongoDB username and password in the `utils.py` file under the `MongoDB` class.

## Installation

1. Clone the project repository:

```bash
git clone https://github.com/kunalb1383/Ineuron-Scraper.git
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

4. You can find the generated PDF in the `output` directory.

## Contributing

Contributions to the Ineuron Scraper are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

The Ineuron Scraper is open-source and available under the [MIT License](LICENSE).

---

Please make sure that the project repository is actually named "Ineuron-Scraper" on GitHub under your "kunalb1383" account. If it's different, update the URL accordingly in the installation step. Also, ensure that the main script is named "application.py" as mentioned in your message.

Remember to update any other specific details related to your project in the README.md file.









