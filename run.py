"""Running the xetra etl application"""
import logging
import logging.config

import yaml


def main():
    """
    entry point to run the xetra etl job"""
    general_path = 'C://development//xetra_project//xetra-stock-data//config//'
    config_path = general_path+"xetra_report1_config.yml"
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    print(config)
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("this is a test.")


if __name__ == '__main__':
    main()
