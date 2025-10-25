#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 제어문 조합 및 고급 예제
Python 3.14 Control Statements Combination and Advanced Examples

이 예제는 파이썬의 제어문을 조합한 고급 예제들을 다룹니다.
This example covers advanced examples combining control statements in Python.
"""

def main():
    print("=== 파이썬 제어문 조합 및 고급 예제 ===")
    print("=== Python Control Statements Combination and Advanced Examples ===\n")
    
    # 1. 복합 조건과 반복문
    print("1. 복합 조건과 반복문 (Complex conditions with loops)")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = []
    
    for num in numbers:
        if num % 2 == 0:  # 짝수인 경우
            square = num ** 2
            even_squares.append(square)
            print(f"{num}의 제곱: {square}")
    
    print(f"짝수의 제곱들: {even_squares}")
    print()
    
    # 2. 중첩된 제어문으로 패턴 만들기
    print("2. 중첩된 제어문으로 패턴 만들기 (Creating patterns with nested control statements)")
    
    print("삼각형 패턴:")
    rows = 5
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()
    
    print("\n역삼각형 패턴:")
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
    
    print("\n숫자 피라미드:")
    for i in range(1, rows + 1):
        # 공백 출력
        for j in range(rows - i):
            print(" ", end="")
        # 숫자 출력
        for j in range(1, i + 1):
            print(j, end="")
        print()
    
    print()
    
    # 3. 데이터 검색 및 필터링
    print("3. 데이터 검색 및 필터링 (Data search and filtering)")
    
    students = [
        {"name": "김철수", "age": 20, "grade": "A", "major": "컴퓨터공학"},
        {"name": "이영희", "age": 19, "grade": "B", "major": "수학"},
        {"name": "박민수", "age": 21, "grade": "A", "major": "컴퓨터공학"},
        {"name": "최지영", "age": 20, "grade": "C", "major": "영어"},
        {"name": "정현우", "age": 22, "grade": "B", "major": "컴퓨터공학"}
    ]
    
    print("전체 학생 목록:")
    for student in students:
        print(f"  {student['name']} - {student['age']}세, {student['grade']}등급, {student['major']}")
    
    print("\n컴퓨터공학 전공 학생들:")
    cs_students = []
    for student in students:
        if student["major"] == "컴퓨터공학":
            cs_students.append(student["name"])
            print(f"  {student['name']} - {student['age']}세, {student['grade']}등급")
    
    print(f"\n컴퓨터공학 전공 학생 수: {len(cs_students)}")
    
    print("\nA등급 학생들:")
    a_grade_students = []
    for student in students:
        if student["grade"] == "A":
            a_grade_students.append(student["name"])
            print(f"  {student['name']} - {student['age']}세, {student['major']}")
    
    print()
    
    # 4. 게임 로직 시뮬레이션
    print("4. 게임 로직 시뮬레이션 (Game logic simulation)")
    
    def number_guessing_game():
        """숫자 맞추기 게임 시뮬레이션"""
        import random
        
        target_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print(f"숫자 맞추기 게임 (1-100, 최대 {max_attempts}번 시도)")
        
        while attempts < max_attempts:
            attempts += 1
            
            # 시뮬레이션을 위한 추측값 생성
            if attempts == 1:
                guess = 50
            elif attempts == 2:
                guess = 25 if target_number < 50 else 75
            elif attempts == 3:
                guess = 12 if target_number < 25 else 37 if target_number < 50 else 62 if target_number < 75 else 87
            else:
                guess = random.randint(1, 100)
            
            print(f"시도 {attempts}: {guess}")
            
            if guess == target_number:
                print(f"정답입니다! {attempts}번 만에 맞췄습니다.")
                break
            elif guess < target_number:
                print("더 큰 수입니다.")
            else:
                print("더 작은 수입니다.")
            
            if attempts == max_attempts:
                print(f"게임 종료! 정답은 {target_number}였습니다.")
    
    number_guessing_game()
    print()
    
    # 5. 파일 처리 시뮬레이션
    print("5. 파일 처리 시뮬레이션 (File processing simulation)")
    
    def process_text_data():
        """텍스트 데이터 처리 시뮬레이션"""
        # 시뮬레이션용 텍스트 데이터
        lines = [
            "안녕하세요, 파이썬 프로그래밍입니다.",
            "오늘은 좋은 날씨입니다.",
            "파이썬은 매우 유용한 언어입니다.",
            "프로그래밍을 배우는 것은 재미있습니다.",
            "코딩은 창의적인 활동입니다."
        ]
        
        print("원본 텍스트:")
        for i, line in enumerate(lines, 1):
            print(f"  {i}. {line}")
        
        print("\n처리된 텍스트:")
        processed_lines = []
        
        for line in lines:
            # 특정 조건에 따른 처리
            if "파이썬" in line:
                processed_line = f"[PYTHON] {line}"
            elif "프로그래밍" in line:
                processed_line = f"[CODE] {line}"
            else:
                processed_line = f"[INFO] {line}"
            
            processed_lines.append(processed_line)
            print(f"  {processed_line}")
        
        # 통계 계산
        python_lines = sum(1 for line in processed_lines if "[PYTHON]" in line)
        code_lines = sum(1 for line in processed_lines if "[CODE]" in line)
        info_lines = sum(1 for line in processed_lines if "[INFO]" in line)
        
        print(f"\n통계:")
        print(f"  파이썬 관련: {python_lines}줄")
        print(f"  프로그래밍 관련: {code_lines}줄")
        print(f"  일반 정보: {info_lines}줄")
    
    process_text_data()
    print()
    
    # 6. 메뉴 시스템 시뮬레이션
    print("6. 메뉴 시스템 시뮬레이션 (Menu system simulation)")
    
    def menu_system():
        """메뉴 시스템 시뮬레이션"""
        balance = 1000  # 초기 잔액
        
        # 시뮬레이션용 메뉴 선택
        menu_choices = [1, 2, 3, 4, 5]  # 5번은 종료
        
        print("은행 시스템 메뉴:")
        print("1. 잔액 조회")
        print("2. 입금")
        print("3. 출금")
        print("4. 이체")
        print("5. 종료")
        
        for choice in menu_choices:
            print(f"\n선택: {choice}")
            
            if choice == 1:
                print(f"현재 잔액: {balance:,}원")
            
            elif choice == 2:
                amount = 50000  # 시뮬레이션용 입금액
                balance += amount
                print(f"{amount:,}원을 입금했습니다.")
                print(f"현재 잔액: {balance:,}원")
            
            elif choice == 3:
                amount = 30000  # 시뮬레이션용 출금액
                if balance >= amount:
                    balance -= amount
                    print(f"{amount:,}원을 출금했습니다.")
                    print(f"현재 잔액: {balance:,}원")
                else:
                    print("잔액이 부족합니다.")
            
            elif choice == 4:
                amount = 20000  # 시뮬레이션용 이체액
                if balance >= amount:
                    balance -= amount
                    print(f"{amount:,}원을 이체했습니다.")
                    print(f"현재 잔액: {balance:,}원")
                else:
                    print("잔액이 부족합니다.")
            
            elif choice == 5:
                print("시스템을 종료합니다.")
                break
            
            else:
                print("잘못된 선택입니다.")
    
    menu_system()

if __name__ == "__main__":
    main()

