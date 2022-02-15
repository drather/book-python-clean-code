configuration = {"dbport": 5432}

print(f"configuration['dbhost']: {configuration.get('dbhost', 'localhost')}")

print(f"configuration['dbport']: {configuration.get('dbport')}")