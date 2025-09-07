"""
AI 교육 전문가 팀 - Streamlit 웹 애플리케이션
===============================================

이 애플리케이션은 3명의 AI 전문가가 협력하여 사용자에게 맞춤형 AI 학습 가이드를 제공합니다.

주요 기능:
- AI 개념 이해: 복잡한 AI 개념을 쉽게 설명
- AI 도구 사용법: 실무에서 AI 도구를 효과적으로 활용하는 방법
- AI 학습 계획: 개인 수준에 맞는 체계적인 학습 로드맵
- AI 윤리 및 안전: AI의 윤리적 사용과 안전한 활용 방법

전문가 팀:
1. 김민준 기초 전문가: AI 핵심 개념과 이론적 배경 설명
2. 박서연 실무 전문가: 실제 적용 사례와 업계 통찰력 제공
3. 이준호 학습 경로 전문가: 맞춤형 학습 계획과 자원 추천

사용 방법:
1. Google AI Studio에서 API 키 발급 (https://aistudio.google.com)
2. 사이드바에 API 키 입력
3. 원하는 서비스 선택
4. 필요한 정보 입력
5. '학습 가이드 생성' 버튼 클릭

필요한 라이브러리:
- streamlit
- google-generativeai
- datetime
- time
- json

작성자: AI 교육 전문가 팀
버전: 2.0
최종 업데이트: 2024
"""

# 필요한 라이브러리 임포트
import streamlit as st
from google.generativeai import GenerativeModel
import google.generativeai as genai
import os
from datetime import datetime
import time
import json

# ============================================================================
# 에이전틱 워크플로우 기반 AI 교육 팀 시스템
# 3명의 특화된 교육 전문가가 팀을 이루어 사용자를 지원
# ============================================================================

class AIEducationTeam:
    """
    AI 기반 교육 팀을 관리하는 클래스
    각 전문가의 협업을 조율하고 최종 결과를 제공
    """
    
    def __init__(self, api_key):
        """
        AI 교육 팀 초기화
        Args:
            api_key (str): Google AI API 키
        """
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = GenerativeModel('gemini-1.5-flash-8b')
        
        # 3명의 특화된 교육 전문가 초기화
        self.foundations_expert = AIFoundationsExpert(self.model)  # AI 기초 개념 전문가
        self.practical_expert = PracticalAIExpert(self.model)      # 실무 응용 전문가
        self.learning_expert = LearningPathExpert(self.model)      # 학습 경로 및 성장 전문가
        
        # 워크플로우 로그 초기화
        self.workflow_logs = []
    
    def get_ai_education(self, service_type, input_data):
        """
        사용자 요청에 따라 3명의 전문가가 순차적으로 협업하여 교육 지원 제공
        Args:
            service_type (str): 요청 서비스 유형
            input_data (dict): 사용자 입력 데이터
        Returns:
            str: 최종 교육 지원 결과
        """
        try:
            # 워크플로우 기록 시작
            workflow_log = {
                "service_type": service_type,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "experts_involved": ["AIFoundationsExpert", "PracticalAIExpert", "LearningPathExpert"],
                "steps": [],
                "status": "in_progress"
            }
            
            # 진행 상황 표시를 위한 컨테이너
            progress_container = st.container()
            
            with progress_container:
                # 1단계: AI 기초 전문가의 초기 분석 및 개념 설명
                st.markdown("### 🧠 1단계: AI 기초 개념 분석")
                with st.spinner("김민준 기초 전문가가 핵심 개념을 분석 중입니다..."):
                    initial_explanation = self.foundations_expert.explain(service_type, input_data)
                    workflow_log["steps"].append({
                        "expert": "AIFoundationsExpert",
                        "action": "initial_explanation",
                        "timestamp": datetime.now().strftime("%H:%M:%S")
                    })
                    st.success("✅ 기초 개념 분석 완료!")
                    time.sleep(1)  # 사용자 경험을 위한 짧은 대기
                
                # 2단계: 실무 응용 전문가의 실전 활용법 및 사례 추가
                st.markdown("### 💼 2단계: 실무 응용 분석")
                with st.spinner("박서연 실무 전문가가 실제 사례를 분석 중입니다..."):
                    practical_enhanced_explanation = self.practical_expert.enhance(initial_explanation, service_type, input_data)
                    workflow_log["steps"].append({
                        "expert": "PracticalAIExpert",
                        "action": "practical_enhancement",
                        "timestamp": datetime.now().strftime("%H:%M:%S")
                    })
                    st.success("✅ 실무 사례 분석 완료!")
                    time.sleep(1)
                
                # 3단계: 학습 경로 전문가의 맞춤형 학습 계획 및 자원 최적화
                st.markdown("### 📚 3단계: 맞춤형 학습 경로 설계")
                with st.spinner("이준호 학습 경로 전문가가 최종 학습 계획을 준비 중입니다..."):
                    final_guidance = self.learning_expert.finalize(practical_enhanced_explanation, service_type, input_data)
                    workflow_log["steps"].append({
                        "expert": "LearningPathExpert",
                        "action": "finalization",
                        "timestamp": datetime.now().strftime("%H:%M:%S")
                    })
                    st.success("✅ 학습 경로 설계 완료!")
            
            # 워크플로우 로그 저장
            workflow_log["status"] = "completed"
            self.workflow_logs.append(workflow_log)
            
            # 최종 결과 반환
            return final_guidance
            
        except Exception as e:
            st.error(f"❌ 오류가 발생했습니다: {str(e)}")
            workflow_log["status"] = "error"
            workflow_log["error"] = str(e)
            self.workflow_logs.append(workflow_log)
            return "죄송합니다. 처리 중 오류가 발생했습니다. 다시 시도해주세요."


