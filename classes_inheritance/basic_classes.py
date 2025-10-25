#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파이썬 3.14 기본 클래스 예제
Python 3.14 Basic Classes Example

이 예제는 파이썬의 기본 클래스 개념을 다룹니다.
This example covers basic class concepts in Python.
"""

class Person:
    """사람을 나타내는 기본 클래스"""
    
    # 클래스 변수 (Class Variable)
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age, gender):
        """생성자 (Constructor)"""
        # 인스턴스 변수 (Instance Variables)
        self.name = name
        self.age = age
        self.gender = gender
        
        # 클래스 변수 증가
        Person.population += 1
    
    def introduce(self):
        """자기소개 메서드"""
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세 {self.gender}입니다."
    
    def get_info(self):
        """정보 반환 메서드"""
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "species": self.species
        }
    
    def have_birthday(self):
        """생일 메서드 - 나이 증가"""
        self.age += 1
        print(f"{self.name}의 생일! 이제 {self.age}세가 되었습니다.")
    
    @classmethod
    def get_population(cls):
        """클래스 메서드 - 전체 인구 수 반환"""
        return f"현재 총 {cls.population}명의 사람이 있습니다."
    
    @staticmethod
    def is_adult(age):
        """정적 메서드 - 성인 여부 판단"""
        return age >= 18
    
    def __str__(self):
        """문자열 표현"""
        return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}')"
    
    def __repr__(self):
        """개발자용 문자열 표현"""
        return f"Person('{self.name}', {self.age}, '{self.gender}')"


class Student(Person):
    """학생 클래스 - Person을 상속"""
    
    def __init__(self, name, age, gender, student_id, major):
        # 부모 클래스 생성자 호출
        super().__init__(name, age, gender)
        
        # 학생만의 속성
        self.student_id = student_id
        self.major = major
        self.grades = []
    
    def add_grade(self, subject, score):
        """성적 추가 메서드"""
        self.grades.append({"subject": subject, "score": score})
        print(f"{self.name}의 {subject} 성적 {score}점이 추가되었습니다.")
    
    def get_average_grade(self):
        """평균 성적 계산 메서드"""
        if not self.grades:
            return 0
        
        total_score = sum(grade["score"] for grade in self.grades)
        return total_score / len(self.grades)
    
    def introduce(self):
        """자기소개 메서드 오버라이드"""
        base_intro = super().introduce()
        return f"{base_intro} 저는 {self.major} 전공 학생이고 학번은 {self.student_id}입니다."
    
    def get_info(self):
        """정보 반환 메서드 오버라이드"""
        info = super().get_info()
        info.update({
            "student_id": self.student_id,
            "major": self.major,
            "grades": self.grades,
            "average_grade": self.get_average_grade()
        })
        return info
    
    def __str__(self):
        """문자열 표현 오버라이드"""
        return f"Student(name='{self.name}', age={self.age}, major='{self.major}', id='{self.student_id}')"


class Teacher(Person):
    """교사 클래스 - Person을 상속"""
    
    def __init__(self, name, age, gender, teacher_id, subject, experience_years):
        # 부모 클래스 생성자 호출
        super().__init__(name, age, gender)
        
        # 교사만의 속성
        self.teacher_id = teacher_id
        self.subject = subject
        self.experience_years = experience_years
        self.students = []
    
    def add_student(self, student):
        """학생 추가 메서드"""
        if isinstance(student, Student):
            self.students.append(student)
            print(f"{student.name} 학생이 {self.name} 선생님의 수업에 추가되었습니다.")
        else:
            print("학생 객체만 추가할 수 있습니다.")
    
    def teach(self):
        """수업 메서드"""
        print(f"{self.name} 선생님이 {self.subject} 수업을 진행합니다.")
        print(f"경력 {self.experience_years}년의 노하우를 전달합니다.")
    
    def introduce(self):
        """자기소개 메서드 오버라이드"""
        base_intro = super().introduce()
        return f"{base_intro} 저는 {self.subject} 교사이고 {self.experience_years}년 경력이 있습니다."
    
    def get_info(self):
        """정보 반환 메서드 오버라이드"""
        info = super().get_info()
        info.update({
            "teacher_id": self.teacher_id,
            "subject": self.subject,
            "experience_years": self.experience_years,
            "student_count": len(self.students)
        })
        return info
    
    def __str__(self):
        """문자열 표현 오버라이드"""
        return f"Teacher(name='{self.name}', age={self.age}, subject='{self.subject}', experience={self.experience_years}년)"


def main():
    print("=== 파이썬 기본 클래스 예제 ===")
    print("=== Python Basic Classes Example ===\n")
    
    # 1. 기본 Person 클래스 사용
    print("1. 기본 Person 클래스 사용")
    person1 = Person("김철수", 25, "남성")
    person2 = Person("이영희", 30, "여성")
    
    print(person1.introduce())
    print(person2.introduce())
    print(f"Person 클래스 정보: {person1.get_info()}")
    print(Person.get_population())
    print(f"25세는 성인인가? {Person.is_adult(25)}")
    print(f"15세는 성인인가? {Person.is_adult(15)}")
    print()
    
    # 2. Student 클래스 사용
    print("2. Student 클래스 사용")
    student1 = Student("박민수", 20, "남성", "2023001", "컴퓨터공학")
    student2 = Student("최지영", 22, "여성", "2023002", "수학")
    
    print(student1.introduce())
    print(student2.introduce())
    
    # 성적 추가
    student1.add_grade("프로그래밍", 95)
    student1.add_grade("자료구조", 88)
    student1.add_grade("알고리즘", 92)
    
    student2.add_grade("미적분학", 90)
    student2.add_grade("선형대수", 85)
    
    print(f"{student1.name}의 평균 성적: {student1.get_average_grade():.1f}")
    print(f"{student2.name}의 평균 성적: {student2.get_average_grade():.1f}")
    print()
    
    # 3. Teacher 클래스 사용
    print("3. Teacher 클래스 사용")
    teacher1 = Teacher("정교수", 45, "남성", "T001", "프로그래밍", 15)
    teacher2 = Teacher("김교수", 38, "여성", "T002", "수학", 10)
    
    print(teacher1.introduce())
    print(teacher2.introduce())
    
    teacher1.teach()
    teacher2.teach()
    
    # 학생 추가
    teacher1.add_student(student1)
    teacher2.add_student(student2)
    
    print(f"{teacher1.name} 선생님의 학생 수: {len(teacher1.students)}")
    print(f"{teacher2.name} 선생님의 학생 수: {len(teacher2.students)}")
    print()
    
    # 4. 클래스 정보 출력
    print("4. 클래스 정보 출력")
    print(f"Person 클래스: {Person}")
    print(f"Student 클래스: {Student}")
    print(f"Teacher 클래스: {Teacher}")
    print()
    
    print("객체 정보:")
    print(f"person1: {person1}")
    print(f"student1: {student1}")
    print(f"teacher1: {teacher1}")
    print()
    
    # 5. 상속 관계 확인
    print("5. 상속 관계 확인")
    print(f"Student는 Person의 서브클래스인가? {issubclass(Student, Person)}")
    print(f"Teacher는 Person의 서브클래스인가? {issubclass(Teacher, Person)}")
    print(f"student1은 Student의 인스턴스인가? {isinstance(student1, Student)}")
    print(f"student1은 Person의 인스턴스인가? {isinstance(student1, Person)}")
    print(f"teacher1은 Student의 인스턴스인가? {isinstance(teacher1, Student)}")
    print()
    
    # 6. 전체 인구 수 확인
    print("6. 전체 인구 수 확인")
    print(Person.get_population())
    print()
    
    # 7. 생일 이벤트
    print("7. 생일 이벤트")
    person1.have_birthday()
    student1.have_birthday()
    teacher1.have_birthday()

if __name__ == "__main__":
    main()

