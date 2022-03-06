class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query


class QueryEnhancer:
    def __init__(self, query: DictQuery):
        self.decorated = query

    def render(self):
        return self.decorated.render()


class RemoveEmpty(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v for k, v in original.items() if v}


class CaseInsensitive(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v.lower() for k, v in original.items() if v}


if __name__ == '__main__':
    original = DictQuery(key="value", empty="", none=None, upper="UPPERCASE", title="Title")

    new_query = CaseInsensitive(RemoveEmpty(original))

    print(original.render())
    print(new_query.render())