class AIFoundationsExpert:
    """
    AI 기초 개념 전문가
    인공지능 핵심 개념, 이론적 배경, 기술 원리 담당
    """
    
    def __init__(self, model):
        self.model = model
        self.expertise = "ai_foundations"
        self.expert_name = "김민준 AI 기초 전문가"
        self.expert_intro = """
        안녕하세요, 김민준 AI 기초 전문가입니다. 
        저는 인공지능의 핵심 개념과 이론적 배경을 쉽게 설명합니다.
        12년간 AI 연구와 교육 경험을 바탕으로 복잡한 개념을 명확하게 전달해 드리겠습니다.
        """
    
    def explain(self, service_type, input_data):
        """
        사용자 요청에 대한 AI 기초 개념 설명 제공
        """
        try:
            # 서비스 유형별 맞춤 프롬프트 생성
            if service_type == "AI 개념 이해":
                prompt = self._create_concept_prompt(input_data)
            elif service_type == "AI 도구 사용법":
                prompt = self._create_tool_basics_prompt(input_data)
            elif service_type == "AI 학습 계획":
                prompt = self._create_learning_basics_prompt(input_data)
            elif service_type == "AI 윤리 및 안전":
                prompt = self._create_ethics_basics_prompt(input_data)
            elif service_type == "CS 학생 스펙 가이드":
                prompt = self._create_cs_spec_basics_prompt(input_data)
            else:
                prompt = self._create_general_foundations_prompt(input_data, service_type)
            
            # 전문가 정보 추가
            prompt = f"""
            당신은 '{self.expert_name}'이라는 AI 기초 개념 전문가입니다.
            {self.expert_intro}
            
            {prompt}
            
            설명 결과에 핵심 개념과 이론적 배경을 반드시 포함해 주세요.
            가능한 한 복잡한 용어는 피하고, 초보자도 이해할 수 있는 명확한 설명을 제공하세요.
            """
            
            # AI 모델을 통한 응답 생성
            response = self.model.generate_content(prompt)
            return response.text if response.text else "응답을 생성할 수 없습니다. 다시 시도해주세요."
            
        except Exception as e:
            return f"기초 개념 설명 중 오류가 발생했습니다: {str(e)}"
    
    def _create_concept_prompt(self, input_data):
        return f"""
        다음 AI 개념에 대해 기초적인 설명을 제공해주세요:
        
        {input_data.get('concept', '')}
        
        다음 항목을 포함하는 기초 설명을 제공해주세요:
        1. 개념의 정의와 핵심 원리
        2. 역사적 배경과 발전 과정
        3. 작동 방식의 기본 원리
        4. 해당 기술이 속한 AI 분야에서의 위치
        5. 이해하기 쉬운 비유나 예시
        """
    
    def _create_tool_basics_prompt(self, input_data):
        return f"""
        다음 AI 도구의 기본 원리와 개념에 대해 설명해주세요:
        
        도구 이름:
        {input_data.get('tool_name', '')}
        
        사용 목적:
        {input_data.get('purpose', '')}
        
        다음 항목을 포함하는 기초 설명을 제공해주세요:
        1. 해당 도구가 기반하는 AI 기술 설명
        2. 핵심 작동 원리와 알고리즘
        3. 비슷한 도구들과의 차이점
        4. 기술적 한계와 주의사항
        5. 초보자가 이해해야 할 핵심 개념
        """
    
    def _create_learning_basics_prompt(self, input_data):
        return f"""
        AI 학습을 위한 기초 개념과 배경 지식을 설명해주세요:
        
        현재 지식 수준:
        {input_data.get('current_level', '')}
        
        학습 목표:
        {input_data.get('goals', '')}
        
        다음 항목을 포함한 기초 설명을 제공해주세요:
        
        1. AI 학습을 위한 필수 기초 개념
           - 기계학습의 핵심 원리
           - 딥러닝과 신경망의 기초
           - AI 모델 학습 과정의 이해
        
        2. 학습 목표를 위해 알아야 할 이론적 배경
           - 관련 수학적/통계적 개념
           - 프로그래밍 관련 기초 지식
           - 데이터 관련 핵심 개념
        
        3. 학습 난이도와 선수 지식 설명
           - 필수적으로 알아야 할 개념
           - 추가적으로 도움이 될 배경 지식
           - 개념 간의 연결성과 학습 순서
        """
    
    def _create_ethics_basics_prompt(self, input_data):
        return f"""
        AI 윤리 및 안전에 관한 기초 개념을 설명해주세요:
        
        관심 분야:
        {input_data.get('area_of_interest', '')}
        
        다음 구조로 AI 윤리 및 안전의 기초 개념을 설명해주세요:
        
        1. AI 윤리의 기본 원칙
           - 핵심 윤리적 프레임워크
           - 주요 윤리적 고려사항
           - 산업 표준과 가이드라인
        
        2. AI 안전의 기술적 기초
           - 안전 관련 기술적 개념
           - 주요 위험 요소와 취약점
           - 안전 설계의 기본 원칙
        
        3. 법적/사회적 관점
           - 관련 규제와 정책 동향
           - 사회적 영향과 책임
           - 투명성과 설명 가능성의 중요성
        """
    
    def _create_cs_spec_basics_prompt(self, input_data):
        return f"""
        CS 학생을 위한 스펙 가이드의 기초 개념과 이론적 배경을 설명해주세요:
        
        현재 상황:
        {input_data.get('current_situation', '')}
        
        목표:
        {input_data.get('career_goals', '')}
        
        다음 항목을 포함한 기초 설명을 제공해주세요:
        
        1. CS 전공의 핵심 기초 개념
           - 컴퓨터과학의 기본 원리와 이론적 배경
           - 프로그래밍 언어의 분류와 특징
           - 자료구조와 알고리즘의 중요성
           - 소프트웨어 개발 생명주기
        
        2. 학년별 필수 이론 지식
           - 1-2학년: 기초 수학, 프로그래밍 기초, 컴퓨터 구조
           - 3-4학년: 고급 알고리즘, 시스템 설계, 전공 심화
           - 각 학년별로 필요한 수학적 배경과 이론적 기초
        
        3. 기술 스택의 이론적 이해
           - 웹 개발: HTTP, REST API, 데이터베이스 이론
           - 모바일 개발: 플랫폼별 아키텍처, 네이티브 vs 크로스플랫폼
           - AI/ML: 머신러닝 이론, 통계학, 선형대수학
           - 클라우드: 분산시스템, 마이크로서비스 아키텍처
        
        4. 학업 성취도와 GPA의 중요성
           - 전공 GPA의 의미와 중요성
           - 각 학년별 권장 GPA 목표
           - 수학, 전공 과목의 가중치와 중요도
        """
    
    def _create_general_foundations_prompt(self, input_data, service_type):
        return f"""
        다음 {service_type} 요청에 대해 AI 기초 개념 관점에서 설명해주세요:
        
        요청 내용:
        {str(input_data)}
        
        핵심 개념, 이론적 배경, 기술적 원리를 포함한 기초 설명을 제공해주세요.
        """


