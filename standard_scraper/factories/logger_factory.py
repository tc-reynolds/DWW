import logging
import constants

def build_log_handler(log_location):
    #Handles log formatting and timestamping
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_location, mode='w')
    handler.setFormatter(formatter)
    return handler

def build_logger(state, log_location, type):
    # Builds logger object for whatever state you are crawling
    # With convention ; Florida_Chem_logger as the unique name.
    logger_name = state + '_' + type + '_logger'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(build_log_handler(log_location))
    return logger

def build_master_logger():
    logger = logging.getLogger('master_logger')
    logger.setLevel(logging.INFO)
    logger.addHandler(build_log_handler(constants.MASTER_LOG))
    return logger