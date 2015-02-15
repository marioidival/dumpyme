import os
import shutil


class DumpyConfig(object):
    """Handler configuration of dumpyme."""

    def __init__(self):
        # Path to file or False
        self.dumpy_file = self.verify_dumpy_file()

    @classmethod
    def verify_dumpy_file(cls):
        """Verify if exists dumpy file in home directory.

        Return path to file or False.
        """
        home_dir = os.path.expanduser("~")
        file_exist = os.path.exists(os.path.join(home_dir, ".dumpyme.ini"))

        if file_exist:
            return os.path.join(home_dir, ".dumpyme.ini")

        return file_exist

    def move_config_file(self, default_file):
        """Move default dumpyfile to user home.
        path/str default_file:
            templates/tmp_dumpyme.ini

        If dumpyfile already exists, return False. If not, move it and return
        True.
        """
        if self.dumpy_file:
            return False

        shutil.copy(default_file, os.path.expanduser("~") + "/.dumpyme.ini")
        return True

    def dumpylocation(self, dumpy_local):
        """Create or return dumpylocation.

        path/str dumpy_local:
            path to home directory

        If dumpy_local already exists, return it. If not, create and return it.
        """
        if not os.path.exists(dumpy_local):
            os.makedirs(dumpy_local)

        return dumpy_local
