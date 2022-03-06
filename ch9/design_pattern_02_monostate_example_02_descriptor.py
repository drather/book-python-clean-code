class SharedAttribute:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self._name = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.value is None:
            raise AttributeError(f"{self._name} was never set")
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __set_name__(self, owner, name):
        self_name = name


class GitFetcher:
    current_tag = SharedAttribute()
    current_branch = SharedAttribute()

    def __init__(self, tag, branch=None):
        self.current_tag = tag
        self.current_branch = branch

    def pull(self):
        print(f"{self.current_tag} 에서 풀")
        return self.current_tag


if __name__ == '__main__':
    f1 = GitFetcher(0.1)
    f2 = GitFetcher(0.2)
    f1.current_tag = 0.3

    print(f2.pull())

    print(f1.pull())

