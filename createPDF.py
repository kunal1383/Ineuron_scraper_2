import logging
import os
import urllib.parse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

os.makedirs('PDFLog', exist_ok=True)
logging.basicConfig(filename='PDFLog/PDFLOG.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFCreator:
    def __init__(self):
        pass
        

    def create_pdf(self, course_details, course_category):
        logging.info("Creating PDFs")
        try:
            for course in course_details:
                # Generate a filename for the PDF based on the course title
                try:
                    # Generate the filename based on the course title
                    filename = course['course'].lower().replace(' ', '_') + '.pdf'
                except KeyError:
                    # If the 'course' key is not present, assign a default filename
                    logging.error('Title not found')
                    filename = 'unknown.pdf'

                # Generate the file path for the PDF inside the "courses_pdf" folder
                try:
                    folder_path = os.path.join('courses_pdf', course_category)
                    os.makedirs(folder_path, exist_ok=True)
                    file_path = os.path.join(folder_path, filename)
                    logging.info(f'folder_path:{folder_path}, file_path:{file_path}')
                except Exception as e:
                    logging.error(f'Unsuccessful to create directory due to {e}')
                    raise Exception('Failed to create PDF')

                # Create a new PDF document
                doc = SimpleDocTemplate(file_path, pagesize=letter)

                # Create a list to hold the PDF content
                content = []

                # Define styles for headings and paragraphs
                styles = getSampleStyleSheet()
                heading_style = styles['Heading1']
                paragraph_style = ParagraphStyle(
                    'normal',
                    parent=styles['BodyText'],
                    spaceAfter=12,
                    fontSize=11,
                    leading=14,
                )

                # Add the course title
                title = Paragraph(course['course'], heading_style)
                content.append(title)
                content.append(Spacer(1, 0.5 * inch))
                
                description = Paragraph(course['description'], paragraph_style)
                content.append(description)
                content.append(Spacer(1, 0.5 * inch))

                # Add the instructors section
                instructors_heading = Paragraph('<b>Instructors:</b>', paragraph_style)
                content.append(instructors_heading)

                for instructor in course['instructors']:
                    instructor_name = Paragraph(f'<b>{instructor["instructor_name"]}:</b>', paragraph_style)
                    instructor_description = Paragraph(instructor['instructor_description'], paragraph_style)

                    content.append(instructor_name)
                    content.append(instructor_description)
                    if 'instructor_social' in instructor:
                        instructor_social = instructor['instructor_social']
                        social_links = [f"• {platform}: {link}" for platform, link in instructor_social.items()]
                        social_links_paragraph = Paragraph("<br />".join(social_links), paragraph_style)
                        content.append(social_links_paragraph)

                    content.append(Spacer(1, 0.2 * inch))

                content.append(Spacer(1, 0.5 * inch))

                # Add the curriculum section
                curriculum_heading = Paragraph('<b>Curriculum:</b>', paragraph_style)
                content.append(curriculum_heading)
                for topic in course['topics']:
                    topic_title = Paragraph(f'•{topic}', paragraph_style)
                    content.append(topic_title)
                    
                content.append(Spacer(1, 0.5 * inch))    
                requirements = Paragraph('<b>Requirements:</b>', paragraph_style)
                content.append(requirements)    
                for item in course['requirements']:
                    curriculum_item = Paragraph(f"• {item}", paragraph_style)
                    content.append(curriculum_item)
                content.append(Spacer(1, 0.2 * inch))
                content.append(Spacer(1, 0.5 * inch))

                # Build the PDF document
                doc.build(content)
                logging.info(f"Created PDF for course: {course['course']}")
        except Exception as e:
            logging.error(f'Unsuccessful to create PDF due to {e}')
            raise Exception('Failed to create PDF')

    def generate_download_link(self, course_details, course_category):
        try:
            download_links = []
            for course in course_details:
                # Generate a filename for the PDF based on the course title
                try:
                    # Generate the filename based on the course title
                    filename = course['course'].lower().replace(' ', '_') + '.pdf'
                except KeyError:
                    # If the 'course' key is not present, assign a default filename
                    logging.error('Title not found')
                    filename = 'unknown.pdf'

                # Generate the file path for the PDF inside the "courses_pdf" folder
                try:
                    folder_path = os.path.join('courses_pdf', course_category)
                    file_path = os.path.join(folder_path, filename)
                    logging.info(f'folder_path:{folder_path}, file_path:{file_path}')
                except Exception as e:
                    logging.error(f'Unsuccessful to generate download link due to {e}')
                    continue

                # Generate the download link for the PDF
                try:
                    download_url = '/download?file=' + urllib.parse.quote(file_path)
                    download_links.append(download_url)
                    logging.info(f"Generated download link for course: {course['course']}")
                except Exception as e:
                    logging.error(f'Unsuccessful to generate download link due to {e}')

            return download_links
        except Exception as e:
            logging.error(f'Unsuccessful to generate download links due to {e}')
            raise Exception('Failed to generate download links')
