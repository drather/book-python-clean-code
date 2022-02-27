import functools
import logging
import time

logger = logging.getLogger()


def traced_function_wrong(function):
    logger.info(f"{function} 함수 실행", function)

    start_time = time.time()

    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        result = function(*args, **kwargs)
        logger.info("함수 %s 의 실행 시간: %.2f", function, time.time() - start_time)
        return result
    return wrapped


@traced_function_wrong
def process_with_delay(callback, delay=0):
    time.sleep(delay)
    return callback()



