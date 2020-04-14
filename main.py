import logging
from logging.config import fileConfig
from pathlib import Path
import src.parser

####################################################################################################
def init_logger():
    log_config_path = Path(__file__).parent / 'logging_config.ini'
    logging.config.fileConfig(log_config_path.absolute())

####################################################################################################
def main():
    init_logger()
    LOG = logging.getLogger()
    
    parser = src.parser.get_argparser()
    args = parser.parse_args()
    print(args.target_dir)

    LOG.info("Script Start")
    return

####################################################################################################
if __name__ == "__main__":
    main()