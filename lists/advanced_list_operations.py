#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 리스트 고급 예제
Python 3.14 Advanced List Examples

이 예제는 파이썬 리스트의 고급 기능들을 다룹니다.
This example covers advanced features of Python lists.
"""

def main():
    print("=== 파이썬 리스트 고급 예제 ===")
    print("=== Python Advanced List Examples ===\n")

    # 1. 중첩된 리스트 (2차원 리스트)
    print("1. 중첩된 리스트 (2차원 리스트) - Nested Lists (2D Lists)")

    # 3x3 행렬 생성
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("3x3 행렬:")
    for i, row in enumerate(matrix):
        print(f"  행 {i}: {row}")

    # 특정 요소 접근
    print(f"matrix[1][2] (2행 3열): {matrix[1][2]}")  # 6
    print(f"matrix[0][0] (1행 1열): {matrix[0][0]}")  # 1

    # 행렬의 대각선 요소들
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"주대각선 요소들: {diagonal}")

    # 행렬 전치 (행과 열 바꾸기)
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("전치 행렬:")
    for i, row in enumerate(transposed):
        print(f"  행 {i}: {row}")
    print()

    # 2. 리스트를 이용한 데이터 구조 시뮬레이션
    print("2. 리스트를 이용한 데이터 구조 시뮬레이션")

    # 학생 성적 관리 시스템
    students = [
        ["김철수", 85, 92, 78],  # [이름, 수학, 영어, 과학]
        ["이영희", 90, 88, 95],
        ["박민수", 78, 85, 92],
        ["최지영", 95, 90, 88]
    ]

    print("학생 성적표:")
    print("이름\t수학\t영어\t과학\t평균")
    print("-" * 40)

    for student in students:
        name = student[0]
        scores = student[1:]  # 점수들만 추출
        average = sum(scores) / len(scores)  # 평균 계산
        print(f"{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t{average:.1f}")

    # 과목별 평균 계산
    math_scores = [student[1] for student in students]
    english_scores = [student[2] for student in students]
    science_scores = [student[3] for student in students]

    print(f"\n과목별 평균:")
    print(f"수학: {sum(math_scores) / len(math_scores):.1f}")
    print(f"영어: {sum(english_scores) / len(english_scores):.1f}")
    print(f"과학: {sum(science_scores) / len(science_scores):.1f}")
    print()

    # 3. 리스트를 이용한 스택과 큐 구현
    print("3. 리스트를 이용한 스택과 큐 구현")

    # 스택 (Stack) - LIFO (Last In, First Out)
    print("스택 (Stack) 구현:")
    stack = []

    # 스택에 요소 추가 (push)
    stack.append("첫 번째")
    stack.append("두 번째")
    stack.append("세 번째")
    print(f"스택에 추가 후: {stack}")

    # 스택에서 요소 제거 (pop)
    popped = stack.pop()
    print(f"pop() 결과: {popped}, 남은 스택: {stack}")

    popped = stack.pop()
    print(f"pop() 결과: {popped}, 남은 스택: {stack}")

    # 큐 (Queue) - FIFO (First In, First Out)
    print("\n큐 (Queue) 구현:")
    queue = []

    # 큐에 요소 추가 (enqueue)
    queue.append("고객1")
    queue.append("고객2")
    queue.append("고객3")
    print(f"큐에 추가 후: {queue}")

    # 큐에서 요소 제거 (dequeue)
    dequeued = queue.pop(0)  # 첫 번째 요소 제거
    print(f"dequeue() 결과: {dequeued}, 남은 큐: {queue}")

    dequeued = queue.pop(0)
    print(f"dequeue() 결과: {dequeued}, 남은 큐: {queue}")
    print()

    # 4. 리스트를 이용한 통계 분석
    print("4. 리스트를 이용한 통계 분석")

    # 시험 점수 데이터
    scores = [85, 92, 78, 96, 88, 85, 90, 92, 78, 85, 88, 92, 96, 78, 90]
    print(f"시험 점수: {scores}")

    # 기본 통계
    print(f"점수 개수: {len(scores)}")
    print(f"최고점: {max(scores)}")
    print(f"최저점: {min(scores)}")
    print(f"평균: {sum(scores) / len(scores):.2f}")

    # 중앙값 계산
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    if n % 2 == 0:
        median = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2
    else:
        median = sorted_scores[n//2]
    print(f"중앙값: {median}")

    # 점수 분포 (도수)
    score_counts = {}
    for score in scores:
        score_counts[score] = score_counts.get(score, 0) + 1

    print("점수 분포:")
    for score in sorted(score_counts.keys()):
        print(f"  {score}점: {score_counts[score]}명")

    # 구간별 분포
    ranges = [(0, 60, "F"), (60, 70, "D"), (70, 80, "C"), (80, 90, "B"), (90, 100, "A")]
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for score in scores:
        for min_score, max_score, grade in ranges:
            if min_score <= score < max_score:
                grade_counts[grade] += 1
                break

    print("\n등급별 분포:")
    for grade, count in grade_counts.items():
        print(f"  {grade}등급: {count}명")
    print()

    # 5. 리스트를 이용한 알고리즘 구현
    print("5. 리스트를 이용한 알고리즘 구현")

    # 버블 정렬 (Bubble Sort)
    def bubble_sort(arr):
        """버블 정렬 알고리즘"""
        n = len(arr)
        arr_copy = arr.copy()  # 원본 보호

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    # 요소 교환
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]

        return arr_copy

    # 이진 탐색 (Binary Search)
    def binary_search(arr, target):
        """이진 탐색 알고리즘 (정렬된 리스트에서 사용)"""
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # 찾지 못함

    # 알고리즘 테스트
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"정렬 전: {test_data}")

    sorted_data = bubble_sort(test_data)
    print(f"정렬 후: {sorted_data}")

    # 이진 탐색 테스트
    target = 25
    index = binary_search(sorted_data, target)
    if index != -1:
        print(f"{target}을(를) 인덱스 {index}에서 찾았습니다.")
    else:
        print(f"{target}을(를) 찾지 못했습니다.")

    target = 100
    index = binary_search(sorted_data, target)
    if index != -1:
        print(f"{target}을(를) 인덱스 {index}에서 찾았습니다.")
    else:
        print(f"{target}을(를) 찾지 못했습니다.")
    print()

    # 6. 리스트를 이용한 게임 로직
    print("6. 리스트를 이용한 게임 로직")

    # 틱택토 게임 보드
    def print_board(board):
        """게임 보드 출력"""
        for i in range(3):
            print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
            if i < 2:
                print("-----------")

    def check_winner(board):
        """승자 확인"""
        # 승리 조건들
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
            [0, 4, 8], [2, 4, 6]  # 대각선
        ]

        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
                return board[condition[0]]
        return None

    # 게임 시뮬레이션
    board = [" " for _ in range(9)]  # 빈 보드
    print("틱택토 게임 보드:")
    print_board(board)

    # 게임 진행 시뮬레이션
    moves = [0, 4, 1, 7, 2]  # X가 이기는 시나리오
    players = ["X", "O"]

    for i, move in enumerate(moves):
        player = players[i % 2]
        board[move] = player
        print(f"\n{player}가 {move}번 위치에 놓음:")
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"\n{winner}가 승리했습니다!")
            break

    print()

    # 7. 리스트를 이용한 데이터 처리
    print("7. 리스트를 이용한 데이터 처리")

    # 상품 데이터
    products = [
        ["노트북", 1200000, "전자제품", 5],
        ["마우스", 25000, "전자제품", 20],
        ["키보드", 80000, "전자제품", 15],
        ["책상", 150000, "가구", 3],
        ["의자", 200000, "가구", 8],
        ["모니터", 300000, "전자제품", 10]
    ]

    print("상품 목록:")
    print("상품명\t\t가격\t\t카테고리\t재고")
    print("-" * 50)

    for product in products:
        name, price, category, stock = product
        print(f"{name}\t\t{price:,}원\t{category}\t{stock}개")

    # 카테고리별 상품 수
    categories = {}
    for product in products:
        category = product[2]
        categories[category] = categories.get(category, 0) + 1

    print(f"\n카테고리별 상품 수: {categories}")

    # 가격대별 상품 분류
    price_ranges = {
        "저가": [p for p in products if p[1] < 100000],
        "중가": [p for p in products if 100000 <= p[1] < 500000],
        "고가": [p for p in products if p[1] >= 500000]
    }

    print("\n가격대별 상품 분류:")
    for range_name, products_in_range in price_ranges.items():
        print(f"{range_name}: {len(products_in_range)}개")
        for product in products_in_range:
            print(f"  - {product[0]}: {product[1]:,}원")

    # 재고 부족 상품 찾기
    low_stock = [p for p in products if p[3] < 10]
    print(f"\n재고 부족 상품 (10개 미만): {len(low_stock)}개")
    for product in low_stock:
        print(f"  - {product[0]}: {product[3]}개")

if __name__ == "__main__":
    main()
