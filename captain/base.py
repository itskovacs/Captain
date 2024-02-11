from abc import ABC, abstractmethod
import time
from .utils.formatter import logger


class Base(ABC):
    NAME = "Base Agent"
    ACTIVATED = False
    VERSION = "0.0"
    MISSION = "No description"

    def __init__(self, args):
        ...

    @abstractmethod
    def mission(self) -> tuple:
        """Do not touch this. This function will be used in every agent to program their mission"""
        ...

    def run(self):
        """Run agent, describing a pattern of started - accomplished - done"""
        start_time = time.time()
        logger.debug(f"[{self.NAME}] Started.")

        try:  # Completed if no error is encountered
            stdout = self.mission()
            logger.debug(f"[{self.NAME}] Results:")
            print(stdout)

        except Exception as e:  # Completed if error is encountered
            logger.error(f"[{self.NAME}] Error encountered: {e.args} {e.with_traceback}")

        finally:  # Completed no matter what
            logger.debug(f"[{self.NAME}] Completed in {time.time() - start_time}s.")
