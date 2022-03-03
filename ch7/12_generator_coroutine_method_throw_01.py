class CustomException(Exception):
    pass


def stream_data(db_handler):
    while True:
        try:
            yield db_handler.read_n_records(1)
        except CustomException as e:
            print("처리 가능한 에러, 계속 진행")

        except Exception as e:
            print("처리할 수 없는 에러, 중단")
            db_handler.close()
            break