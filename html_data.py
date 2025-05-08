# assets/html_data.py
from bs4 import BeautifulSoup

def read_html_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            # هنا هنقرأ البيانات من الـ HTML ونحفظها في شكل نص
            data = soup.get_text()
            return data
    except FileNotFoundError:
        return "Error: HTML file not found!"
