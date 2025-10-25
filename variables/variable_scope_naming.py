#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 변수 스코프와 네이밍 예제
Python 3.14 Variable Scope and Naming Example

이 예제는 파이썬의 변수 스코프와 네이밍 규칙을 다룹니다.
This example covers variable scope and naming conventions in Python.
"""

# 전역 변수 (Global Variable)
GLOBAL_CONSTANT = "전역 상수"
global_counter = 0

def demonstrate_scope():
    """변수 스코프를 보여주는 함수"""
    print("=== 변수 스코프 예제 ===")
    print("=== Variable Scope Example ===\n")
    
    # 지역 변수 (Local Variable)
    local_variable = "지역 변수"
    print(f"지역 변수: {local_variable}")
    
    # 전역 변수 접근
    global global_counter
    global_counter += 1
    print(f"전역 카운터: {global_counter}")
    print(f"전역 상수: {GLOBAL_CONSTANT}")
    print()

def demonstrate_naming():
    """변수 네이밍 규칙을 보여주는 함수"""
    print("=== 변수 네이밍 규칙 예제 ===")
    print("=== Variable Naming Convention Example ===\n")
    
    # 올바른 변수명 (Good Variable Names)
    user_name = "김철수"           # snake_case (권장)
    userAge = 25                  # camelCase (가능하지만 권장하지 않음)
    MAX_SIZE = 100                # 상수는 대문자와 언더스코어
    
    # 숫자로 시작할 수 없음 (에러 발생)
    # 1st_name = "잘못된 변수명"   # SyntaxError
    
    # 예약어 사용 불가 (에러 발생)
    # class = "잘못된 변수명"      # SyntaxError
    
    print(f"사용자 이름: {user_name}")
    print(f"사용자 나이: {userAge}")
    print(f"최대 크기: {MAX_SIZE}")
    print()
    
    # 변수 타입 확인
    print("=== 변수 타입 확인 ===")
    print("=== Variable Type Checking ===")
    
    number = 42
    text = "Hello"
    is_valid = True
    
    print(f"number = {number}, 타입: {type(number)}")
    print(f"text = {text}, 타입: {type(text)}")
    print(f"is_valid = {is_valid}, 타입: {type(is_valid)}")
    
    # 타입 변환
    print("\n=== 타입 변환 ===")
    print("=== Type Conversion ===")
    
    str_number = str(number)      # 정수를 문자열로
    int_text = int("123")         # 문자열을 정수로
    float_text = float("3.14")    # 문자열을 실수로
    
    print(f"정수를 문자열로: {str_number} (타입: {type(str_number)})")
    print(f"문자열을 정수로: {int_text} (타입: {type(int_text)})")
    print(f"문자열을 실수로: {float_text} (타입: {type(float_text)})")

def main():
    demonstrate_scope()
    demonstrate_naming()

if __name__ == "__main__":
    main()

