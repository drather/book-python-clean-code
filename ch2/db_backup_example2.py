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


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


with db_handler():
    db_backup()
