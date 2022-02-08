def data_from_response(response:dict) -> dict:
    """
    response 에 문제가 없다면 response 의 payload 를 반환
    :param response:
    :return: dict
    - response 값의 예제
    {
        "status": 200,
        "timestamp": "..."
        "payload": {...}
    }

    - 리턴 사전값의 예제
    {"data": { ... }}

    - 발생 가능한 예외:
    - HTTP status 가 200 이 아닌 경우 ValueError 발생
    """
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}
