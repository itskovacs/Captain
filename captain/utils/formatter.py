import logging
from colorama import Fore, Style


class ColorFormatter(logging.Formatter):
    """Custom color Formatter for logging"""
    LOG_COLORS = {
        logging.DEBUG: Fore.GREEN,
        logging.INFO: Fore.BLUE,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED
    }

    def format(self, record, *args, **kwargs):
        color = self.LOG_COLORS.get(record.levelno)
        record.levelname = f"{color}{record.levelname:>8s}{Style.RESET_ALL}"
        return super().format(record, *args, **kwargs)


logger = logging.getLogger("captain")
LOG_HANDLER = logging.StreamHandler()
LOG_HANDLER.setFormatter(ColorFormatter(fmt="%(asctime)s %(levelname)s %(message)s",
                                        datefmt=f"{Style.DIM}[%H:%M:%S]{Style.RESET_ALL}"))
logger.setLevel(logging.INFO)
logger.addHandler(LOG_HANDLER)
