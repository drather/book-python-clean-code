class InternalDataError(Exception):
    """
    업무 도메인 데이터 예외
    """


def process(data_dictionary, record_id):
    try:
        return data_dictionary[record_id]

    except KeyError as e:
        raise InternalDataError("해당 기록이 없습니다") from e


if __name__ == '__main__':
    my_dict = dict()
    process(my_dict, 'a')

