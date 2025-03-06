from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import Response

def generate_resume_pdf():
    pdf_data = Response(content_type='application/pdf')
    pdf_data.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'

    c = canvas.Canvas(pdf_data, pagesize=letter)
    c.drawString(100, 750, "이름: 홍길동")
    c.drawString(100, 730, "이메일: hong@example.com")
    c.drawString(100, 710, "전화번호: 010-1234-5678")
    c.drawString(100, 690, "경력: Flask 개발자")

    c.save()
    return pdf_data
