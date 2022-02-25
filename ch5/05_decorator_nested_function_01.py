import logging
from functools import wraps

RETRIES_LIMIT = 3


class ControlledException:
    """
    도메인 예외
    """


def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
    allowed_exceptions = allowed_exceptions or (ControlledException,)

    def retry(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(retries_limit):
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    logging.getLogger().info("retrying %s due to %s", operation, e)
                    last_raised = e

            raise last_raised
        return wrapped
    return retry
