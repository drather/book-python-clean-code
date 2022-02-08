import os


def run(cmd):
    os.system(cmd)


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()


def db_backup():
    run("pg_dump database")


def main():
    with DBHandler():
        db_backup()