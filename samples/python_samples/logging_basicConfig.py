import logging

# logging using basicConfig() instead of getLogger() 
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s %(levelname)s: %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S')

logging.error("foo")