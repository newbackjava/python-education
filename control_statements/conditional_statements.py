#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 조건문 예제
Python 3.14 Conditional Statements Example

이 예제는 파이썬의 조건문(if, elif, else)을 다룹니다.
This example covers conditional statements (if, elif, else) in Python.
"""

def main():
    print("=== 파이썬 조건문 예제 ===")
    print("=== Python Conditional Statements Example ===\n")
    
    # 1. 기본 if문
    print("1. 기본 if문 (Basic if statement)")
    age = 20
    
    if age >= 18:
        print(f"나이 {age}세는 성인입니다.")
    
    print()
    
    # 2. if-else문
    print("2. if-else문 (if-else statement)")
    score = 75
    
    if score >= 60:
        print(f"점수 {score}점으로 합격입니다!")
    else:
        print(f"점수 {score}점으로 불합격입니다.")
    
    print()
    
    # 3. if-elif-else문
    print("3. if-elif-else문 (if-elif-else statement)")
    temperature = 25
    
    if temperature > 30:
        print(f"온도 {temperature}°C는 매우 더운 날씨입니다.")
    elif temperature > 20:
        print(f"온도 {temperature}°C는 따뜻한 날씨입니다.")
    elif temperature > 10:
        print(f"온도 {temperature}°C는 시원한 날씨입니다.")
    else:
        print(f"온도 {temperature}°C는 추운 날씨입니다.")
    
    print()
    
    # 4. 중첩된 조건문
    print("4. 중첩된 조건문 (Nested conditional statements)")
    age = 25
    has_license = True
    
    if age >= 18:
        print("성인입니다.")
        if has_license:
            print("면허가 있어서 운전할 수 있습니다.")
        else:
            print("면허가 없어서 운전할 수 없습니다.")
    else:
        print("미성년자입니다.")
    
    print()
    
    # 5. 복합 조건문
    print("5. 복합 조건문 (Complex conditional statements)")
    username = "admin"
    password = "12345"
    is_active = True
    
    if username == "admin" and password == "12345" and is_active:
        print("관리자 로그인 성공!")
    elif username == "admin" and password == "12345" and not is_active:
        print("계정이 비활성화되어 있습니다.")
    elif username == "admin":
        print("비밀번호가 틀렸습니다.")
    else:
        print("사용자명이 틀렸습니다.")
    
    print()
    
    # 6. 삼항 연산자 (조건부 표현식)
    print("6. 삼항 연산자 (Ternary operator)")
    number = 7
    
    result = "짝수" if number % 2 == 0 else "홀수"
    print(f"숫자 {number}는 {result}입니다.")
    
    # 중첩된 삼항 연산자
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    print(f"점수 {score}점의 등급은 {grade}입니다.")
    
    print()
    
    # 7. 멤버십 테스트와 조건문
    print("7. 멤버십 테스트와 조건문 (Membership test with conditionals)")
    fruits = ["사과", "바나나", "오렌지", "포도"]
    user_fruit = "사과"
    
    if user_fruit in fruits:
        print(f"{user_fruit}는 과일 목록에 있습니다.")
    else:
        print(f"{user_fruit}는 과일 목록에 없습니다.")
    
    print()
    
    # 8. 문자열 조건문
    print("8. 문자열 조건문 (String conditionals)")
    text = "Hello, World!"
    
    if text.startswith("Hello"):
        print("문자열이 'Hello'로 시작합니다.")
    
    if text.endswith("!"):
        print("문자열이 '!'로 끝납니다.")
    
    if len(text) > 10:
        print("문자열 길이가 10보다 깁니다.")
    
    print()
    
    # 9. 실용적인 예제: 성적 계산기
    print("9. 실용적인 예제: 성적 계산기 (Practical example: Grade calculator)")
    
    def calculate_grade(korean, english, math):
        """성적을 계산하고 등급을 반환하는 함수"""
        total = korean + english + math
        average = total / 3
        
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
        
        return total, average, grade
    
    # 성적 입력
    korean_score = 85
    english_score = 92
    math_score = 78
    
    total, average, grade = calculate_grade(korean_score, english_score, math_score)
    
    print(f"국어: {korean_score}점")
    print(f"영어: {english_score}점")
    print(f"수학: {math_score}점")
    print(f"총점: {total}점")
    print(f"평균: {average:.1f}점")
    print(f"등급: {grade}")

if __name__ == "__main__":
    main()

