#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 리스트 기본 예제
Python 3.14 Basic List Examples

이 예제는 파이썬 리스트의 기본적인 사용법을 다룹니다.
This example covers basic usage of Python lists.
"""

def main():
    print("=== 파이썬 리스트 기본 예제 ===")
    print("=== Python Basic List Examples ===\n")

    # 1. 리스트 생성 방법들
    print("1. 리스트 생성 방법들 (Different ways to create lists)")

    # 빈 리스트 생성
    empty_list = []  # 빈 리스트 생성
    empty_list2 = list()  # list() 함수로 빈 리스트 생성

    # 숫자 리스트
    numbers = [1, 2, 3, 4, 5]  # 정수 리스트
    decimals = [1.5, 2.7, 3.14, 4.0]  # 실수 리스트

    # 문자열 리스트
    fruits = ["사과", "바나나", "오렌지", "포도"]  # 한글 문자열 리스트
    colors = ["red", "green", "blue", "yellow"]  # 영문 문자열 리스트

    # 혼합 타입 리스트
    mixed_list = ["문자열", 123, True, 3.14, [1, 2, 3]]  # 다양한 타입이 섞인 리스트

    print(f"빈 리스트: {empty_list}")
    print(f"숫자 리스트: {numbers}")
    print(f"실수 리스트: {decimals}")
    print(f"과일 리스트: {fruits}")
    print(f"색깔 리스트: {colors}")
    print(f"혼합 리스트: {mixed_list}")
    print()

    # 2. 리스트 인덱싱과 슬라이싱
    print("2. 리스트 인덱싱과 슬라이싱 (List indexing and slicing)")

    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"원본 리스트: {data}")

    # 양수 인덱스 (앞에서부터)
    print(f"첫 번째 요소 (data[0]): {data[0]}")  # 첫 번째 요소
    print(f"두 번째 요소 (data[1]): {data[1]}")  # 두 번째 요소
    print(f"마지막 요소 (data[-1]): {data[-1]}")  # 마지막 요소 (음수 인덱스)
    print(f"뒤에서 두 번째 (data[-2]): {data[-2]}")  # 뒤에서 두 번째 요소

    # 슬라이싱 (범위 선택)
    print(f"처음 3개 요소 (data[0:3]): {data[0:3]}")  # 0번부터 2번까지
    print(f"3번부터 끝까지 (data[3:]): {data[3:]}")  # 3번부터 끝까지
    print(f"처음부터 5번까지 (data[:5]): {data[:5]}")  # 처음부터 4번까지
    print(f"2번부터 7번까지 (data[2:7]): {data[2:7]}")  # 2번부터 6번까지
    print(f"뒤에서 3개 (data[-3:]): {data[-3:]}")  # 뒤에서 3개
    print(f"모든 요소 (data[:]): {data[:]}")  # 모든 요소 (복사본)
    print()

    # 3. 리스트 요소 추가와 삭제
    print("3. 리스트 요소 추가와 삭제 (Adding and removing list elements)")

    # 요소 추가
    shopping_list = ["우유", "빵"]
    print(f"초기 쇼핑 리스트: {shopping_list}")

    shopping_list.append("계란")  # 맨 뒤에 추가
    print(f"append('계란') 후: {shopping_list}")

    shopping_list.insert(1, "치즈")  # 1번 위치에 삽입
    print(f"insert(1, '치즈') 후: {shopping_list}")

    shopping_list.extend(["사과", "바나나"])  # 여러 요소 한번에 추가
    print(f"extend(['사과', '바나나']) 후: {shopping_list}")

    # 요소 삭제
    shopping_list.remove("치즈")  # 특정 값 삭제
    print(f"remove('치즈') 후: {shopping_list}")

    popped_item = shopping_list.pop()  # 마지막 요소 삭제하고 반환
    print(f"pop() 후: {shopping_list}, 삭제된 요소: {popped_item}")

    popped_item = shopping_list.pop(0)  # 0번 위치 요소 삭제하고 반환
    print(f"pop(0) 후: {shopping_list}, 삭제된 요소: {popped_item}")

    del shopping_list[1]  # del 키워드로 특정 인덱스 삭제
    print(f"del shopping_list[1] 후: {shopping_list}")
    print()

    # 4. 리스트 검색과 정렬
    print("4. 리스트 검색과 정렬 (List searching and sorting)")

    scores = [85, 92, 78, 96, 88, 85, 90]
    print(f"점수 리스트: {scores}")

    # 요소 검색
    print(f"85가 몇 개 있는가? {scores.count(85)}")  # 특정 값의 개수
    print(f"92의 인덱스는? {scores.index(92)}")  # 특정 값의 첫 번째 인덱스
    print(f"90이 리스트에 있는가? {90 in scores}")  # 멤버십 테스트
    print(f"95가 리스트에 있는가? {95 in scores}")  # 멤버십 테스트

    # 정렬
    scores_copy = scores.copy()  # 원본 보호를 위해 복사
    scores_copy.sort()  # 오름차순 정렬 (원본 변경)
    print(f"오름차순 정렬: {scores_copy}")

    scores_copy.sort(reverse=True)  # 내림차순 정렬
    print(f"내림차순 정렬: {scores_copy}")

    # sorted() 함수 사용 (원본 변경하지 않음)
    sorted_scores = sorted(scores)  # 오름차순 정렬된 새 리스트
    print(f"원본: {scores}")
    print(f"sorted() 결과: {sorted_scores}")
    print()

    # 5. 리스트 복사와 비교
    print("5. 리스트 복사와 비교 (List copying and comparison)")

    original = [1, 2, 3, [4, 5]]
    print(f"원본 리스트: {original}")

    # 얕은 복사 (shallow copy)
    shallow_copy = original.copy()  # 또는 original[:]
    print(f"얕은 복사: {shallow_copy}")

    # 깊은 복사 (deep copy)
    import copy
    deep_copy = copy.deepcopy(original)
    print(f"깊은 복사: {deep_copy}")

    # 복사본 수정해보기
    shallow_copy[0] = 999  # 첫 번째 요소 변경
    shallow_copy[3][0] = 999  # 중첩된 리스트의 첫 번째 요소 변경

    print(f"얕은 복사 수정 후 원본: {original}")  # 중첩된 부분이 변경됨
    print(f"얕은 복사 수정 후 복사본: {shallow_copy}")

    deep_copy[0] = 888
    deep_copy[3][0] = 888

    print(f"깊은 복사 수정 후 원본: {original}")  # 원본은 변경되지 않음
    print(f"깊은 복사 수정 후 복사본: {deep_copy}")
    print()

    # 6. 리스트 컴프리헨션 (List Comprehension)
    print("6. 리스트 컴프리헨션 (List Comprehension)")

    # 기본 리스트 컴프리헨션
    squares = [x**2 for x in range(1, 6)]  # 1부터 5까지의 제곱
    print(f"제곱수 리스트: {squares}")

    # 조건이 있는 리스트 컴프리헨션
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # 짝수의 제곱
    print(f"짝수 제곱수 리스트: {even_squares}")

    # 문자열 리스트 컴프리헨션
    words = ["hello", "world", "python", "programming"]
    upper_words = [word.upper() for word in words]  # 대문자로 변환
    print(f"대문자 변환: {upper_words}")

    # 길이가 5 이상인 단어만 필터링
    long_words = [word for word in words if len(word) >= 5]
    print(f"5글자 이상 단어: {long_words}")

    # 중첩된 리스트 컴프리헨션
    matrix = [[i + j for j in range(3)] for i in range(3)]
    print(f"3x3 행렬: {matrix}")
    print()

    # 7. 리스트 유틸리티 함수들
    print("7. 리스트 유틸리티 함수들 (List utility functions)")

    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"숫자 리스트: {numbers}")

    print(f"리스트 길이: {len(numbers)}")  # 길이
    print(f"최댓값: {max(numbers)}")  # 최댓값
    print(f"최솟값: {min(numbers)}")  # 최솟값
    print(f"합계: {sum(numbers)}")  # 합계
    print(f"평균: {sum(numbers) / len(numbers):.2f}")  # 평균

    # 리스트 뒤집기
    reversed_numbers = list(reversed(numbers))  # reversed() 함수 사용
    print(f"뒤집힌 리스트: {reversed_numbers}")

    numbers.reverse()  # 원본 리스트 뒤집기
    print(f"원본 뒤집기 후: {numbers}")

    # 리스트 연결
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2  # + 연산자로 연결
    print(f"리스트 연결 (+): {combined}")

    # 리스트 반복
    repeated = list1 * 3  # * 연산자로 반복
    print(f"리스트 반복 (*3): {repeated}")

if __name__ == "__main__":
    main()
