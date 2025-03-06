from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_mail import Message
from app.utils import generate_resume_pdf
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/resume')
def resume():
    return render_template('resume.html')

@main.route('/portfolio')
def portfolio():
    # 애플리케이션 루트 경로를 기준으로 static/img 폴더의 절대 경로 생성
    base_path = os.path.join(current_app.root_path, 'static', 'img')
    
    # 각 폴더에 대해 이미지 목록을 가져오기
    def get_images(folder):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            # 템플릿에서 사용할 경로는 static 폴더 기준으로 설정 (예: img/cctv1/슬라이드1.jpg)
            return [os.path.join('img', folder, f).replace("\\", "/") for f in sorted(os.listdir(folder_path)) if f.lower().endswith(('jpg', 'png', 'jpeg'))]
        else:
            return []
    
    cctv1_images = get_images('cctv1')
    cctv2_images = get_images('cctv2')
    papercup_images = get_images('papercup')
    
    # 로그 출력 (디버깅용)
    print("CCTV1 Images:", cctv1_images)
    print("CCTV2 Images:", cctv2_images)
    print("Papercup Images:", papercup_images)
    
    return render_template('portfolio.html', 
                           cctv1_images=cctv1_images,
                           cctv2_images=cctv2_images,
                           papercup_images=papercup_images)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')