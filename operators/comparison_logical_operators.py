#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 비교 및 논리 연산자 예제
Python 3.14 Comparison and Logical Operators Example

이 예제는 파이썬의 비교 연산자와 논리 연산자들을 다룹니다.
This example covers comparison and logical operators in Python.
"""

def main():
    print("=== 파이썬 비교 및 논리 연산자 예제 ===")
    print("=== Python Comparison and Logical Operators Example ===\n")
    
    # 기본 변수 설정
    a = 10
    b = 5
    c = 10
    
    print(f"a = {a}, b = {b}, c = {c}")
    print()
    
    # 1. 비교 연산자 (Comparison Operators)
    print("1. 비교 연산자 (Comparison Operators)")
    print(f"a == b (같다): {a} == {b} = {a == b}")
    print(f"a != b (다르다): {a} != {b} = {a != b}")
    print(f"a > b (크다): {a} > {b} = {a > b}")
    print(f"a < b (작다): {a} < {b} = {a < b}")
    print(f"a >= c (크거나 같다): {a} >= {c} = {a >= c}")
    print(f"a <= b (작거나 같다): {a} <= {b} = {a <= b}")
    print()
    
    # 2. 논리 연산자 (Logical Operators)
    print("2. 논리 연산자 (Logical Operators)")
    
    # AND 연산자
    print("AND 연산자 (and)")
    print(f"True and True = {True and True}")
    print(f"True and False = {True and False}")
    print(f"False and True = {False and True}")
    print(f"False and False = {False and False}")
    print(f"a > 5 and b < 10 = {a > 5 and b < 10}")
    print()
    
    # OR 연산자
    print("OR 연산자 (or)")
    print(f"True or True = {True or True}")
    print(f"True or False = {True or False}")
    print(f"False or True = {False or True}")
    print(f"False or False = {False or False}")
    print(f"a < 5 or b > 10 = {a < 5 or b > 10}")
    print()
    
    # NOT 연산자
    print("NOT 연산자 (not)")
    print(f"not True = {not True}")
    print(f"not False = {not False}")
    print(f"not (a > b) = {not (a > b)}")
    print()
    
    # 3. 복합 논리 연산
    print("3. 복합 논리 연산 (Complex Logical Operations)")
    age = 25
    has_license = True
    has_car = False
    
    print(f"나이: {age}")
    print(f"면허 보유: {has_license}")
    print(f"차량 보유: {has_car}")
    print()
    
    can_drive = age >= 18 and has_license
    can_rent_car = age >= 21 and has_license and not has_car
    
    print(f"운전 가능: 나이 >= 18 and 면허 보유 = {can_drive}")
    print(f"렌터카 가능: 나이 >= 21 and 면허 보유 and 차량 미보유 = {can_rent_car}")
    print()
    
    # 4. 문자열 비교
    print("4. 문자열 비교 (String Comparison)")
    name1 = "김철수"
    name2 = "김영희"
    name3 = "김철수"
    
    print(f"name1 = '{name1}', name2 = '{name2}', name3 = '{name3}'")
    print(f"name1 == name2: {name1 == name2}")
    print(f"name1 == name3: {name1 == name3}")
    print(f"name1 != name2: {name1 != name2}")
    print(f"name1 < name2 (사전순): {name1 < name2}")
    print()
    
    # 5. 멤버십 연산자 (Membership Operators)
    print("5. 멤버십 연산자 (Membership Operators)")
    fruits = ["사과", "바나나", "오렌지", "포도"]
    text = "Hello, World!"
    
    print(f"과일 리스트: {fruits}")
    print(f"문자열: '{text}'")
    print()
    
    print(f"'사과' in fruits: {'사과' in fruits}")
    print(f"'딸기' in fruits: {'딸기' in fruits}")
    print(f"'딸기' not in fruits: {'딸기' not in fruits}")
    print(f"'World' in text: {'World' in text}")
    print(f"'Python' in text: {'Python' in text}")
    print()
    
    # 6. 식별 연산자 (Identity Operators)
    print("6. 식별 연산자 (Identity Operators)")
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = x")
    print()
    
    print(f"x == y (값이 같은가): {x == y}")
    print(f"x is y (같은 객체인가): {x is y}")
    print(f"x is z (같은 객체인가): {x is z}")
    print(f"x is not y (다른 객체인가): {x is not y}")

if __name__ == "__main__":
    main()

