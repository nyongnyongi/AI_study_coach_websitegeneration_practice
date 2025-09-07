# AI 교육 전문가 팀

3명의 AI 전문가가 협력하여 맞춤형 AI 학습 가이드를 제공하는 Streamlit 웹 애플리케이션입니다.

주요 기능

- AI 개념 이해: 복잡한 AI 개념을 쉽게 설명
- AI 도구 사용법: 실무에서 AI 도구를 효과적으로 활용하는 방법
- AI 학습 계획: 개인 수준에 맞는 체계적인 학습 로드맵
- AI 윤리 및 안전: AI의 윤리적 사용과 안전한 활용 방법

전문가 팀(virtual)

1. 김민준 기초 전문가 (12년 경력)
   - AI 핵심 개념과 이론적 배경 설명
   - 복잡한 개념을 명확하게 전달

2. 박서연 실무 전문가 (10년 경력)
   - 실제 적용 사례와 업계 통찰력 제공
   - 이론을 실제 비즈니스 환경에서 활용하는 방법 안내

3. 이준호 학습 경로 전문가 (15년 경력)
   - 맞춤형 학습 계획과 자원 추천
   - 개인의 목표와 수준에 맞는 최적의 학습 경로 제안

사전 요구사항

- Python 3.8 이상
- Google AI Studio API 키

설치 및 실행

1. 저장소 클론 또는 파일 다운로드
```bash
# 프로젝트 디렉토리로 이동
cd "AI 코치"
```

2. 가상환경 생성 (권장)
```bash
# 가상환경 생성
python -m venv ai_coach_env

# 가상환경 활성화 (Windows)
ai_coach_env\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source ai_coach_env/bin/activate
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. Google AI Studio API 키 발급
1. [Google AI Studio](https://aistudio.google.com) 방문
2. Google 계정으로 로그인
3. "Get API key" 클릭하여 API 키 생성
4. 생성된 API 키를 복사하여 보관

5. 애플리케이션 실행
```bash
streamlit run ai_study_coach.py
```

6. 웹 브라우저에서 접속
- 자동으로 브라우저가 열리거나, 터미널에 표시된 URL로 접속
- 일반적으로: `http://localhost:8501`

사용 방법

1. API 키 입력: 사이드바에 Google AI Studio API 키 입력
2. 서비스 선택: 원하는 AI 교육 서비스 선택
3. 정보 입력: 각 서비스에 맞는 정보 입력
4. 가이드 생성: "학습 가이드 생성" 버튼 클릭
5. 결과 확인: 3명의 전문가가 협력하여 생성한 맞춤형 가이드 확인

프로젝트 구조

```
AI 코치/
├── ai_study_coach.py      # 메인 애플리케이션 파일
├── requirements.txt       # Python 의존성 목록
└── README.md             # 프로젝트 설명서
```

기술 스택

- Frontend: Streamlit
- AI Model: Google Gemini 2.5 Pro
- Language: Python 3.8+
- Dependencies: google-generativeai, streamlit

## CS 학생을 위한 스펙 가이드

### 1학년 (신입생)
기술 스택
- 프로그래밍 언어: Python 기초, C/C++ 기초
- 개발 환경: VS Code, PyCharm Community
- 버전 관리: Git 기초 명령어 (add, commit, push, pull)
- 운영체제: Windows/Linux 기본 사용법

GPA 목표
- 3.0 이상 (전공 3.2 이상 권장)

추천 스펙
- 수학: 미적분학, 이산수학 기초
- 컴퓨터 기초: 컴퓨터 구조론, 자료구조 기초
- 프로젝트: 간단한 계산기, 텍스트 게임 등

### 2학년
기술 스택
- 프로그래밍 언어: Python 중급, Java, JavaScript
- 웹 개발: HTML/CSS, React 기초
- 데이터베이스: SQL 기초, MySQL/PostgreSQL
- 개발 도구: Docker 기초, API 사용법

GPA 목표
- 3.2 이상 (전공 3.4 이상 권장)

