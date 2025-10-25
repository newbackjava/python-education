#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 리스트 실용 예제
Python 3.14 Practical List Examples

이 예제는 파이썬 리스트를 이용한 실용적인 프로그램들을 다룹니다.
This example covers practical programs using Python lists.
"""

def main():
    print("=== 파이썬 리스트 실용 예제 ===")
    print("=== Python Practical List Examples ===\n")

    # 1. 학생 성적 관리 시스템
    print("1. 학생 성적 관리 시스템")

    class StudentManager:
        """학생 성적 관리 클래스"""

        def __init__(self):
            self.students = []  # 학생 정보를 저장할 리스트

        def add_student(self, name, student_id, grades):
            """학생 추가"""
            student = {
                "name": name,
                "id": student_id,
                "grades": grades,
                "average": sum(grades) / len(grades) if grades else 0
            }
            self.students.append(student)
            print(f"학생 {name} (학번: {student_id})이 추가되었습니다.")

        def get_student_by_id(self, student_id):
            """학번으로 학생 찾기"""
            for student in self.students:
                if student["id"] == student_id:
                    return student
            return None

        def update_grades(self, student_id, new_grades):
            """성적 업데이트"""
            student = self.get_student_by_id(student_id)
            if student:
                student["grades"] = new_grades
                student["average"] = sum(new_grades) / len(new_grades)
                print(f"학번 {student_id}의 성적이 업데이트되었습니다.")
            else:
                print(f"학번 {student_id}을 찾을 수 없습니다.")

        def get_class_average(self):
            """반 평균 계산"""
            if not self.students:
                return 0
            total_average = sum(student["average"] for student in self.students)
            return total_average / len(self.students)

        def get_top_students(self, n=3):
            """상위 n명 학생 반환"""
            sorted_students = sorted(self.students, key=lambda x: x["average"], reverse=True)
            return sorted_students[:n]

        def print_report(self):
            """성적표 출력"""
            print("\n=== 성적표 ===")
            print("학번\t이름\t성적\t평균")
            print("-" * 30)

            for student in self.students:
                grades_str = ", ".join(map(str, student["grades"]))
                print(f"{student['id']}\t{student['name']}\t{grades_str}\t{student['average']:.1f}")

            print(f"\n반 평균: {self.get_class_average():.1f}")

            top_students = self.get_top_students(3)
            print("\n상위 3명:")
            for i, student in enumerate(top_students, 1):
                print(f"{i}. {student['name']} - {student['average']:.1f}")

    # 학생 관리 시스템 사용 예제
    manager = StudentManager()

    # 학생들 추가
    manager.add_student("김철수", "2023001", [85, 92, 78, 90])
    manager.add_student("이영희", "2023002", [90, 88, 95, 87])
    manager.add_student("박민수", "2023003", [78, 85, 92, 88])
    manager.add_student("최지영", "2023004", [95, 90, 88, 92])

    # 성적표 출력
    manager.print_report()
    print()

    # 2. 쇼핑몰 장바구니 시스템
    print("2. 쇼핑몰 장바구니 시스템")

    class ShoppingCart:
        """쇼핑몰 장바구니 클래스"""

        def __init__(self):
            self.items = []  # 장바구니 아이템 리스트

        def add_item(self, name, price, quantity=1):
            """상품 추가"""
            # 이미 있는 상품인지 확인
            for item in self.items:
                if item["name"] == name:
                    item["quantity"] += quantity
                    print(f"{name}의 수량이 {item['quantity']}개로 업데이트되었습니다.")
                    return

            # 새로운 상품 추가
            item = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            self.items.append(item)
            print(f"{name} {quantity}개가 장바구니에 추가되었습니다.")

        def remove_item(self, name):
            """상품 제거"""
            for i, item in enumerate(self.items):
                if item["name"] == name:
                    removed_item = self.items.pop(i)
                    print(f"{removed_item['name']}이 장바구니에서 제거되었습니다.")
                    return
            print(f"{name}을 찾을 수 없습니다.")

        def update_quantity(self, name, new_quantity):
            """수량 업데이트"""
            for item in self.items:
                if item["name"] == name:
                    item["quantity"] = new_quantity
                    print(f"{name}의 수량이 {new_quantity}개로 변경되었습니다.")
                    return
            print(f"{name}을 찾을 수 없습니다.")

        def get_total_price(self):
            """총 가격 계산"""
            total = 0
            for item in self.items:
                total += item["price"] * item["quantity"]
            return total

        def apply_discount(self, discount_rate):
            """할인 적용"""
            total = self.get_total_price()
            discount_amount = total * discount_rate
            return total - discount_amount

        def print_cart(self):
            """장바구니 내용 출력"""
            if not self.items:
                print("장바구니가 비어있습니다.")
                return

            print("\n=== 장바구니 ===")
            print("상품명\t\t단가\t\t수량\t\t소계")
            print("-" * 50)

            for item in self.items:
                subtotal = item["price"] * item["quantity"]
                print(f"{item['name']}\t\t{item['price']:,}원\t{item['quantity']}개\t\t{subtotal:,}원")

            total = self.get_total_price()
            print("-" * 50)
            print(f"총 금액: {total:,}원")

    # 장바구니 사용 예제
    cart = ShoppingCart()

    # 상품 추가
    cart.add_item("노트북", 1200000, 1)
    cart.add_item("마우스", 25000, 2)
    cart.add_item("키보드", 80000, 1)
    cart.add_item("마우스", 25000, 1)  # 기존 상품 수량 증가

    # 장바구니 출력
    cart.print_cart()

    # 할인 적용
    discounted_total = cart.apply_discount(0.1)  # 10% 할인
    print(f"\n10% 할인 적용 후: {discounted_total:,}원")
    print()

    # 3. 도서관 도서 관리 시스템
    print("3. 도서관 도서 관리 시스템")

    class LibraryManager:
        """도서관 도서 관리 클래스"""

        def __init__(self):
            self.books = []  # 도서 정보 리스트
            self.borrowed_books = []  # 대출된 도서 리스트

        def add_book(self, title, author, isbn, copies=1):
            """도서 추가"""
            book = {
                "title": title,
                "author": author,
                "isbn": isbn,
                "copies": copies,
                "available": copies
            }
            self.books.append(book)
            print(f"도서 '{title}' {copies}권이 추가되었습니다.")

        def search_books(self, keyword):
            """도서 검색"""
            results = []
            keyword_lower = keyword.lower()

            for book in self.books:
                if (keyword_lower in book["title"].lower() or
                    keyword_lower in book["author"].lower() or
                    keyword_lower in book["isbn"]):
                    results.append(book)

            return results

        def borrow_book(self, isbn, borrower_name):
            """도서 대출"""
            for book in self.books:
                if book["isbn"] == isbn:
                    if book["available"] > 0:
                        book["available"] -= 1
                        borrowed_record = {
                            "isbn": isbn,
                            "title": book["title"],
                            "borrower": borrower_name,
                            "borrow_date": "2024-01-15"  # 실제로는 현재 날짜
                        }
                        self.borrowed_books.append(borrowed_record)
                        print(f"'{book['title']}'이 {borrower_name}님에게 대출되었습니다.")
                        return True
                    else:
                        print(f"'{book['title']}'은 현재 대출 중입니다.")
                        return False

            print(f"ISBN {isbn}에 해당하는 도서를 찾을 수 없습니다.")
            return False

        def return_book(self, isbn, borrower_name):
            """도서 반납"""
            for i, record in enumerate(self.borrowed_books):
                if record["isbn"] == isbn and record["borrower"] == borrower_name:
                    # 대출 기록 제거
                    returned_record = self.borrowed_books.pop(i)

                    # 도서 재고 복원
                    for book in self.books:
                        if book["isbn"] == isbn:
                            book["available"] += 1
                            break

                    print(f"'{returned_record['title']}'이 반납되었습니다.")
                    return True

            print(f"반납할 도서를 찾을 수 없습니다.")
            return False

        def print_library_status(self):
            """도서관 현황 출력"""
            print("\n=== 도서관 현황 ===")
            print("도서명\t\t저자\t\tISBN\t\t총권수\t대출가능")
            print("-" * 70)

            for book in self.books:
                print(f"{book['title']}\t\t{book['author']}\t\t{book['isbn']}\t\t{book['copies']}\t{book['available']}")

            print(f"\n총 도서 수: {len(self.books)}종")
            print(f"총 권수: {sum(book['copies'] for book in self.books)}권")
            print(f"대출 가능 권수: {sum(book['available'] for book in self.books)}권")
            print(f"대출 중 권수: {len(self.borrowed_books)}권")

            if self.borrowed_books:
                print("\n=== 대출 중인 도서 ===")
                print("도서명\t\t대출자\t\t대출일")
                print("-" * 40)
                for record in self.borrowed_books:
                    print(f"{record['title']}\t\t{record['borrower']}\t\t{record['borrow_date']}")

    # 도서관 관리 시스템 사용 예제
    library = LibraryManager()

    # 도서 추가
    library.add_book("파이썬 프로그래밍", "김파이썬", "978-1234567890", 3)
    library.add_book("자바스크립트 완벽 가이드", "이자바", "978-1234567891", 2)
    library.add_book("데이터베이스 설계", "박데이터", "978-1234567892", 1)
    library.add_book("알고리즘과 자료구조", "최알고", "978-1234567893", 2)

    # 도서 검색
    search_results = library.search_books("파이썬")
    print(f"\n'파이썬' 검색 결과: {len(search_results)}건")
    for book in search_results:
        print(f"  - {book['title']} ({book['author']})")

    # 도서 대출
    library.borrow_book("978-1234567890", "김학생")
    library.borrow_book("978-1234567890", "이학생")
    library.borrow_book("978-1234567891", "박학생")

    # 도서 반납
    library.return_book("978-1234567890", "김학생")

    # 도서관 현황 출력
    library.print_library_status()
    print()

    # 4. 투두 리스트 관리 시스템
    print("4. 투두 리스트 관리 시스템")

    class TodoManager:
        """투두 리스트 관리 클래스"""

        def __init__(self):
            self.todos = []  # 할 일 리스트
            self.completed = []  # 완료된 할 일 리스트

        def add_todo(self, task, priority="보통"):
            """할 일 추가"""
            todo = {
                "id": len(self.todos) + 1,
                "task": task,
                "priority": priority,
                "status": "대기",
                "created_date": "2024-01-15"
            }
            self.todos.append(todo)
            print(f"할 일이 추가되었습니다: {task}")

        def complete_todo(self, todo_id):
            """할 일 완료"""
            for i, todo in enumerate(self.todos):
                if todo["id"] == todo_id:
                    todo["status"] = "완료"
                    completed_todo = self.todos.pop(i)
                    self.completed.append(completed_todo)
                    print(f"할 일이 완료되었습니다: {completed_todo['task']}")
                    return True
            print(f"ID {todo_id}에 해당하는 할 일을 찾을 수 없습니다.")
            return False

        def get_todos_by_priority(self, priority):
            """우선순위별 할 일 조회"""
            return [todo for todo in self.todos if todo["priority"] == priority]

        def get_statistics(self):
            """통계 정보"""
            total = len(self.todos) + len(self.completed)
            completed_count = len(self.completed)
            pending_count = len(self.todos)

            return {
                "total": total,
                "completed": completed_count,
                "pending": pending_count,
                "completion_rate": (completed_count / total * 100) if total > 0 else 0
            }

        def print_todos(self):
            """할 일 목록 출력"""
            print("\n=== 할 일 목록 ===")
            if not self.todos:
                print("할 일이 없습니다.")
                return

            print("ID\t할 일\t\t우선순위\t상태")
            print("-" * 50)
            for todo in self.todos:
                print(f"{todo['id']}\t{todo['task']}\t\t{todo['priority']}\t\t{todo['status']}")

        def print_completed(self):
            """완료된 할 일 목록 출력"""
            print("\n=== 완료된 할 일 ===")
            if not self.completed:
                print("완료된 할 일이 없습니다.")
                return

            print("ID\t할 일\t\t완료일")
            print("-" * 40)
            for todo in self.completed:
                print(f"{todo['id']}\t{todo['task']}\t\t{todo['created_date']}")

    # 투두 리스트 관리 시스템 사용 예제
    todo_manager = TodoManager()

    # 할 일 추가
    todo_manager.add_todo("파이썬 공부하기", "높음")
    todo_manager.add_todo("운동하기", "보통")
    todo_manager.add_todo("책 읽기", "낮음")
    todo_manager.add_todo("프로젝트 완성하기", "높음")
    todo_manager.add_todo("친구 만나기", "낮음")

    # 할 일 목록 출력
    todo_manager.print_todos()

    # 할 일 완료
    todo_manager.complete_todo(1)  # 파이썬 공부하기 완료
    todo_manager.complete_todo(3)  # 책 읽기 완료

    # 완료된 할 일 출력
    todo_manager.print_completed()

    # 통계 정보
    stats = todo_manager.get_statistics()
    print(f"\n=== 통계 ===")
    print(f"전체 할 일: {stats['total']}개")
    print(f"완료: {stats['completed']}개")
    print(f"대기: {stats['pending']}개")
    print(f"완료율: {stats['completion_rate']:.1f}%")

    # 우선순위별 할 일 조회
    high_priority_todos = todo_manager.get_todos_by_priority("높음")
    print(f"\n높은 우선순위 할 일: {len(high_priority_todos)}개")
    for todo in high_priority_todos:
        print(f"  - {todo['task']}")

if __name__ == "__main__":
    main()
