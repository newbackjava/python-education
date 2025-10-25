#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 컬렉션 변수 예제
Python 3.14 Collection Variables Example

이 예제는 파이썬의 컬렉션 타입 변수들을 다룹니다.
This example covers collection type variables in Python.
"""

def main():
    print("=== 파이썬 컬렉션 변수 예제 ===")
    print("=== Python Collection Variables Example ===\n")
    
    # 1. 리스트 (List)
    print("1. 리스트 (List)")
    fruits = ["사과", "바나나", "오렌지", "포도"]
    numbers = [1, 2, 3, 4, 5]
    mixed_list = ["문자열", 123, True, 3.14]
    
    print(f"과일 리스트: {fruits} (타입: {type(fruits)})")
    print(f"숫자 리스트: {numbers} (타입: {type(numbers)})")
    print(f"혼합 리스트: {mixed_list} (타입: {type(mixed_list)})")
    print(f"첫 번째 과일: {fruits[0]}")
    print(f"리스트 길이: {len(fruits)}")
    print()
    
    # 2. 튜플 (Tuple)
    print("2. 튜플 (Tuple)")
    coordinates = (10, 20)
    person_info = ("김철수", 25, "서울")
    single_tuple = (42,)  # 단일 요소 튜플 (쉼표 필요)
    
    print(f"좌표: {coordinates} (타입: {type(coordinates)})")
    print(f"사람 정보: {person_info} (타입: {type(person_info)})")
    print(f"단일 튜플: {single_tuple} (타입: {type(single_tuple)})")
    print(f"X 좌표: {coordinates[0]}")
    print()
    
    # 3. 딕셔너리 (Dictionary)
    print("3. 딕셔너리 (Dictionary)")
    student = {
        "이름": "이영희",
        "나이": 22,
        "전공": "컴퓨터공학",
        "학년": 3
    }
    
    scores = {
        "수학": 95,
        "영어": 88,
        "과학": 92
    }
    
    print(f"학생 정보: {student} (타입: {type(student)})")
    print(f"성적: {scores} (타입: {type(scores)})")
    print(f"학생 이름: {student['이름']}")
    print(f"수학 점수: {scores['수학']}")
    print()
    
    # 4. 집합 (Set)
    print("4. 집합 (Set)")
    unique_numbers = {1, 2, 3, 4, 5, 5, 4}  # 중복 제거됨
    programming_languages = {"Python", "Java", "C++", "JavaScript"}
    
    print(f"고유 숫자: {unique_numbers} (타입: {type(unique_numbers)})")
    print(f"프로그래밍 언어: {programming_languages} (타입: {type(programming_languages)})")
    print(f"Python 포함 여부: {'Python' in programming_languages}")
    print()

if __name__ == "__main__":
    main()

