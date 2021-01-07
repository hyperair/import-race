import logging
import random
import threading
import traceback
import time

logger = logging.getLogger(__name__)


def foo(): ...
time.sleep(random.random())
def bar(): ...
def baz(): ...
def asdf(): ...

def list_globals():
    return list(globals())


def run_loop():
    logger.info("before loop: %s", list_globals())
    try:
        for x in globals():
            logger.info("in loop before sleep: %s", list_globals())
            time.sleep(random.random())
            logger.info("in loop after sleep: %s", list_globals())
    except Exception as e:
        logger.exception("caught exception: %s", list_globals())


run_loop()
