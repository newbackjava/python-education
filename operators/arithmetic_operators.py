#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 산술 연산자 예제
Python 3.14 Arithmetic Operators Example

이 예제는 파이썬의 산술 연산자들을 다룹니다.
This example covers arithmetic operators in Python.
"""

def main():
    print("=== 파이썬 산술 연산자 예제 ===")
    print("=== Python Arithmetic Operators Example ===\n")
    
    # 기본 변수 설정
    a = 10
    b = 3
    
    print(f"a = {a}, b = {b}")
    print()
    
    # 1. 기본 산술 연산
    print("1. 기본 산술 연산 (Basic Arithmetic Operations)")
    print(f"덧셈 (Addition): {a} + {b} = {a + b}")
    print(f"뺄셈 (Subtraction): {a} - {b} = {a - b}")
    print(f"곱셈 (Multiplication): {a} * {b} = {a * b}")
    print(f"나눗셈 (Division): {a} / {b} = {a / b}")
    print(f"나머지 (Modulus): {a} % {b} = {a % b}")
    print(f"거듭제곱 (Exponentiation): {a} ** {b} = {a ** b}")
    print()
    
    # 2. 정수 나눗셈 (Floor Division)
    print("2. 정수 나눗셈 (Floor Division)")
    print(f"정수 나눗셈: {a} // {b} = {a // b}")
    print(f"일반 나눗셈: {a} / {b} = {a / b}")
    print()
    
    # 3. 복합 할당 연산자
    print("3. 복합 할당 연산자 (Compound Assignment Operators)")
    x = 10
    print(f"초기값: x = {x}")
    
    x += 5  # x = x + 5
    print(f"x += 5 후: x = {x}")
    
    x -= 3  # x = x - 3
    print(f"x -= 3 후: x = {x}")
    
    x *= 2  # x = x * 2
    print(f"x *= 2 후: x = {x}")
    
    x //= 3  # x = x // 3
    print(f"x //= 3 후: x = {x}")
    
    x **= 2  # x = x ** 2
    print(f"x **= 2 후: x = {x}")
    print()
    
    # 4. 문자열 연산
    print("4. 문자열 연산 (String Operations)")
    first_name = "김"
    last_name = "철수"
    age = 25
    
    full_name = first_name + last_name
    greeting = "안녕하세요, " + full_name + "님!"
    info = f"{full_name}님은 {age}세입니다."
    
    print(f"이름 합치기: {first_name} + {last_name} = {full_name}")
    print(f"인사말: {greeting}")
    print(f"정보: {info}")
    print(f"이름 반복: {first_name * 3}")
    print()
    
    # 5. 실수 연산의 정밀도
    print("5. 실수 연산의 정밀도 (Floating Point Precision)")
    pi = 3.14159265359
    radius = 5.0
    
    circumference = 2 * pi * radius
    area = pi * radius ** 2
    
    print(f"원주율: {pi}")
    print(f"반지름: {radius}")
    print(f"둘레: 2 * π * r = {circumference}")
    print(f"면적: π * r² = {area}")
    print(f"면적 (소수점 2자리): {area:.2f}")

if __name__ == "__main__":
    main()

