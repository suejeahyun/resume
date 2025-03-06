import pdfkit
import imgkit
from flask import current_app

def save_pdf():
    """현재 페이지를 PDF로 저장"""
    pdf_path = "static/output.pdf"
    url = current_app.config["BASE_URL"]  # 기본 URL을 가져옴
    pdfkit.from_url(url, pdf_path)
    return pdf_path

def save_jpg():
    """현재 페이지를 JPG로 저장"""
    img_path = "static/output.jpg"
    url = current_app.config["BASE_URL"]
    options = {"format": "jpg"}
    imgkit.from_url(url, img_path, options=options)
    return img_path
