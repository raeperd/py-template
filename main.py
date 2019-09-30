import logging
from logging.config import fileConfig
from pathlib import Path


def main():
    init_logger()
    LOG = logging.getLogger()
    LOG.info("Script Start")
    
    return

def init_logger():
    log_config_path = Path(__file__).parent / 'logging_config.ini'
    logging.config.fileConfig(log_config_path.absolute())

if __name__ == "__main__":
    main()