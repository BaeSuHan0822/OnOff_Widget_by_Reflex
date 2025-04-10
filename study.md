@ : decorator : 함수를 감싸는 함수
ex)
def say_hello():
    print("안녕!")

say_hello()  # → 안녕!

def decorate(func):
    def wrapper():
        print("🍀 기능 실행 전")
        func()
        print("🍀 기능 실행 후")
    return wrapper

say_hello = decorate(say_hello)
say_hello()

-> 축약
@decorate
def say_hello():
    print("안녕!")

@rx.var : 함수 결과를 "값"처럼 보여줌 -> 상태 기반으로 계산된 값 반환
@rx.event : 함수를 이벤트 핸들러로 등록 -> 사용자 액션에 반응해서 상태 변경 (진짜 이벤트 핸들러로 쓰게 만듦)


@rx.var -> Reflex State에 기반해서 자동으로 업데이트하는 계산된 값을 만드는 방법

@rx.var와 일반 속성의 차이
| **특징**       | **일반 속성**                     | **@rx.var 속성**               |
|----------------|-----------------------------------|---------------------------------|
| **값 저장**    | 값을 직접 저장                   | 계산된 값을 반환               |
| **UI 업데이트**| 상태 변경 시 수동으로 업데이트 필요 | 상태 변경 시 자동으로 UI 업데이트 |
| **읽기/쓰기**  | 읽기 및 쓰기 가능                | 읽기 전용                      |
| **사용 목적**  | 단순 데이터 저장                 | 동적으로 계산된 값 제공        |

lambda 함수 사용 : Reflex에서 lambda함수가 주는 값 추적 불가능 + self 인수값 전달x
lambda 함수 사용x : Reflex에서 자체적으로 self 인수값 전달

-> : Return Type Hint 반환될 값의 타입을 명시해줌
    효과 - 코드의 가독성을 높이고 타입 검사 도구를 사용할 때 유용
@rx.var 데코레이터가 반환 타입을 명시적으로 요구하기 때문에 @rx.var에는 반드시 사용