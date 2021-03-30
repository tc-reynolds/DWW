import logging

class LoggerFactory:
    @staticmethod
    def build_logger(name, log_location):
        # Builds logger object for whatever state you are crawling
        # With convention ; Florida_Chem_logger as the unique name.
        logger_name = name + '_logger'
        handler = build_log_handler(log_location)
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger


def build_log_handler(log_location):
    #Handles log formatting and timestamping
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_location, mode='w')
    handler.setFormatter(formatter)
    return handler


