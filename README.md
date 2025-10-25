# 파이썬 3.14 교육 자료
# Python 3.14 Educational Materials

이 폴더는 파이썬 3.14 버전에 맞춘 교육용 예제들을 포함하고 있습니다.
This folder contains educational examples tailored for Python 3.14.

## 📁 폴더 구조 (Folder Structure)

```
python-education/
├── variables/                    # 변수 (Variables)
│   ├── basic_variables.py      # 기본 변수 타입
│   ├── collection_variables.py  # 컬렉션 타입 변수
│   └── variable_scope_naming.py # 변수 스코프와 네이밍
├── operators/                   # 연산자 (Operators)
│   ├── arithmetic_operators.py # 산술 연산자
│   ├── comparison_logical_operators.py # 비교 및 논리 연산자
│   └── bitwise_other_operators.py # 비트 연산자 및 기타
├── control_statements/          # 제어문 (Control Statements)
│   ├── conditional_statements.py # 조건문
│   ├── loop_statements.py      # 반복문
│   └── advanced_control_statements.py # 고급 제어문
├── classes_inheritance/         # 클래스와 상속 (Classes & Inheritance)
│   └── basic_classes.py        # 기본 클래스와 상속
├── lists/                      # 리스트 (Lists)
│   ├── basic_list_operations.py # 기본 리스트 연산
│   ├── advanced_list_operations.py # 고급 리스트 연산
│   └── practical_list_examples.py # 실용적인 리스트 예제
└── README.md                   # 이 파일
```

## 📚 학습 내용 (Learning Contents)

### 1. 변수 (Variables)
- **기본 변수 타입**: 정수, 실수, 문자열, 불린
- **컬렉션 타입**: 리스트, 튜플, 딕셔너리, 집합
- **변수 스코프와 네이밍**: 전역/지역 변수, 네이밍 규칙

### 2. 연산자 (Operators)
- **산술 연산자**: +, -, *, /, //, %, **
- **비교 및 논리 연산자**: ==, !=, <, >, and, or, not
- **비트 연산자**: &, |, ^, ~, <<, >>
- **기타 연산자**: 삼항 연산자, walrus 연산자, 연산자 우선순위

### 3. 제어문 (Control Statements)
- **조건문**: if, elif, else, 중첩 조건문
- **반복문**: for, while, break, continue
- **고급 제어문**: 복합 조건, 패턴 만들기, 알고리즘 구현

### 4. 클래스와 상속 (Classes & Inheritance)
- **기본 클래스**: 클래스 정의, 생성자, 메서드
- **상속**: 부모-자식 클래스 관계, 메서드 오버라이딩
- **클래스 변수와 인스턴스 변수**: 차이점과 사용법

### 5. 리스트 (Lists)
- **기본 연산**: 생성, 인덱싱, 슬라이싱, 추가/삭제
- **고급 기능**: 정렬, 검색, 복사, 컴프리헨션
- **실용 예제**: 학생 관리, 쇼핑몰, 도서관, 투두리스트

## 🚀 사용 방법 (How to Use)

### 개별 파일 실행
```bash
# 변수 예제 실행
python variables/basic_variables.py

# 연산자 예제 실행
python operators/arithmetic_operators.py

# 제어문 예제 실행
python control_statements/conditional_statements.py

# 클래스 예제 실행
python classes_inheritance/basic_classes.py

# 리스트 예제 실행
python lists/basic_list_operations.py
```

### 전체 예제 실행
```bash
# 모든 예제를 순차적으로 실행
for file in $(find python-education -name "*.py" | sort); do
    echo "=== 실행 중: $file ==="
    python "$file"
    echo ""
done
```

## 📖 예제 특징 (Example Features)

### 🎯 교육 목적
- **단계별 학습**: 기초부터 고급까지 체계적인 구성
- **실용적 예제**: 실제 프로젝트에서 사용할 수 있는 코드
- **한글 주석**: 모든 코드에 상세한 한글 설명 포함

### 💡 학습 포인트
- **파이썬 3.14 최신 기능** 반영
- **실무 중심** 예제와 시나리오
- **다양한 응용** 사례 제공

### 🔧 코드 품질
- **PEP 8 스타일 가이드** 준수
- **명확한 변수명** 사용
- **모듈화된 구조**로 재사용성 고려

## 📝 각 파일별 상세 설명

### Variables (변수)
1. **basic_variables.py**: 파이썬의 기본 데이터 타입 소개
2. **collection_variables.py**: 리스트, 튜플, 딕셔너리, 집합 사용법
3. **variable_scope_naming.py**: 변수 스코프와 네이밍 규칙

### Operators (연산자)
1. **arithmetic_operators.py**: 수학 연산과 문자열 연산
2. **comparison_logical_operators.py**: 조건 판단과 논리 연산
3. **bitwise_other_operators.py**: 비트 연산과 고급 연산자

### Control Statements (제어문)
1. **conditional_statements.py**: if문과 조건 분기
2. **loop_statements.py**: for문과 while문
3. **advanced_control_statements.py**: 복합 제어문과 알고리즘

### Classes & Inheritance (클래스와 상속)
1. **basic_classes.py**: 클래스 정의, 상속, 메서드 오버라이딩

### Lists (리스트)
1. **basic_list_operations.py**: 리스트 기본 조작법
2. **advanced_list_operations.py**: 고급 리스트 기능과 알고리즘
3. **practical_list_examples.py**: 실제 프로젝트에서 사용하는 리스트 활용

## 🎓 학습 순서 권장사항

1. **Variables** → **Operators** → **Control Statements** → **Lists** → **Classes**
2. 각 폴더 내에서 파일 순서대로 학습
3. 예제 코드를 직접 실행해보며 결과 확인
4. 코드를 수정해보며 다양한 시나리오 테스트

## 🔍 추가 학습 자료

- [Python 공식 문서](https://docs.python.org/3.14/)
- [PEP 8 스타일 가이드](https://pep8.org/)
- [Python 튜토리얼](https://docs.python.org/3.14/tutorial/)

## 📞 문의사항

교육 자료에 대한 문의사항이나 개선 제안이 있으시면 언제든지 연락해주세요.

---

**Happy Coding! 🐍✨**
