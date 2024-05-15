import logging

def setup_logger(logger_name, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='[%H:%M:%S]')

    #file_handler = logging.FileHandler(log_file, mode='w')
    #file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    l.setLevel(level)
    #l.addHandler(file_handler)
    l.addHandler(stream_handler)

    return l