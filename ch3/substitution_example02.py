import os

print(os.getenv("DBHOST", "localhost"))
print(os.getenv("DBPORT", "5432"))
