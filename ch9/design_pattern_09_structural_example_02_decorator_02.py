from typing import Iterable, Callable, Dict


class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query


class QueryEnhancer:
    def __init__(self, query: DictQuery, *decorators: Iterable[Callable][[Dict[str, str]], Dict[str, str]]) -> None:
        self._decorated = query
        self._decorators = decorators

    def render(self):
        current_result = self._decorated.render()
        for deco in self._decorators:
            current_result = deco(current_result)

        return current_result


def remove_empty():
    return ""


def case_insensitive():
    return ""


if __name__ == '__main__':
    query = DictQuery(
        foo="bar",
        empty="",
        none=None,
        upper="UPPERCASE",
        title="Title"
    )

    query = QueryEnhancer(query, remove_empty, case_insensitive).render()


