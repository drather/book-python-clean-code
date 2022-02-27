import logging


def trace_decorator(function):
    def wrapped(*args, **kwargs):
        logging.getLogger().info("%s 실행", function.__qualname__)
        return function(*args, **kwargs)

    return wrapped


@trace_decorator
def process_account(account_id):
    logging.getLogger().info("%s 계정 처리", account_id)


if __name__ == '__main__':
    help(process_account)