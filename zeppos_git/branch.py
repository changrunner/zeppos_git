import git
from zeppos_root.root import Root
from zeppos_logging.app_logger import AppLogger


class Branch:
    @staticmethod
    def get_current():
        g = git.cmd.Git(Root.find_root_of_project(__file__))
        for line in g.branch().split('\n'):
            if line.startswith("*"):
                AppLogger.logger.info(f"Current Git Branch: {line[1:].strip()}")
                return line[1:].strip()
        return None