class PracticalAIExpert:
    """
    실무 응용 전문가
    AI 활용 사례, 실무 적용 방법, 현업 통찰력 제공 담당
    """
    
    def __init__(self, model):
        self.model = model
        self.expertise = "practical_applications"
        self.expert_name = "박서연 실무 응용 전문가"
        self.expert_intro = """
        안녕하세요, 박서연 실무 응용 전문가입니다.
        저는 AI의 실무 적용 방법과 현업 사례를 전문으로 합니다.
        10년간의 AI 프로젝트 구현 및 컨설팅 경험을 통해 이론을 실제로 적용하는 방법을 안내해 드리겠습니다.
        """
    
    def enhance(self, previous_explanation, service_type, input_data):
        """
        기초 전문가의 설명을 바탕으로 실무 응용 관점의 내용 추가
        """
        try:
            # 서비스 유형별 맞춤 프롬프트 생성
            if service_type == "AI 개념 이해":
                prompt = self._create_concept_practical_prompt(previous_explanation, input_data)
            elif service_type == "AI 도구 사용법":
                prompt = self._create_tool_practical_prompt(previous_explanation, input_data)
            elif service_type == "AI 학습 계획":
                prompt = self._create_learning_practical_prompt(previous_explanation, input_data)
            elif service_type == "AI 윤리 및 안전":
                prompt = self._create_ethics_practical_prompt(previous_explanation, input_data)
            elif service_type == "CS 학생 스펙 가이드":
                prompt = self._create_cs_spec_practical_prompt(previous_explanation, input_data)
            else:
                prompt = self._create_general_practical_prompt(previous_explanation, input_data, service_type)
            
            # 전문가 정보 추가
            prompt = f"""
            당신은 '{self.expert_name}'이라는 AI 실무 응용 전문가입니다.
            {self.expert_intro}
            
            AI 기초 전문가가 제공한 다음 설명을 검토하고, 실무 응용 관점에서 보완해주세요:
            
            === 기초 전문가의 설명 ===
            {previous_explanation}
            === 설명 끝 ===
            
            {prompt}
            
            구체적인 실무 사례, 적용 방법, 업계 동향과 트렌드를 반드시 포함해 주세요.
            """
            
            # AI 모델을 통한 응답 생성
            response = self.model.generate_content(prompt)
            return response.text if response.text else "실무 응용 설명을 생성할 수 없습니다. 다시 시도해주세요."
            
        except Exception as e:
            return f"실무 응용 설명 중 오류가 발생했습니다: {str(e)}"
    
    def _create_concept_practical_prompt(self, previous_explanation, input_data):
        return f"""
        앞서 설명된 AI 개념의 실무 활용 사례와 적용 방법을 제시해주세요:
        
        1. 해당 개념의 주요 산업별 활용 사례
           - 기술 기업에서의 활용법
           - 금융, 의료, 교육 등 다양한 분야의 적용 예시
           - 스타트업과 대기업의 적용 차이
        
        2. 실제 구현 시 고려사항
           - 일반적인 구현 과정과 단계
           - 자주 발생하는 문제점과 해결 방법
           - 필요한 인프라 및 리소스
        
        3. 최신 트렌드와 미래 전망
           - 현재 업계 동향과 기술 발전 방향
           - 주목할 만한 혁신 사례
           - 미래 잠재적 응용 분야
        
        원본 개념:
        {input_data.get('concept', '')}
        """
    
    def _create_tool_practical_prompt(self, previous_explanation, input_data):
        return f"""
        앞서 설명된 AI 도구의 실전 사용법과 활용 사례를 제시해주세요:
        
        1. 도구의 실제 사용 시나리오
           - 일반적인 사용 워크플로우
           - 효과적인 활용을 위한 설정 및 팁
           - 고급 활용법과 숨겨진 기능
        
        2. 산업별 활용 사례
           - 대표적인 성공 사례 분석
           - 실제 비즈니스 가치와 ROI
           - 사용자 피드백과 평가
        
        3. 유사 도구와의 비교 및 통합
           - 경쟁 도구와의 장단점 비교
           - 다른 AI 도구와의 통합 방법
           - 생태계 내 위치와 호환성
        
        도구 이름:
        {input_data.get('tool_name', '')}
        
        사용 목적:
        {input_data.get('purpose', '')}
        """
    
    def _create_learning_practical_prompt(self, previous_explanation, input_data):
        return f"""
        AI 학습을 위한 실무 중심 접근법과 실전 적용 방법을 제안해주세요:
        
        1. 실무 중심 학습 방법론
           - 프로젝트 기반 학습 접근법
           - 실제 문제 해결을 통한 학습 전략
           - 업계 표준 도구 및 워크플로우 습득법
        
        2. 실전 경험 구축 방법
           - 포트폴리오 프로젝트 아이디어
           - 오픈소스 기여 및 커뮤니티 참여 방법
           - 인턴십 및 실무 경험 확보 전략
        
        3. 업계 연결 및 네트워킹
           - 주요 커뮤니티 및 컨퍼런스 소개
           - 전문가 네트워킹 구축 방법
           - AI 분야 취업/전환 준비 전략
        
        현재 지식 수준:
        {input_data.get('current_level', '')}
        
        학습 목표:
        {input_data.get('goals', '')}
        """
    
    def _create_ethics_practical_prompt(self, previous_explanation, input_data):
        return f"""
        AI 윤리 및 안전의 실무 적용 방법과 사례를 제시해주세요:
        
        1. 윤리적 설계 및 개발 실무
           - 윤리적 AI 개발 프로세스 및 프레임워크
           - 실제 프로젝트에서의 윤리적 검토 방법
           - 윤리적 문제 발견 및 해결 사례
        
        2. 규제 준수 및 거버넌스
           - 주요 규제 준수 전략
           - 윤리위원회 및 감독 메커니즘 구축
           - 문서화 및 투명성 확보 방법
        
        3. 현업 사례 분석
           - 윤리적 문제로 인한 실패 사례
           - 성공적인 윤리적 AI 구현 사례
           - 업계별 특수한 윤리적 고려사항
        
        관심 분야:
        {input_data.get('area_of_interest', '')}
        """
    
    def _create_cs_spec_practical_prompt(self, previous_explanation, input_data):
        return f"""
        CS 학생을 위한 스펙 가이드의 실무 적용 사례와 업계 동향을 제시해주세요:
        
        현재 상황:
        {input_data.get('current_situation', '')}
        
        목표:
        {input_data.get('career_goals', '')}
        
        다음 항목을 포함한 실무 관점의 설명을 제공해주세요:
        
        1. 업계별 실제 요구사항과 스펙
           - 빅테크 (구글, 마이크로소프트, 아마존): 알고리즘, 시스템 설계, 클라우드
           - 스타트업: 풀스택 개발, 빠른 학습 능력, 다양한 기술 스택
           - 금융/핀테크: 보안, 규정 준수, 고성능 시스템
           - 게임/엔터테인먼트: 실시간 처리, 그래픽스, 최적화
        
        2. 학년별 실무 경험 구축 방법
           - 1-2학년: 개인 프로젝트, 해커톤 참여, 오픈소스 기여
           - 3-4학년: 인턴십, 대회 참여, 스타트업 아르바이트
           - 졸업 후: 포트폴리오 구축, 네트워킹, 기술 블로그
        
        3. 실제 채용 프로세스와 평가 기준
           - 코딩 테스트: 알고리즘, 자료구조, 문제 해결 능력
           - 기술 면접: 시스템 설계, 아키텍처, 트레이드오프
           - 포트폴리오: 프로젝트의 기술적 깊이와 비즈니스 임팩트
           - 소프트 스킬: 커뮤니케이션, 팀워크, 학습 능력
        
        4. 최신 기술 트렌드와 업계 동향
           - AI/ML: MLOps, LLM, 생성형 AI
           - 클라우드: 멀티클라우드, 서버리스, 컨테이너
           - 웹 개발: JAMstack, 마이크로프론트엔드, WebAssembly
           - 모바일: 크로스플랫폼, PWA, 모바일 최적화
        """
    
    def _create_general_practical_prompt(self, previous_explanation, input_data, service_type):
        return f"""
        다음 {service_type} 요청에 대해 AI 실무 응용 관점에서 분석해주세요:
        
        요청 내용:
        {str(input_data)}
        
        실제 활용 사례, 구현 방법, 업계 트렌드를 구체적으로 제시해주세요.
        """


