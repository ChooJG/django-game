# Django Game Project

이 프로젝트는 Django를 기반으로 한 웹 애플리케이션입니다. 아래의 단계를 따라 로컬 환경에서 프로젝트를 설정하고 실행할 수 있습니다.

## 사전 준비

- Python이 설치되어 있어야 합니다. (Python 3.6+ 권장)
- 버전 관리를 위한 Git이 설치되어 있어야 합니다.

## 설정 방법

개발 환경을 설정하려면 다음 단계를 따르세요:

```shell
# 1. 가상 환경 생성
python -m venv venv

# 2. 실행 정책 설정 (Windows 전용)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 3. 가상 환경 활성화
# Windows에서:
.\venv\Scripts\activate
# macOS/Linux에서:
source venv/bin/activate

# 4. Django 설치
pip install django

# 5. Django REST Framework 설치
pip install djangorestframework

# 6. 프로젝트 디렉토리로 이동
cd .\firstdjango\

# 7. 개발 서버 실행
python manage.py runserver
