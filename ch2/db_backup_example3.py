import contextlib
import os


def run(cmd):
    os.system(cmd)


def db_backup():
    run("pg_dump database")


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandlerDecorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()


@DBHandlerDecorator()
def offline_backup():
    run("pg_dump database")
