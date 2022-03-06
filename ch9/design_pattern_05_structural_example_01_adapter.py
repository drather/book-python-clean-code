class UsernameLookup:
    @staticmethod
    def search(self, user_namespace):
        print("base_function")


class UserSource(UsernameLookup):
    def fetch(self, user_id, username):
        user_namespace = self._adapt_arguments(user_id, username)
        return self.search(user_namespace)

    @staticmethod
    def _adapt_arguments(user_id, username):
        return f"{user_id}: {username}"

