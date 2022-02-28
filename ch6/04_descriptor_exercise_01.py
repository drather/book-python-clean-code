class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name) -> None:
        self.trace_attribute_name = trace_attribute_name
        # current_city 에 할당. 이에 대한 추적을 저장할 변수 이름을 디스크립터에 전달.
        # 이 예에서는 cities_visited 속성에 current_city 의 모든 값을 추적하라 지시
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._track_change_value_for_instance(instance, value)
        instance.__dict__[self._name] = value

    def _track_change_value_for_instance(self, instance, value):
        self._set_default(instance)
        # 디스크립터를 처음으로 호출할 때, 추적 값이 존재하지 않을 것이므로 나중에 초가할 수 있도록 초기화
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance, value) -> bool:
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            # 처음 Traveller 를 호출할 때는 방문지 X 이므로,키가 없다. 이 경우, True 를 리턴한다.
            return True
        return value != current_value
        # 새 값이 현재 설정된 값과 다를 때만 변경 사항 추적

    def _set_default(self, instance):
        instance.__dict__.setdefault(self.trace_attribute_name, [])
        # 없는 키 조회할 때 사용하는 메서드


class Traveller:
    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city
        # 디스크립터가 이미 생성된 단계
        # 2단계 값을 추적하기 위한 빈 리스트 만들기 실행
        # 3단계 실행하여 리스트에 값을 추가하고 검색 위한 키 설정
