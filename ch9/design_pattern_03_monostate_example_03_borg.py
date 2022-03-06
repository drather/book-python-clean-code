class BaseFetcher:
    def __init__(self, source):
        self.source = source


class TagFetcher(BaseFetcher):
    _attributes = {}

    def __init__(self, source):
        self.__dict__ = self.__class__._attributes
        super().__init__(source)

    def pull(self):
        print(f"{self.source} 태그에서 풀")
        return f"Tag = {self.source}"


class BranchFetcher(BaseFetcher):
    _attributes = {}

    def __init__(self, source):
        self.__dict__ = self.__class__._attributes
        super().__init__(source)

    def pull(self):
        print(f"{self.source} 브랜치에서 풀")
        return f"Branch = {self.source}"


