#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 테스트 문제집
Python 3.14 Test Questions

이 파일은 파이썬 교육 내용을 테스트할 수 있는 문제들을 포함합니다.
This file contains test questions to evaluate Python learning content.

난이도별 구성:
- 하급 (10문제): 기본 문법과 개념
- 중급 (5문제): 응용과 실무 활용
- 상급 (5문제): 고급 개념과 알고리즘
"""

def print_question(level, number, question, options=None):
    """문제 출력 함수"""
    print(f"\n{'='*60}")
    print(f"[{level}급 문제 {number}]")
    print(f"{'='*60}")
    print(f"{question}")
    if options:
        print("\n선택지:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

def main():
    print("파이썬 3.14 테스트 문제집")
    print("Python 3.14 Test Questions")
    print("="*60)
    
    # 하급 문제 (1-10)
    print("\n" + "="*60)
    print("하급 문제 (Basic Level) - 10문제")
    print("="*60)
    
    print_question("하", 1, 
        "다음 중 파이썬에서 올바른 변수명은 무엇인가요?",
        ["1st_name", "class", "user_name", "2nd_grade"]
    )
    
    print_question("하", 2,
        "다음 코드의 실행 결과는 무엇인가요?\nresult = 10 // 3",
        ["3", "3.33", "3.0", "4"]
    )
    
    print_question("하", 3,
        "다음 리스트에서 '바나나'의 인덱스는 무엇인가요?\nfruits = ['사과', '바나나', '오렌지']",
        ["0", "1", "2", "3"]
    )
    
    print_question("하", 4,
        "다음 중 불린(boolean) 값이 아닌 것은 무엇인가요?",
        ["True", "False", "true", "1"]
    )
    
    print_question("하", 5,
        "다음 코드의 실행 결과는 무엇인가요?\nprint('Hello' + 'World')",
        ["HelloWorld", "Hello World", "Hello + World", "에러 발생"]
    )
    
    print_question("하", 6,
        "다음 딕셔너리에서 '나이' 값을 가져오는 올바른 방법은 무엇인가요?\nperson = {'이름': '김철수', '나이': 25}",
        ["person['나이']", "person.나이", "person.get('나이')", "person['나이'] 또는 person.get('나이')"]
    )
    
    print_question("하", 7,
        "다음 코드의 실행 결과는 무엇인가요?\nnumbers = [1, 2, 3, 4, 5]\nprint(len(numbers))",
        ["4", "5", "6", "에러 발생"]
    )
    
    print_question("하", 8,
        "다음 조건문에서 어떤 값이 출력되나요?\nage = 20\nif age >= 18:\n    print('성인')\nelse:\n    print('미성년자')",
        ["성인", "미성년자", "아무것도 출력되지 않음", "에러 발생"]
    )
    
    print_question("하", 9,
        "다음 for문의 실행 횟수는 몇 번인가요?\nfor i in range(3):\n    print(i)",
        ["2번", "3번", "4번", "무한번"]
    )
    
    print_question("하", 10,
        "다음 집합의 결과는 무엇인가요?\nnumbers = {1, 2, 2, 3, 3, 4}",
        ["{1, 2, 2, 3, 3, 4}", "{1, 2, 3, 4}", "{2, 3}", "에러 발생"]
    )
    
    # 중급 문제 (11-15)
    print("\n" + "="*60)
    print("중급 문제 (Intermediate Level) - 5문제")
    print("="*60)
    
    print_question("중", 11,
        "다음 리스트 컴프리헨션의 결과는 무엇인가요?\n[x**2 for x in range(1, 4)]",
        ["[1, 4, 9]", "[1, 2, 3]", "[2, 4, 6]", "[0, 1, 4]"]
    )
    
    print_question("중", 12,
        "다음 코드의 실행 결과는 무엇인가요?\nnumbers = [1, 2, 3, 4, 5]\nresult = [x for x in numbers if x % 2 == 0]",
        ["[1, 3, 5]", "[2, 4]", "[0, 2, 4]", "[1, 2, 3, 4, 5]"]
    )
    
    print_question("중", 13,
        "다음 클래스에서 Student 인스턴스의 introduce() 메서드 호출 결과는 무엇인가요?\n\nclass Person:\n    def __init__(self, name):\n        self.name = name\n    def introduce(self):\n        return f'안녕하세요, {self.name}입니다.'\n\nclass Student(Person):\n    def __init__(self, name, student_id):\n        super().__init__(name)\n        self.student_id = student_id\n    def introduce(self):\n        return f'안녕하세요, {self.name}입니다. 학번은 {self.student_id}입니다.'\n\nstudent = Student('김철수', '2023001')\nprint(student.introduce())",
        ["안녕하세요, 김철수입니다.", "안녕하세요, 김철수입니다. 학번은 2023001입니다.", "에러 발생", "아무것도 출력되지 않음"]
    )
    
    print_question("중", 14,
        "다음 코드의 실행 결과는 무엇인가요?\n\ndef process_data(data):\n    if isinstance(data, list):\n        return sum(data) / len(data)\n    elif isinstance(data, dict):\n        return sum(data.values()) / len(data)\n    else:\n        return data\n\nresult = process_data({'a': 10, 'b': 20, 'c': 30})",
        ["20", "60", "30", "에러 발생"]
    )
    
    print_question("중", 15,
        "다음 코드에서 리스트의 얕은 복사와 깊은 복사의 차이를 보여주는 예제입니다.\n원본 리스트를 수정한 후 각각의 결과는 무엇인가요?\n\nimport copy\noriginal = [1, 2, [3, 4]]\nshallow = original.copy()\ndeep = copy.deepcopy(original)\n\noriginal[2][0] = 999\n\nprint(f'원본: {original}')\nprint(f'얕은 복사: {shallow}')\nprint(f'깊은 복사: {deep}')",
        ["원본: [1, 2, [999, 4]], 얕은 복사: [1, 2, [999, 4]], 깊은 복사: [1, 2, [3, 4]]", 
         "원본: [1, 2, [999, 4]], 얕은 복사: [1, 2, [3, 4]], 깊은 복사: [1, 2, [3, 4]]",
         "원본: [1, 2, [999, 4]], 얕은 복사: [1, 2, [999, 4]], 깊은 복사: [1, 2, [999, 4]]",
         "에러 발생"]
    )
    
    # 상급 문제 (16-20)
    print("\n" + "="*60)
    print("상급 문제 (Advanced Level) - 5문제")
    print("="*60)
    
    print_question("상", 16,
        "다음 코드는 학생 성적을 관리하는 클래스입니다.\nget_top_students(2) 메서드 호출 결과는 무엇인가요?\n\nclass StudentManager:\n    def __init__(self):\n        self.students = []\n    \n    def add_student(self, name, grades):\n        avg = sum(grades) / len(grades)\n        self.students.append({'name': name, 'grades': grades, 'average': avg})\n    \n    def get_top_students(self, n):\n        sorted_students = sorted(self.students, key=lambda x: x['average'], reverse=True)\n        return sorted_students[:n]\n\nmanager = StudentManager()\nmanager.add_student('김철수', [85, 90, 88])\nmanager.add_student('이영희', [92, 88, 95])\nmanager.add_student('박민수', [78, 85, 82])\n\ntop_students = manager.get_top_students(2)",
        ["김철수, 이영희", "이영희, 김철수", "박민수, 김철수", "에러 발생"]
    )
    
    print_question("상", 17,
        "다음 코드는 리스트를 이용한 스택 구현입니다.\n모든 연산을 수행한 후 스택의 상태는 무엇인가요?\n\nclass Stack:\n    def __init__(self):\n        self.items = []\n    \n    def push(self, item):\n        self.items.append(item)\n    \n    def pop(self):\n        return self.items.pop() if self.items else None\n    \n    def peek(self):\n        return self.items[-1] if self.items else None\n    \n    def is_empty(self):\n        return len(self.items) == 0\n\nstack = Stack()\nstack.push(1)\nstack.push(2)\nstack.push(3)\nstack.pop()\nstack.push(4)\nstack.pop()\nstack.pop()",
        ["[1]", "[1, 2]", "[1, 2, 3]", "[]"]
    )
    
    print_question("상", 18,
        "다음 코드는 문자열에서 가장 많이 나타나는 문자를 찾는 함수입니다.\nmost_frequent_char('hello world')의 결과는 무엇인가요?\n\ndef most_frequent_char(text):\n    char_count = {}\n    for char in text:\n        if char != ' ':\n            char_count[char] = char_count.get(char, 0) + 1\n    \n    max_count = max(char_count.values())\n    most_frequent = [char for char, count in char_count.items() if count == max_count]\n    return most_frequent[0] if len(most_frequent) == 1 else most_frequent",
        ["'l'", "'o'", "['l', 'o']", "에러 발생"]
    )
    
    print_question("상", 19,
        "다음 코드는 이진 탐색 알고리즘입니다.\nbinary_search([1, 3, 5, 7, 9, 11, 13], 7)의 결과는 무엇인가요?\n\ndef binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    \n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
        ["3", "4", "5", "-1"]
    )
    
    print_question("상", 20,
        "다음 코드는 도서관 관리 시스템의 일부입니다.\nborrow_book('978-1234567890', '김학생') 호출 후 도서관 상태는 어떻게 되나요?\n\nclass Library:\n    def __init__(self):\n        self.books = [\n            {'isbn': '978-1234567890', 'title': '파이썬 프로그래밍', 'available': 2},\n            {'isbn': '978-1234567891', 'title': '자바스크립트', 'available': 1}\n        ]\n        self.borrowed = []\n    \n    def borrow_book(self, isbn, borrower):\n        for book in self.books:\n            if book['isbn'] == isbn and book['available'] > 0:\n                book['available'] -= 1\n                self.borrowed.append({'isbn': isbn, 'borrower': borrower})\n                return True\n        return False\n\nlibrary = Library()\nresult = library.borrow_book('978-1234567890', '김학생')",
        ["파이썬 프로그래밍 도서의 available이 1이 되고, borrowed 리스트에 대출 기록이 추가됨",
         "파이썬 프로그래밍 도서의 available이 0이 되고, borrowed 리스트에 대출 기록이 추가됨",
         "아무 변화 없음",
         "에러 발생"]
    )

if __name__ == "__main__":
    main()
