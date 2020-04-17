import logging
from logging.config import fileConfig
from pathlib import Path

from src.argument_parser import get_argparser
from src.percentage_checker import PercentChecker
####################################################################################################
def init():
    init_logger()
    argparser =  get_argparser()
    return argparser.parse_args()

def init_logger():
    log_config_path = Path(__file__).parent / 'logging_config.ini'
    logging.config.fileConfig(log_config_path.absolute())

####################################################################################################
def main():
    args = init()
    LOG = logging.getLogger()
    LOG.info(f"{args.target_file} is passed by commandline argument")

    percent = PercentChecker(len('123456'))
    LOG.info(f"[{percent.increased_percent()}]")
    return

####################################################################################################
if __name__ == "__main__":
    main()