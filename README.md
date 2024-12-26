# 스파르타 마켓 (Sparta Market)

스파르타 코딩클럽 회원들을 위한 중고거래 플랫폼입니다.

## 프로젝트 소개

스파르타 마켓은 Django 기반의 중고거래 웹 애플리케이션으로, 사용자들이 중고 물품을 등록하고 찜하기 기능을 통해 관심 상품을 저장할 수 있습니다.

## 주요 기능

### 1. 회원 기능
- 회원가입/로그인/로그아웃
- 프로필 페이지
- 팔로우/팔로잉 기능

### 2. 상품 기능
- 상품 등록/수정/삭제
- 상품 목록 조회
- 상품 상세 정보 조회
- 찜하기 기능

## 기술 스택

- Backend: Django 4.2
- Database: SQLite
- Frontend: HTML, CSS (Bootstrap 5)

## 프로젝트 구조
spartamarket/
├── accounts/              # 사용자 관련 앱
├── products/             # 상품 관련 앱
├── templates/            # 공통 템플릿
├── media/               # 미디어 파일 (이미지 등)
└── spartamarket/        # 프로젝트 설정

## 실행 방법

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

2. 필요한 패키지 설치
pip install django pillow

3. 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

4. 서버 실행
python manage.py runserver

5. 웹 브라우저에서 접속
http://127.0.0.1:8000 으로 접속

