#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 반복문 예제
Python 3.14 Loop Statements Example

이 예제는 파이썬의 반복문(for, while)을 다룹니다.
This example covers loop statements (for, while) in Python.
"""

def main():
    print("=== 파이썬 반복문 예제 ===")
    print("=== Python Loop Statements Example ===\n")
    
    # 1. 기본 for문
    print("1. 기본 for문 (Basic for loop)")
    fruits = ["사과", "바나나", "오렌지", "포도"]
    
    print("과일 목록:")
    for fruit in fruits:
        print(f"  - {fruit}")
    
    print()
    
    # 2. range()를 사용한 for문
    print("2. range()를 사용한 for문 (for loop with range)")
    
    print("1부터 5까지:")
    for i in range(1, 6):
        print(f"  {i}")
    
    print("\n0부터 10까지 (2씩 증가):")
    for i in range(0, 11, 2):
        print(f"  {i}")
    
    print("\n5부터 1까지 (역순):")
    for i in range(5, 0, -1):
        print(f"  {i}")
    
    print()
    
    # 3. enumerate()를 사용한 for문
    print("3. enumerate()를 사용한 for문 (for loop with enumerate)")
    subjects = ["수학", "영어", "과학", "사회"]
    
    print("과목 목록:")
    for index, subject in enumerate(subjects, 1):
        print(f"  {index}. {subject}")
    
    print()
    
    # 4. 딕셔너리 순회
    print("4. 딕셔너리 순회 (Dictionary iteration)")
    student = {
        "이름": "김철수",
        "나이": 20,
        "전공": "컴퓨터공학",
        "학년": 2
    }
    
    print("학생 정보:")
    for key, value in student.items():
        print(f"  {key}: {value}")
    
    print()
    
    # 5. 중첩된 for문
    print("5. 중첩된 for문 (Nested for loops)")
    print("구구단 2단:")
    for i in range(1, 10):
        result = 2 * i
        print(f"  2 × {i} = {result}")
    
    print("\n구구단 전체 (2단~3단):")
    for i in range(2, 4):
        print(f"{i}단:")
        for j in range(1, 10):
            result = i * j
            print(f"  {i} × {j} = {result}")
        print()
    
    # 6. while문
    print("6. while문 (while loop)")
    count = 1
    print("while문으로 1부터 5까지 출력:")
    while count <= 5:
        print(f"  {count}")
        count += 1
    
    print()
    
    # 7. break와 continue
    print("7. break와 continue (break and continue)")
    
    print("break 예제 (5에서 중단):")
    for i in range(1, 11):
        if i == 5:
            break
        print(f"  {i}")
    
    print("\ncontinue 예제 (홀수만 출력):")
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(f"  {i}")
    
    print()
    
    # 8. else절과 반복문
    print("8. else절과 반복문 (else clause with loops)")
    
    print("for문의 else절:")
    for i in range(1, 4):
        print(f"  {i}")
    else:
        print("  반복이 정상적으로 완료되었습니다.")
    
    print("\nbreak가 있는 경우:")
    for i in range(1, 6):
        if i == 3:
            break
        print(f"  {i}")
    else:
        print("  이 메시지는 출력되지 않습니다.")
    
    print()
    
    # 9. 실용적인 예제들
    print("9. 실용적인 예제들 (Practical examples)")
    
    # 예제 1: 숫자 합계 계산
    print("예제 1: 숫자 합계 계산")
    numbers = [1, 2, 3, 4, 5]
    total = 0
    
    for num in numbers:
        total += num
    
    print(f"숫자들: {numbers}")
    print(f"합계: {total}")
    print()
    
    # 예제 2: 최대값 찾기
    print("예제 2: 최대값 찾기")
    scores = [85, 92, 78, 96, 88]
    max_score = scores[0]
    
    for score in scores[1:]:
        if score > max_score:
            max_score = score
    
    print(f"점수들: {scores}")
    print(f"최고 점수: {max_score}")
    print()
    
    # 예제 3: 문자열 처리
    print("예제 3: 문자열 처리")
    text = "Hello, World!"
    vowel_count = 0
    vowels = "aeiouAEIOU"
    
    for char in text:
        if char in vowels:
            vowel_count += 1
    
    print(f"문자열: '{text}'")
    print(f"모음 개수: {vowel_count}")
    print()
    
    # 예제 4: 사용자 입력 처리 (시뮬레이션)
    print("예제 4: 사용자 입력 처리 시뮬레이션")
    
    def simulate_user_input():
        """사용자 입력을 시뮬레이션하는 함수"""
        inputs = ["안녕하세요", "파이썬", "프로그래밍", "quit"]
        index = 0
        
        while index < len(inputs):
            user_input = inputs[index]
            print(f"사용자 입력: {user_input}")
            
            if user_input.lower() == "quit":
                print("프로그램을 종료합니다.")
                break
            
            print(f"처리된 입력: {user_input.upper()}")
            index += 1
    
    simulate_user_input()

if __name__ == "__main__":
    main()

