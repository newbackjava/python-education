#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 비트 연산자 및 기타 연산자 예제
Python 3.14 Bitwise and Other Operators Example

이 예제는 파이썬의 비트 연산자와 기타 연산자들을 다룹니다.
This example covers bitwise and other operators in Python.
"""

def main():
    print("=== 파이썬 비트 연산자 및 기타 연산자 예제 ===")
    print("=== Python Bitwise and Other Operators Example ===\n")
    
    # 기본 변수 설정
    a = 12  # 이진수: 1100
    b = 10  # 이진수: 1010
    
    print(f"a = {a} (이진수: {bin(a)})")
    print(f"b = {b} (이진수: {bin(b)})")
    print()
    
    # 1. 비트 연산자 (Bitwise Operators)
    print("1. 비트 연산자 (Bitwise Operators)")
    
    # AND 연산
    result_and = a & b
    print(f"AND (&): {a} & {b} = {result_and} (이진수: {bin(result_and)})")
    
    # OR 연산
    result_or = a | b
    print(f"OR (|): {a} | {b} = {result_or} (이진수: {bin(result_or)})")
    
    # XOR 연산
    result_xor = a ^ b
    print(f"XOR (^): {a} ^ {b} = {result_xor} (이진수: {bin(result_xor)})")
    
    # NOT 연산
    result_not_a = ~a
    print(f"NOT (~): ~{a} = {result_not_a} (이진수: {bin(result_not_a & 0xFF)})")
    
    # 왼쪽 시프트
    result_left = a << 2
    print(f"왼쪽 시프트 (<<): {a} << 2 = {result_left} (이진수: {bin(result_left)})")
    
    # 오른쪽 시프트
    result_right = a >> 2
    print(f"오른쪽 시프트 (>>): {a} >> 2 = {result_right} (이진수: {bin(result_right)})")
    print()
    
    # 2. 삼항 연산자 (Ternary Operator)
    print("2. 삼항 연산자 (Ternary Operator)")
    
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    
    print(f"점수: {score}")
    print(f"등급: {grade}")
    print()
    
    # 더 복잡한 삼항 연산자 예제
    age = 20
    status = "성인" if age >= 18 else "미성년자"
    discount = 0.1 if age >= 65 else 0.05 if age >= 60 else 0
    
    print(f"나이: {age}")
    print(f"상태: {status}")
    print(f"할인율: {discount * 100}%")
    print()
    
    # 3. 할당 연산자와 walrus 연산자 (Python 3.8+)
    print("3. 할당 연산자와 walrus 연산자 (Assignment and Walrus Operators)")
    
    # 일반적인 할당
    numbers = [1, 2, 3, 4, 5]
    total = 0
    
    for num in numbers:
        total += num
    
    print(f"숫자 리스트: {numbers}")
    print(f"합계: {total}")
    print()
    
    # Walrus 연산자 (:=) 예제
    print("Walrus 연산자 (:=) 예제:")
    text = "Hello, World! This is a test."
    
    # while 루프에서 walrus 연산자 사용
    words = []
    while (word := input("단어를 입력하세요 (종료: quit): ")) != "quit":
        words.append(word)
    
    print(f"입력된 단어들: {words}")
    print()
    
    # 4. 연산자 우선순위 예제
    print("4. 연산자 우선순위 예제 (Operator Precedence)")
    
    result1 = 2 + 3 * 4
    result2 = (2 + 3) * 4
    result3 = 2 ** 3 * 4
    result4 = 2 ** (3 * 4)
    
    print(f"2 + 3 * 4 = {result1} (곱셈이 먼저)")
    print(f"(2 + 3) * 4 = {result2} (괄호가 먼저)")
    print(f"2 ** 3 * 4 = {result3} (거듭제곱이 먼저)")
    print(f"2 ** (3 * 4) = {result4} (괄호가 먼저)")
    print()
    
    # 5. 조건부 표현식과 연산자 조합
    print("5. 조건부 표현식과 연산자 조합")
    
    x, y, z = 10, 20, 30
    
    # 복합 조건
    condition1 = x > 5 and y < 25 or z == 30
    condition2 = (x > 5 and y < 25) or z == 30
    condition3 = x > 5 and (y < 25 or z == 30)
    
    print(f"x = {x}, y = {y}, z = {z}")
    print(f"x > 5 and y < 25 or z == 30 = {condition1}")
    print(f"(x > 5 and y < 25) or z == 30 = {condition2}")
    print(f"x > 5 and (y < 25 or z == 30) = {condition3}")
    print()
    
    # 6. 연산자 오버로딩 개념 (간단한 예제)
    print("6. 연산자 오버로딩 개념 (Operator Overloading Concept)")
    
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)
        
        def __str__(self):
            return f"Point({self.x}, {self.y})"
    
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = p1 + p2  # __add__ 메서드 호출
    
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p1 + p2 = {p3}")

if __name__ == "__main__":
    main()

