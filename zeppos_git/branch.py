import git
from zeppos_root.root import Root
from zeppos_logging.app_logger import AppLogger
from cachetools import cached, TTLCache

class Branch:
    @staticmethod
    @cached(cache=TTLCache(maxsize=1024, ttl=600))
    def get_current():
        g = git.cmd.Git(Root.find_root_of_project(__file__))
        for line in g.branch().split('\n'):
            if line.startswith("*"):
                AppLogger.logger.debug(f"Current Git Branch: {line[1:].strip()}")
                return line[1:].strip()
        return None
