import functools
import logging
import time

logger = logging.getLogger()


def traced_function_wrong(function):

    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        logger.info(f"{function} 함수 실행", function)

        result = function(*args, **kwargs)
        logger.info("함수 %s 의 실행 시간: %.2f", function, time.time() - start_time)
        return result
    return wrapped


@traced_function_wrong
def process_with_delay(callback, delay=0):
    time.sleep(delay)
    return callback()



