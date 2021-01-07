import logging
import threading


logging.basicConfig(
    format="[%(asctime)s] %(threadName)10s: %(message)s",
    level='INFO'
)

logger = logging.getLogger(__name__)


def import_slow_module():
    logger.info("before import")
    import slow_module
    logger.info("after import")


threads = [threading.Thread(target=import_slow_module) for _ in range(10)]
for t in threads:
    t.start()

for t in threads:
    try:
        t.join()
    except Exception:
        pass
