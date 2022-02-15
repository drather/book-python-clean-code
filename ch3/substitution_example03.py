def connect_db(host="localhost", port=5432):
    print(f"다음 정보로 DB 접속, {host}, {port}")


if __name__ == '__main__':
    connect_db()

    connect_db('testdb', '8000')