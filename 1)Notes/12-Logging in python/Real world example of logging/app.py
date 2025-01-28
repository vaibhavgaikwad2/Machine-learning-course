import logging




## configure logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


# StreamHAndler --> it is resonsible to put all information inside this app1.log file
 

logger=logging.getLogger("ArithmaticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b}={result}")
    return result


add(10,5)