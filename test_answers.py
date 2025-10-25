#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 테스트 문제 답안
Python 3.14 Test Questions Answers

이 파일은 파이썬 테스트 문제의 답안과 해설을 포함합니다.
This file contains answers and explanations for Python test questions.
"""

def print_answer(level, number, correct_answer, explanation):
    """답안 출력 함수"""
    print(f"\n{'='*60}")
    print(f"[{level}급 문제 {number} 답안]")
    print(f"{'='*60}")
    print(f"정답: {correct_answer}")
    print(f"\n해설:")
    print(f"{explanation}")

def main():
    print("파이썬 3.14 테스트 문제 답안")
    print("Python 3.14 Test Questions Answers")
    print("="*60)
    
    # 하급 문제 답안 (1-10)
    print("\n" + "="*60)
    print("하급 문제 답안 (Basic Level Answers)")
    print("="*60)
    
    print_answer("하", 1, "3. user_name",
        "파이썬 변수명 규칙:\n"
        "- 숫자로 시작할 수 없음 (1st_name ❌)\n"
        "- 예약어 사용 불가 (class ❌)\n"
        "- 숫자로 시작 불가 (2nd_grade ❌)\n"
        "- snake_case 권장 (user_name ✅)")
    
    print_answer("하", 2, "1. 3",
        "// 연산자는 정수 나눗셈(floor division)을 수행합니다.\n"
        "10 // 3 = 3 (나머지는 버림)\n"
        "일반 나눗셈(/)과는 다릅니다: 10 / 3 = 3.333...")
    
    print_answer("하", 3, "2. 1",
        "리스트 인덱스는 0부터 시작합니다:\n"
        "fruits[0] = '사과'\n"
        "fruits[1] = '바나나' ← 정답\n"
        "fruits[2] = '오렌지'")
    
    print_answer("하", 4, "3. true",
        "파이썬의 불린 값은 대소문자를 구분합니다:\n"
        "- True (올바름)\n"
        "- False (올바름)\n"
        "- true (소문자, 잘못됨)\n"
        "- 1 (숫자, 불린이 아님)")
    
    print_answer("하", 5, "1. HelloWorld",
        "문자열 연결 연산자 +는 두 문자열을 붙여줍니다:\n"
        "'Hello' + 'World' = 'HelloWorld'\n"
        "공백이 없이 바로 연결됩니다.")
    
    print_answer("하", 6, "4. person['나이'] 또는 person.get('나이')",
        "딕셔너리에서 값을 가져오는 방법:\n"
        "- person['나이']: 키가 없으면 KeyError 발생\n"
        "- person.get('나이'): 키가 없으면 None 반환\n"
        "- person.나이: 잘못된 문법\n"
        "두 방법 모두 올바른 방법입니다.")
    
    print_answer("하", 7, "2. 5",
        "len() 함수는 리스트의 요소 개수를 반환합니다:\n"
        "numbers = [1, 2, 3, 4, 5]\n"
        "len(numbers) = 5")
    
    print_answer("하", 8, "1. 성인",
        "조건문 실행 과정:\n"
        "age = 20\n"
        "age >= 18 → 20 >= 18 → True\n"
        "if 조건이 True이므로 '성인' 출력")
    
    print_answer("하", 9, "2. 3번",
        "range(3)은 0, 1, 2를 생성합니다:\n"
        "for i in range(3):\n"
        "    print(i)  # 0, 1, 2 출력\n"
        "총 3번 실행됩니다.")
    
    print_answer("하", 10, "2. {1, 2, 3, 4}",
        "집합(set)의 특징:\n"
        "- 중복 요소 자동 제거\n"
        "- 순서 없음\n"
        "{1, 2, 2, 3, 3, 4} → {1, 2, 3, 4}")
    
    # 중급 문제 답안 (11-15)
    print("\n" + "="*60)
    print("중급 문제 답안 (Intermediate Level Answers)")
    print("="*60)
    
    print_answer("중", 11, "1. [1, 4, 9]",
        "리스트 컴프리헨션 실행 과정:\n"
        "range(1, 4) → 1, 2, 3\n"
        "x**2 for x in [1, 2, 3]\n"
        "1**2 = 1, 2**2 = 4, 3**2 = 9\n"
        "결과: [1, 4, 9]")
    
    print_answer("중", 12, "2. [2, 4]",
        "조건부 리스트 컴프리헨션:\n"
        "numbers = [1, 2, 3, 4, 5]\n"
        "x % 2 == 0 조건을 만족하는 요소들:\n"
        "1 % 2 = 1 (False), 2 % 2 = 0 (True)\n"
        "3 % 2 = 1 (False), 4 % 2 = 0 (True)\n"
        "5 % 2 = 1 (False)\n"
        "결과: [2, 4]")
    
    print_answer("중", 13, "2. 안녕하세요, 김철수입니다. 학번은 2023001입니다.",
        "상속과 메서드 오버라이딩:\n"
        "1. Student 클래스가 Person을 상속\n"
        "2. Student.introduce() 메서드가 부모 클래스 메서드를 오버라이딩\n"
        "3. student.introduce() 호출 시 Student 클래스의 introduce() 실행\n"
        "4. 결과: '안녕하세요, 김철수입니다. 학번은 2023001입니다.'")
    
    print_answer("중", 14, "1. 20",
        "함수 실행 과정:\n"
        "data = {'a': 10, 'b': 20, 'c': 30}\n"
        "isinstance(data, dict) → True\n"
        "sum(data.values()) = sum([10, 20, 30]) = 60\n"
        "len(data) = 3\n"
        "60 / 3 = 20")
    
    print_answer("중", 15, "1. 원본: [1, 2, [999, 4]], 얕은 복사: [1, 2, [999, 4]], 깊은 복사: [1, 2, [3, 4]]",
        "얕은 복사 vs 깊은 복사:\n"
        "얕은 복사: 중첩된 객체는 참조만 복사\n"
        "깊은 복사: 모든 객체를 완전히 복사\n"
        "original[2][0] = 999 실행 후:\n"
        "- 원본과 얕은 복사: 중첩 리스트가 공유되어 둘 다 변경\n"
        "- 깊은 복사: 독립적인 복사본이므로 변경되지 않음")
    
    # 상급 문제 답안 (16-20)
    print("\n" + "="*60)
    print("상급 문제 답안 (Advanced Level Answers)")
    print("="*60)
    
    print_answer("상", 16, "2. 이영희, 김철수",
        "학생 성적 계산:\n"
        "김철수: (85+90+88)/3 = 87.67\n"
        "이영희: (92+88+95)/3 = 91.67\n"
        "박민수: (78+85+82)/3 = 81.67\n"
        "평균 순으로 정렬: 이영희(91.67) > 김철수(87.67) > 박민수(81.67)\n"
        "상위 2명: 이영희, 김철수")
    
    print_answer("상", 17, "1. [1]",
        "스택 연산 순서:\n"
        "push(1) → [1]\n"
        "push(2) → [1, 2]\n"
        "push(3) → [1, 2, 3]\n"
        "pop() → 3 제거, [1, 2]\n"
        "push(4) → [1, 2, 4]\n"
        "pop() → 4 제거, [1, 2]\n"
        "pop() → 2 제거, [1]\n"
        "최종 상태: [1]")
    
    print_answer("상", 18, "1. 'l'",
        "문자 빈도 계산:\n"
        "'hello world'에서 공백 제외:\n"
        "h: 1, e: 1, l: 3, o: 2, w: 1, r: 1, d: 1\n"
        "가장 많이 나타나는 문자: 'l' (3번)\n"
        "함수는 가장 빈도가 높은 문자 중 첫 번째를 반환")
    
    print_answer("상", 19, "1. 3",
        "이진 탐색 과정:\n"
        "배열: [1, 3, 5, 7, 9, 11, 13], target: 7\n"
        "1단계: left=0, right=6, mid=3, arr[3]=7 → 찾음!\n"
        "인덱스 3에서 7을 찾았습니다.")
    
    print_answer("상", 20, "1. 파이썬 프로그래밍 도서의 available이 1이 되고, borrowed 리스트에 대출 기록이 추가됨",
        "도서 대출 과정:\n"
        "1. ISBN '978-1234567890' 검색\n"
        "2. 해당 도서의 available = 2 (대출 가능)\n"
        "3. available -= 1 → available = 1\n"
        "4. borrowed 리스트에 대출 기록 추가\n"
        "5. 함수는 True 반환 (대출 성공)")

def print_scoring_guide():
    """채점 기준 출력"""
    print("\n" + "="*60)
    print("채점 기준 (Scoring Guide)")
    print("="*60)
    
    print("\n📊 점수 계산:")
    print("- 하급 문제 (1-10번): 각 3점 = 30점")
    print("- 중급 문제 (11-15번): 각 6점 = 30점") 
    print("- 상급 문제 (16-20번): 각 8점 = 40점")
    print("- 총점: 100점")
    
    print("\n🏆 등급 기준:")
    print("- A등급: 90점 이상 (상급 문제 4개 이상 정답)")
    print("- B등급: 80점 이상 (중급 문제 4개 이상 정답)")
    print("- C등급: 70점 이상 (하급 문제 8개 이상 정답)")
    print("- D등급: 60점 이상 (하급 문제 6개 이상 정답)")
    print("- F등급: 60점 미만")
    
    print("\n💡 학습 권장사항:")
    print("- 하급 문제 틀린 경우: 기본 문법 복습 필요")
    print("- 중급 문제 틀린 경우: 응용 예제 연습 필요")
    print("- 상급 문제 틀린 경우: 알고리즘과 클래스 설계 학습 필요")

if __name__ == "__main__":
    main()
    print_scoring_guide()