추천 스펙
- 수학: 선형대수학, 확률통계
- 전공: 자료구조, 알고리즘, 소프트웨어공학
- 프로젝트: 웹사이트, 모바일 앱, 데이터 분석 프로젝트
- 인턴십: 스타트업 개발 인턴십

### 3학년
기술 스택
- 프로그래밍 언어: Python 고급, Java, C++, Go/Rust 중 하나
- 프레임워크: Spring Boot, Django/Flask, React/Vue.js
- 클라우드: AWS/Azure/GCP 기초
- DevOps: CI/CD, Kubernetes 기초
- AI/ML: TensorFlow/PyTorch 기초

GPA 목표
- 3.4 이상 (전공 3.6 이상 권장)

추천 스펙
- 수학: 선형대수학, 확률통계, 수치해석
- 전공: 운영체제, 컴퓨터네트워크, 데이터베이스시스템
- 프로젝트: 풀스택 웹 애플리케이션, AI/ML 프로젝트
- 인턴십: 대기업/중견기업 개발 인턴십
- 자격증: AWS Certified Cloud Practitioner, 정보처리기사

### 4학년
기술 스택
- 프로그래밍 언어: 3개 이상의 언어 숙련
- 아키텍처: 마이크로서비스, 분산시스템 설계
- 클라우드: AWS/Azure/GCP 중급 이상
- AI/ML: 머신러닝, 딥러닝 실무 적용
- 보안: 웹 보안, 암호학 기초

GPA 목표
- 3.6 이상 (전공 3.8 이상 권장)

추천 스펙
- 수학: 선형대수학, 확률통계, 수치해석, 최적화이론
- 전공: 컴퓨터그래픽스, 인공지능, 컴파일러, 보안
- 프로젝트: 오픈소스 기여, 대규모 시스템 설계
- 인턴십: 구글, 마이크로소프트, 네이버, 카카오 등
- 자격증: AWS Solutions Architect, Google Cloud Professional

### 졸업 후 취업 준비
기술 스택
- 프로그래밍 언어: 4개 이상의 언어 전문가 수준
- 아키텍처: 대규모 분산시스템 설계 및 운영
- 클라우드: 멀티클라우드 환경 구축
- AI/ML: MLOps, AI 모델 배포 및 운영
- 보안: 시큐어 코딩, 침투 테스트

추천 스펙
- 학위: 컴퓨터공학 학사 이상
- GPA: 3.5 이상 (대기업 3.7 이상)
- 프로젝트: 5개 이상의 완성된 프로젝트
- 경험: 2회 이상의 인턴십 또는 아르바이트
- 자격증: 3개 이상의 관련 자격증
- 포트폴리오: GitHub 100+ 커밋, 기술 블로그 운영

### 특화 분야별 추가 요구사항

웹 개발
- 프론트엔드: React, Vue.js, Angular 중 2개 이상
- 백엔드: Node.js, Python, Java, Go 중 2개 이상
- 데이터베이스: MySQL, PostgreSQL, MongoDB, Redis
- 클라우드: AWS EC2, S3, RDS, Lambda

모바일 개발
- 플랫폼: iOS (Swift), Android (Kotlin/Java)
- 크로스플랫폼: React Native, Flutter
- 백엔드: RESTful API, GraphQL
- 클라우드: Firebase, AWS Amplify

AI/ML
- 언어: Python, R, Julia
- 프레임워크: TensorFlow, PyTorch, Scikit-learn
- 클라우드: AWS SageMaker, Google AI Platform
- 수학: 선형대수학, 확률통계, 미적분학

데이터 사이언스
- 언어: Python, R, SQL
- 도구: Jupyter, Tableau, Power BI
- 클라우드: AWS Redshift, Google BigQuery
- 수학: 통계학, 확률론, 선형대수학

사이버보안
- 언어: Python, C/C++, Assembly
- 도구: Wireshark, Metasploit, Burp Suite
- 자격증: CISSP, CEH, Security+
- 네트워크: TCP/IP, 방화벽, IDS/IPS


