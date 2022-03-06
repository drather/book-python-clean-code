class GitFetcher:
    _current_tag = None

    def __init__(self, tag):
        self.current_tag = tag

    @property
    def current_tag(self):
        if self._current_tag is None:
            raise AttributeError("값이 초기화 되지 않음")

        return self._current_tag

    @current_tag.setter
    def current_tag(self, new_tag):
        self.__class__._current_tag = new_tag

    def pull(self):
        print(f"{self.current_tag} 에서 풀")
        return self.current_tag


if __name__ == '__main__':
    f1 = GitFetcher(0.1)
    f2 = GitFetcher(0.2)
    f1.current_tag = 0.3

    print(f2.pull())

    print(f1.pull())

