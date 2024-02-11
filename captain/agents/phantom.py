from ..base import Base, logger


class PhantomAgent(Base):
    NAME = "Phantom"
    ACTIVATED = True
    VERSION = "1.0"
    MISSION = "No description"

    def mission(self):
        logger.info(f'[{self.NAME}] Checking in.')
        return self.NAME
