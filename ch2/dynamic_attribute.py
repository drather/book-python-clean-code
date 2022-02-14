class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"

        raise AttributeError(f"{self.__class__.__name__} 에는 {attr} 속성이 없음.")


if __name__ == '__main__':
    dyn = DynamicAttributes("value")

    # 객체의 속성을 요청하고 그 결과를 반환
    print(f"dyn.attribute: {dyn.attribute}")

    # 객체에 없는 `fallback_test` 라는 메서드를 호출 -> `__getattr__` 메서드가 호출되어 값을 반환
    # 파라미터 값을 포함한 문자열을 반환
    print(f"dyn.fallback_test: {dyn.fallback_test}")

    # `fallback_new` 라는 새로운 속성이 생성됨. 실제로, dyn.fallback_new = "new value" 속성을 생성한 것과 동일
    # 이 때, `__getattr__` 의 로직이 적용 x
    dyn.__dict__["fallback_new"] = "new_value"
    print(f"dyn.fallback_new: {dyn.fallback_new}")

    # 값을 찾을 수 없는 경우, `__getattr__` 는 `AttributeError` 예외가 발생
    print(getattr(dyn, "something", "default"))
