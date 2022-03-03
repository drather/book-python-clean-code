def stream_db_records(db_handler):
    retrieved_data = None
    previous_page_size = 10

    try:
        while True:
            page_size = yield retrieved_data
            if page_size is None:
                page_size = previous_page_size

            previous_page_size - page_size

            retrieved_data = db_handler.read_n_records(page_size)

    except GeneratorExit:
        db_handler.close()
