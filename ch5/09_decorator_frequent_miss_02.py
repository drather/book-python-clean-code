import logging
from functools import wraps


def trace_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logging.getLogger().info("%s 실행", function.__qualname__)
        return function(*args, **kwargs)

    return wrapped


@trace_decorator
def process_account(account_id):
    """
    id 별 계정 처리
    :param account_id:
    :return:
    """
    logging.getLogger().info("%s 계정 처리", account_id)


if __name__ == '__main__':
    help(process_account)

    print(process_account.__qualname__)