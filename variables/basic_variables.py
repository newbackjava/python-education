#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 기본 변수 예제
Python 3.14 Basic Variables Example

이 예제는 파이썬의 기본 변수 타입들을 다룹니다.
This example covers basic variable types in Python.
"""

def main():
    print("=== 파이썬 기본 변수 타입 예제 ===")
    print("=== Python Basic Variable Types Example ===\n")
    
    # 1. 숫자형 변수 (Numeric Variables)
    print("1. 숫자형 변수 (Numeric Variables)")
    age = 25                    # 정수 (Integer)
    height = 175.5             # 실수 (Float)
    temperature = -10.3         # 음수 실수 (Negative Float)
    
    print(f"나이: {age} (타입: {type(age)})")
    print(f"키: {height}cm (타입: {type(height)})")
    print(f"온도: {temperature}°C (타입: {type(temperature)})")
    print()
    
    # 2. 문자열 변수 (String Variables)
    print("2. 문자열 변수 (String Variables)")
    name = "김철수"              # 한글 문자열
    english_name = "John Doe"   # 영문 문자열
    message = '안녕하세요!'      # 작은따옴표 사용
    
    print(f"이름: {name} (타입: {type(name)})")
    print(f"영문명: {english_name} (타입: {type(english_name)})")
    print(f"인사말: {message} (타입: {type(message)})")
    print()
    
    # 3. 불린 변수 (Boolean Variables)
    print("3. 불린 변수 (Boolean Variables)")
    is_student = True           # 참 (True)
    is_working = False          # 거짓 (False)
    
    print(f"학생 여부: {is_student} (타입: {type(is_student)})")
    print(f"직장인 여부: {is_working} (타입: {type(is_working)})")
    print()
    
    # 4. 변수 재할당 (Variable Reassignment)
    print("4. 변수 재할당 (Variable Reassignment)")
    score = 85
    print(f"처음 점수: {score}")
    
    score = 92  # 변수 재할당
    print(f"수정된 점수: {score}")
    print()

if __name__ == "__main__":
    main()