class LearningPathExpert:
    """
    학습 경로 및 성장 전문가
    맞춤형 학습 계획, 교육 자원, 성장 로드맵 설계 담당
    """
    
    def __init__(self, model):
        self.model = model
        self.expertise = "learning_pathways"
        self.expert_name = "이준호 학습 경로 전문가"
        self.expert_intro = """
        안녕하세요, 이준호 학습 경로 전문가입니다.
        저는 AI 학습 계획 수립과 성장 로드맵 설계를 전문으로 합니다.
        15년간의 교육 경험을 바탕으로 여러분에게 최적화된 학습 경로를 제안해 드리겠습니다.
        """
    
    def finalize(self, previous_explanation, service_type, input_data):
        """
        기초 전문가와 실무 전문가의 설명을 바탕으로 최종 학습 경로 제안
        """
        try:
            # 서비스 유형별 맞춤 프롬프트 생성
            if service_type == "AI 개념 이해":
                prompt = self._create_concept_learning_prompt(previous_explanation, input_data)
            elif service_type == "AI 도구 사용법":
                prompt = self._create_tool_learning_prompt(previous_explanation, input_data)
            elif service_type == "AI 학습 계획":
                prompt = self._create_comprehensive_learning_prompt(previous_explanation, input_data)
            elif service_type == "AI 윤리 및 안전":
                prompt = self._create_ethics_learning_prompt(previous_explanation, input_data)
            elif service_type == "CS 학생 스펙 가이드":
                prompt = self._create_cs_spec_learning_prompt(previous_explanation, input_data)
            else:
                prompt = self._create_general_learning_prompt(previous_explanation, input_data, service_type)
            
            # 전문가 정보 추가
            prompt = f"""
            당신은 '{self.expert_name}'이라는 학습 경로 전문가입니다.
            {self.expert_intro}
            
            기초 전문가와 실무 응용 전문가가 제공한, 다음 설명을 검토하고 최종적으로 학습 경로를 완성해주세요:
            
            === 이전 전문가들의 설명 ===
            {previous_explanation}
            === 설명 끝 ===
            
            {prompt}
            
            최종 안내에는 다음 세 전문가의 관점이 균형있게 통합되어야 합니다:
            1. 기초 개념 전문가 (핵심 개념과 이론적 배경)
            2. 실무 응용 전문가 (실제 적용 사례와 업계 통찰력)
            3. 학습 경로 전문가 (개인화된 학습 계획과 자원)
            
            명확하고 실행 가능한 단계별 학습 가이드를 제공해주세요.
            """
            
            # AI 모델을 통한 응답 생성
            response = self.model.generate_content(prompt)
            return response.text if response.text else "학습 경로를 생성할 수 없습니다. 다시 시도해주세요."
            
        except Exception as e:
            return f"학습 경로 생성 중 오류가 발생했습니다: {str(e)}"
    
    def _create_concept_learning_prompt(self, previous_explanation, input_data):
        return f"""
        해당 AI 개념을 효과적으로 학습하기 위한 맞춤형 학습 경로를 제안해주세요:
        
        1. 단계별 학습 계획
           - 초보자부터 전문가까지의 학습 단계
           - 각 단계별 핵심 목표와 성취 지표
           - 예상 소요 시간과 난이도
        
        2. 최적의 학습 자원
           - 추천 온라인 강의, 책, 튜토리얼
           - 무료 및 유료 자원 균형있는 추천
           - 자기주도 학습 vs 지도 학습 옵션
        
        3. 실습 및 응용 프로젝트
           - 단계별 핸즈온 프로젝트 아이디어
           - 학습 내용 검증을 위한 미니 프로젝트
           - 포트폴리오에 추가할 수 있는 응용 과제
        
        4. 학습 진행 측정 및 피드백 방법
           - 자가 평가 방법
           - 지식 검증 및 진단 도구
           - 커뮤니티 피드백 활용법
        
        원본 개념:
        {input_data.get('concept', '')}
        """
    
    def _create_tool_learning_prompt(self, previous_explanation, input_data):
        return f"""
        해당 AI 도구의 숙련도를 높이기 위한 학습 경로를 제안해주세요:
        
        1. 도구 숙련 로드맵
           - 초보자부터 전문가까지의 학습 단계
           - 단계별 기능 익히기 순서
           - 숙련도 수준별 목표와 평가 방법
        
        2. 실습 중심 학습 계획
           - 핵심 기능별 실습 과제
           - 난이도별 프로젝트 아이디어
           - 실전 시나리오 기반 연습
        
        3. 보완 학습 자원
           - 공식 및 비공식 문서와 튜토리얼
           - 커뮤니티 및 포럼 활용법
           - 전문가 인사이트 및 고급 팁 확보 방법
        
        4. 지속적 역량 개발 전략
           - 최신 기능 및 업데이트 학습법
           - 관련 도구 및 확장 기술 습득
           - 전문성 증명 및 인증 방법
        
        도구 이름:
        {input_data.get('tool_name', '')}
        
        사용 목적:
        {input_data.get('purpose', '')}
        """
    
    def _create_comprehensive_learning_prompt(self, previous_explanation, input_data):
        return f"""
        목표 달성을 위한 종합적인 AI 학습 로드맵을 제안해주세요:
        
        1. 개인화된 학습 경로
           - 현재 수준에서 목표까지의 단계별 계획
           - 학습자 특성에 맞는 접근법 및 방법론
           - 단기/중기/장기 목표 설정 및 마일스톤
        
        2. 핵심 학습 자원 큐레이션
           - 온라인 코스, 책, 튜토리얼 등 선별된 자원
           - 품질과 적합성 기준의 자원 평가
           - 비용 효율적인 학습 자원 활용 전략
        
        3. 실전 경험 구축 프레임워크
           - 단계적 프로젝트 구성 계획
           - 포트폴리오 구축 전략
           - 실전 환경 시뮬레이션 및 연습 방법
        
        4. 지속적 피드백 및 개선 시스템
           - 진행 상황 모니터링 및 평가 방법
           - 멘토십 및 코칭 활용 전략
           - 학습 습관 및 효율성 개선 방법
        
        5. 학습 여정 시간표
           - 주간/월간/분기별 학습 일정 제안
           - 시간 관리 및 학습 균형 전략
           - 장애물 극복 및 동기 유지 방법
        
        현재 지식 수준:
        {input_data.get('current_level', '')}
        
        학습 목표:
        {input_data.get('goals', '')}
        """
    
    def _create_ethics_learning_prompt(self, previous_explanation, input_data):
        return f"""
        AI 윤리 및 안전에 대한 체계적인 학습 경로를 제안해주세요:
        
        1. 윤리적 AI 역량 개발 로드맵
           - 기초부터 고급까지의 학습 단계
           - 역할별 필요 지식과 역량(개발자/관리자/정책입안자)
           - 윤리적 사고방식과 평가 능력 개발
        
        2. 추천 학습 자원
           - 교재, 온라인 코스, 케이스 스터디
           - 윤리적 프레임워크 및 도구
           - 인증 및 전문가 과정
        
        3. 실습 및 토론 기반 학습
           - 윤리적 딜레마 시나리오 분석
           - 그룹 토론 및 사례 연구 방법
           - 윤리적 감사 및 평가 실습
        
        4. 지속적인 역량 발전 계획
           - 윤리적 AI 분야 최신 동향 파악 방법
           - 전문가 커뮤니티 및 컨퍼런스 참여
           - 자기 평가 및 성찰 방법론
        
        관심 분야:
        {input_data.get('area_of_interest', '')}
        """
    
    def _create_cs_spec_learning_prompt(self, previous_explanation, input_data):
        return f"""
        CS 학생을 위한 맞춤형 스펙 구축 학습 경로를 제안해주세요:
        
        현재 상황:
        {input_data.get('current_situation', '')}
        
        목표:
        {input_data.get('career_goals', '')}
        
        다음 구조로 구체적인 학습 경로를 제안해주세요:
        
        1. 단계별 스펙 구축 로드맵
           - 1단계 (1-3개월): 기초 기술 스택 완성
           - 2단계 (3-6개월): 프로젝트 경험 쌓기
           - 3단계 (6-12개월): 전문 분야 심화
           - 4단계 (12개월+): 포트폴리오 완성 및 취업 준비
        
        2. 학년별 구체적인 학습 계획
           - 1학년: 프로그래밍 기초, 수학 기초, 컴퓨터 구조
           - 2학년: 자료구조/알고리즘, 웹 개발 기초, 데이터베이스
           - 3학년: 프레임워크 숙련, 클라우드 기초, 인턴십 준비
           - 4학년: 전문 분야 심화, 포트폴리오 완성, 취업 준비
        
        3. 추천 학습 자원과 도구
           - 온라인 강의: Coursera, edX, Udemy, 인프런
           - 책: 각 분야별 필수 서적과 참고서
           - 실습 환경: GitHub, AWS Free Tier, Docker
           - 커뮤니티: Stack Overflow, Reddit, 기술 블로그
        
        4. 프로젝트 포트폴리오 구축 전략
           - 개인 프로젝트: 3-5개의 완성된 프로젝트
           - 오픈소스 기여: GitHub 활동, 기여도 증명
           - 기술 블로그: 학습 과정과 프로젝트 기록
           - 대회 참여: 해커톤, 알고리즘 대회, 해커랭크
        
        5. GPA 관리 및 학업 전략
           - 전공 과목 우선순위와 학습 방법
           - 수학 과목의 중요성과 학습 전략
           - 프로젝트와 학업의 균형 맞추기
           - 각 학년별 목표 GPA 설정
        
        6. 취업 준비 체크리스트
           - 이력서 작성: 기술 스택, 프로젝트 경험
           - 포트폴리오 사이트: GitHub Pages, 개인 웹사이트
           - 코딩 테스트 준비: LeetCode, 프로그래머스
           - 면접 준비: 기술 면접, 시스템 설계, 행동 면접
        
        7. 네트워킹과 커리어 개발
           - 기술 컨퍼런스 참여: PyCon, JSConf, AWS Summit
           - 멘토링: 선배, 교수, 업계 전문가
           - 인턴십 신청: 대기업, 스타트업, 중견기업
           - 자격증 취득: AWS, Google Cloud, 정보처리기사
        """
    
    def _create_general_learning_prompt(self, previous_explanation, input_data, service_type):
        return f"""
        다음 {service_type} 요청에 대해 학습 경로 관점에서 맞춤형 계획을 제안해주세요:
        
        요청 내용:
        {str(input_data)}
        
        체계적인 학습 단계, 추천 자원, 실습 계획, 진행 평가 방법을 구체적으로 제시해주세요.
        """


