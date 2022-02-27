import logging
from functools import wraps

RETRIES_LIMIT = 3


class ControlledException:
    """
    도메인 예외
    """


class WithRetry:
    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exception=None):
        self.retries_limit = retries_limit
        self.allowed_exception = allowed_exception or (ControlledException,)

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exception as e:
                    logging.getLogger().info("retrying %s due to %s", operation, e)
                    last_raised = e
                raise last_raised

        return wrapped


@WithRetry(retries_limit=5)
def run_with_custom_retries_limit(task):
    return task.run()
