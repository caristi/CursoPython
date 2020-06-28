import logging

logger = logging
logger.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s ',
                   datefmt='%m/%d/%Y %I:%M %p',
                   handlers=[logging.FileHandler('archvivoErro.log'),
                             logging.StreamHandler()
                            ]
                   )