# ============================================================================
# Streamlit 웹 애플리케이션 구현
# ============================================================================

def main():
    """
    메인 함수: Streamlit 웹 애플리케이션의 메인 로직
    """
    # 페이지 기본 설정
    st.set_page_config(
        page_title="AI 교육 전문가 팀",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # 세션 상태 초기화
    if 'workflow_logs' not in st.session_state:
        st.session_state.workflow_logs = []
    if 'current_team' not in st.session_state:
        st.session_state.current_team = None
    
    # 페이지 제목 및 설명
    st.title("🧠 AI 교육 전문가 팀")
    st.markdown("""
    ### 3명의 전문 교육가가 협업하여 맞춤형 AI 학습 가이드를 제공합니다
    
    * **김민준 기초 전문가**: 핵심 개념과 이론적 배경 설명
    * **박서연 실무 전문가**: 실제 응용 사례와 현업 통찰력 제공
    * **이준호 학습 경로 전문가**: 맞춤형 학습 계획과 자원 추천
    """)
    st.markdown("---")
    
    # 사이드바 설정
    with st.sidebar:
        st.header("🔑 API 설정")
        # API 키 입력 필드 (비밀번호 형식)
        api_key = st.text_input("Google API 키를 입력하세요", type="password", help="Google AI Studio에서 발급받은 API 키를 입력하세요")
        
        # API 키가 입력되지 않은 경우 경고 메시지 표시
        if not api_key:
            st.warning("API 키를 입력해주세요.")
            st.info("💡 Google AI Studio (https://aistudio.google.com)에서 무료로 API 키를 발급받을 수 있습니다.")
            st.stop()
        
        # API 키 유효성 검사
        try:
            if st.session_state.current_team is None or st.session_state.current_team.api_key != api_key:
                st.session_state.current_team = AIEducationTeam(api_key)
                st.success("✅ API 키가 유효합니다!")
        except Exception as e:
            st.error(f"❌ API 키 오류: {str(e)}")
            st.stop()
            
        st.markdown("---")
        
        # 워크플로우 통계
        if st.session_state.workflow_logs:
            st.markdown("### 📊 워크플로우 통계")
            total_requests = len(st.session_state.workflow_logs)
            successful_requests = len([log for log in st.session_state.workflow_logs if log.get('status') == 'completed'])
            st.metric("총 요청 수", total_requests)
            st.metric("성공한 요청", successful_requests)
            
            if st.button("🗑️ 로그 초기화"):
                st.session_state.workflow_logs = []
                st.rerun()
            
            st.markdown("---")
        
        # 전문가 소개
        st.markdown("### 🧠 전문가 소개")
        
        expert_tab = st.selectbox("전문가 정보 보기", 
                                ["김민준 기초 전문가", "박서연 실무 전문가", "이준호 학습 경로 전문가"])
        
        if expert_tab == "김민준 기초 전문가":
            st.markdown("""
            **김민준 기초 전문가**
            
            AI 기초 개념 전문가로 12년간 인공지능 연구와 교육을 담당했습니다.
            복잡한 AI 개념을 명확하고 이해하기 쉽게 설명합니다.
            
            * 전문 분야: 머신러닝 이론, 딥러닝 아키텍처, 알고리즘 원리
            * 경력: 국내 주요 AI 연구소, 글로벌 테크 기업 AI 교육 담당
            * 학력: 컴퓨터과학 박사, AI 및 머신러닝 전공
            """)
        
        elif expert_tab == "박서연 실무 전문가":
            st.markdown("""
            **박서연 실무 전문가**
            
            AI 실무 응용 전문가로 10년간 AI 프로젝트 구현 및 컨설팅을 담당했습니다.
            이론을 실제 비즈니스 환경에서 어떻게 활용하는지 안내합니다.
            
            * 전문 분야: AI 비즈니스 적용, 산업별 활용 사례, 프로젝트 구현
            * 경력: 스타트업 CTO, 대기업 AI 솔루션 아키텍트, 독립 AI 컨설턴트
            * 학력: 컴퓨터공학 학사, AI 및 데이터 사이언스 석사
            """)
        
        elif expert_tab == "이준호 학습 경로 전문가":
            st.markdown("""
            **이준호 학습 경로 전문가**
            
            AI 학습 계획 전문가로 15년간 맞춤형 교육과 커리큘럼 설계를 담당했습니다.
            개인의 목표와 수준에 맞는 최적의 학습 경로를 제안합니다.
            
            * 전문 분야: 학습 경로 설계, 교육 자원 큐레이션, 학습 방법론
            * 경력: 교육 플랫폼 디렉터, AI 교육 컨설턴트, 대학 교수
            * 학력: 교육학 박사, 인지과학 및 학습 설계 전공
            """)
            
        st.markdown("---")
        # 사용 방법 안내
        st.markdown("### ℹ️ 사용 방법")
        st.markdown("""
        1. API 키를 입력하세요
        2. 원하는 서비스를 선택하세요
        3. 필요한 정보를 입력하세요
        4. '학습 가이드 생성' 버튼을 클릭하면 3명의 전문가가 순차적으로 분석합니다
        5. 최종 학습 가이드를 확인하세요
        """)
    
    # 서비스 선택 드롭다운
    st.markdown("### 🎯 서비스 선택")
    service = st.selectbox(
        "원하는 서비스를 선택하세요",
        ["AI 개념 이해", "AI 도구 사용법", "AI 학습 계획", "CS 학생 스펙 가이드", "AI 윤리 및 안전"],
        help="각 서비스는 3명의 전문가가 협력하여 맞춤형 가이드를 제공합니다"
    )
    
    # 서비스 설명
    service_descriptions = {
        "AI 개념 이해": "AI의 기본 개념과 원리를 쉽게 이해하고 싶을 때",
        "AI 도구 사용법": "특정 AI 도구를 효과적으로 활용하는 방법을 배우고 싶을 때",
        "AI 학습 계획": "체계적인 AI 학습 로드맵과 계획이 필요할 때",
        "CS 학생 스펙 가이드": "컴퓨터공학 전공 학생을 위한 구체적인 스펙 로드맵이 필요할 때",
        "AI 윤리 및 안전": "AI의 윤리적 사용과 안전한 활용에 대해 알고 싶을 때"
    }
    
    st.info(service_descriptions[service])
    st.markdown("---")
    
    # 카드 스타일 CSS
    st.markdown("""
    <style>
    .expert-card {
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .foundations-expert {
        background-color: #E8F4F9;
        border-left: 5px solid #0077B6;
    }
    .practical-expert {
        background-color: #E8F9E9;
        border-left: 5px solid #2D6A4F;
    }
    .learning-expert {
        background-color: #F9F3E8;
        border-left: 5px solid #D4A017;
    }
    .final-guidance {
        background-color: #F2F2F2;
        border: 2px solid #555555;
        border-radius: 10px;
        padding: 25px;
        margin-top: 30px;
        color: #222;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 워크플로우 설명
    with st.expander("에이전틱 워크플로우 프로세스 보기"):
        st.markdown("""
        ### 에이전틱 워크플로우 프로세스
        
        1. **요청 분석**: 사용자 요청을 분석하여 필요한 전문성 식별
        2. **팀 구성**: 각 요청에 최적화된 AI 전문가 팀 구성
        3. **개념 설명**: AI 기초 전문가가 핵심 개념과 이론적 배경 설명
        4. **실무 응용**: 실무 전문가가 실제 적용 사례와 업계 통찰력 제공
        5. **학습 계획**: 학습 경로 전문가가 맞춤형 학습 계획과 자원 추천
        6. **통합 가이드**: 세 전문가의 관점을 통합한 최종 맞춤형 학습 가이드 제공
        
        각 전문가는 독립적인 전문성을 가지고 있으며, 순차적 협업을 통해 종합적인 관점을 제공합니다.
        """)
    
    # 선택된 서비스에 따른 UI 표시
    if service == "AI 개념 이해":
        st.subheader("🧩 AI 개념 이해")
        
        # 예시 제공
        with st.expander("💡 예시 보기"):
            st.markdown("""
            **추천 입력 예시:**
            - 머신러닝이 무엇인지 알고 싶어요
            - 딥러닝과 머신러닝의 차이점은 무엇인가요?
            - 자연어 처리는 어떻게 작동하나요?
            - 컴퓨터 비전의 기본 원리는 무엇인가요?
            """)
        
        # 개념 입력 텍스트 영역
        concept = st.text_area(
            "이해하고 싶은 AI 개념을 입력하세요", 
            height=150,
            placeholder="예: 머신러닝이 무엇인지 알고 싶어요",
            help="구체적으로 궁금한 AI 개념이나 질문을 입력해주세요"
        )
        
        # 분석 시작 버튼
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 학습 가이드 생성", type="primary", use_container_width=True):
                if concept.strip():
                    # 전문가 팀 사용
                    education_team = st.session_state.current_team
                    
                    # 입력 데이터 구성
                    input_data = {"concept": concept.strip()}
                    
                    # 결과 처리
                    result = education_team.get_ai_education("AI 개념 이해", input_data)
                    
                    # 워크플로우 로그 저장
                    st.session_state.workflow_logs.extend(education_team.workflow_logs)
                    
                    # 결과 표시
                    st.markdown("### 📊 전문가 팀 학습 가이드")
                    st.markdown(f"""<div class="final-guidance">{result}</div>""", unsafe_allow_html=True)
                    
                    # 워크플로우 로그 (개발자 모드)
                    with st.expander("🔍 워크플로우 로그 보기 (개발자 모드)"):
                        st.json(education_team.workflow_logs[-1])
                else:
                    st.warning("AI 개념을 입력해주세요.")
                
    elif service == "AI 도구 사용법":
        st.subheader("🛠️ AI 도구 사용법")
        
        # 예시 제공
        with st.expander("💡 예시 보기"):
            st.markdown("""
            **추천 입력 예시:**
            - **도구 이름**: ChatGPT, Claude, Midjourney, Stable Diffusion
            - **사용 목적**: 콘텐츠 작성, 이미지 생성, 코드 작성, 데이터 분석
            """)
        
        # 두 개의 컬럼으로 화면 분할
        col1, col2 = st.columns(2)
        
        with col1:
            tool_name = st.text_area(
                "학습하려는 AI 도구 이름을 입력하세요", 
                height=100,
                placeholder="예: ChatGPT",
                help="구체적인 AI 도구 이름을 입력해주세요"
            )
        with col2:
            purpose = st.text_area(
                "사용 목적을 입력하세요", 
                height=100,
                placeholder="예: 콘텐츠 작성",
                help="해당 도구를 어떤 목적으로 사용하고 싶은지 입력해주세요"
            )
        
        # 분석 시작 버튼
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 학습 가이드 생성", type="primary", use_container_width=True):
                if tool_name.strip() and purpose.strip():
                    # 전문가 팀 사용
                    education_team = st.session_state.current_team
                    
                    # 입력 데이터 구성
                    input_data = {"tool_name": tool_name.strip(), "purpose": purpose.strip()}
                    
                    # 결과 처리
                    result = education_team.get_ai_education("AI 도구 사용법", input_data)
                    
                    # 워크플로우 로그 저장
                    st.session_state.workflow_logs.extend(education_team.workflow_logs)
                    
                    # 결과 표시
                    st.markdown("### 📊 전문가 팀 학습 가이드")
                    st.markdown(f"""<div class="final-guidance">{result}</div>""", unsafe_allow_html=True)
                    
                    # 워크플로우 로그 (개발자 모드)
                    with st.expander("🔍 워크플로우 로그 보기 (개발자 모드)"):
                        st.json(education_team.workflow_logs[-1])
                else:
                    st.warning("도구 이름과 사용 목적을 모두 입력해주세요.")
                
    elif service == "AI 학습 계획":
        st.subheader("📈 AI 학습 계획")
        
        # 예시 제공
        with st.expander("💡 예시 보기"):
            st.markdown("""
            **현재 수준 예시:**
            - AI 초보자입니다. 프로그래밍 경험은 있지만 AI는 처음입니다.
            - 머신러닝 기초는 알고 있지만 딥러닝은 모릅니다.
            - 데이터 사이언스 경험이 있지만 AI 모델 구축은 처음입니다.
            
            **학습 목표 예시:**
            - 6개월 내에 AI 엔지니어로 취업하고 싶습니다.
            - 현재 업무에 AI를 적용할 수 있는 수준이 되고 싶습니다.
            - AI 연구자로 전환하고 싶습니다.
            """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            current_level = st.text_area(
                "현재 AI 지식 수준을 입력하세요", 
                height=150,
                placeholder="예: AI 초보자입니다. 프로그래밍 경험은 있지만 AI는 처음입니다.",
                help="현재 AI에 대한 지식 수준을 구체적으로 설명해주세요"
            )
        with col2:
            goals = st.text_area(
                "학습 목표를 입력하세요", 
                height=150,
                placeholder="예: 6개월 내에 AI 엔지니어로 취업하고 싶습니다.",
                help="구체적인 학습 목표와 기간을 입력해주세요"
            )
        
        # 분석 시작 버튼
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 학습 계획 생성", type="primary", use_container_width=True):
                if current_level.strip() and goals.strip():
                    # 전문가 팀 사용
                    education_team = st.session_state.current_team
                    
                    # 입력 데이터 구성
                    input_data = {"current_level": current_level.strip(), "goals": goals.strip()}
                    
                    # 결과 처리
                    result = education_team.get_ai_education("AI 학습 계획", input_data)
                    
                    # 워크플로우 로그 저장
                    st.session_state.workflow_logs.extend(education_team.workflow_logs)
                    
                    # 결과 표시
                    st.markdown("### 📊 전문가 팀 학습 가이드")
                    st.markdown(f"""<div class="final-guidance">{result}</div>""", unsafe_allow_html=True)
                    
                    # 워크플로우 로그 (개발자 모드)
                    with st.expander("🔍 워크플로우 로그 보기 (개발자 모드)"):
                        st.json(education_team.workflow_logs[-1])
                else:
                    st.warning("현재 지식 수준과 학습 목표를 모두 입력해주세요.")
    
    elif service == "CS 학생 스펙 가이드":
        st.subheader("CS 학생 스펙 가이드")
        
        # 예시 제공
        with st.expander("예시 보기"):
            st.markdown("""
            **현재 상황 예시:**
            - 2학년 CS 전공, Python 기초만 알고 있음
            - 3학년 CS 전공, 웹 개발 경험 있음, 취업 준비 중
            - 4학년 CS 전공, AI/ML 관심 있음, 대기업 목표
            
            **목표 예시:**
            - 3학년까지 웹 개발 전문가가 되고 싶음
            - 졸업 후 구글, 마이크로소프트 같은 빅테크 입사
            - AI/ML 엔지니어로 취업하고 싶음
            - 스타트업에서 풀스택 개발자로 일하고 싶음
            """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            current_situation = st.text_area(
                "현재 상황을 입력하세요", 
                height=150,
                placeholder="예: 2학년 CS 전공, Python 기초만 알고 있음",
                help="현재 학년, 전공, 보유 기술, 경험 등을 구체적으로 입력해주세요"
            )
        with col2:
            career_goals = st.text_area(
                "목표를 입력하세요", 
                height=150,
                placeholder="예: 3학년까지 웹 개발 전문가가 되고 싶음",
                help="구체적인 취업 목표나 기술 목표를 입력해주세요"
            )
        
        # 분석 시작 버튼
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("스펙 가이드 생성", type="primary", use_container_width=True):
                if current_situation.strip() and career_goals.strip():
                    # 전문가 팀 사용
                    education_team = st.session_state.current_team
                    
                    # 입력 데이터 구성
                    input_data = {"current_situation": current_situation.strip(), "career_goals": career_goals.strip()}
                    
                    # 결과 처리
                    result = education_team.get_ai_education("CS 학생 스펙 가이드", input_data)
                    
                    # 워크플로우 로그 저장
                    st.session_state.workflow_logs.extend(education_team.workflow_logs)
                    
                    # 결과 표시
                    st.markdown("### 전문가 팀 스펙 가이드")
                    st.markdown(f"""<div class="final-guidance">{result}</div>""", unsafe_allow_html=True)
                    
                    # 워크플로우 로그 (개발자 모드)
                    with st.expander("워크플로우 로그 보기 (개발자 모드)"):
                        st.json(education_team.workflow_logs[-1])
                else:
                    st.warning("현재 상황과 목표를 모두 입력해주세요.")
    
    elif service == "AI 윤리 및 안전":
        st.subheader("🛡️ AI 윤리 및 안전")
        
        # 예시 제공
        with st.expander("💡 예시 보기"):
            st.markdown("""
            **추천 입력 예시:**
            - AI 편향성과 공정성에 대해 알고 싶습니다.
            - AI의 투명성과 설명 가능성에 관심이 있습니다.
            - AI 개발 시 고려해야 할 윤리적 원칙들을 배우고 싶습니다.
            - AI 안전성과 위험 관리에 대해 알고 싶습니다.
            - AI 규제와 정책에 대해 학습하고 싶습니다.
            """)
        
        area_of_interest = st.text_area(
            "관심 있는 AI 윤리/안전 영역을 입력하세요", 
            height=150,
            placeholder="예: AI 편향성과 공정성에 대해 알고 싶습니다.",
            help="구체적으로 관심 있는 AI 윤리나 안전 관련 주제를 입력해주세요"
        )
        
        # 분석 시작 버튼
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 학습 가이드 생성", type="primary", use_container_width=True):
                if area_of_interest.strip():
                    # 전문가 팀 사용
                    education_team = st.session_state.current_team
                    
                    # 입력 데이터 구성
                    input_data = {"area_of_interest": area_of_interest.strip()}
                    
                    # 결과 처리
                    result = education_team.get_ai_education("AI 윤리 및 안전", input_data)
                    
                    # 워크플로우 로그 저장
                    st.session_state.workflow_logs.extend(education_team.workflow_logs)
                    
                    # 결과 표시
                    st.markdown("### 📊 전문가 팀 학습 가이드")
                    st.markdown(f"""<div class="final-guidance">{result}</div>""", unsafe_allow_html=True)
                    
                    # 워크플로우 로그 (개발자 모드)
                    with st.expander("🔍 워크플로우 로그 보기 (개발자 모드)"):
                        st.json(education_team.workflow_logs[-1])
                else:
                    st.warning("관심 있는 AI 윤리/안전 영역을 입력해주세요.")

# 스크립트가 직접 실행될 때만 main() 함수 실행
if __name__ == "__main__":
    main()