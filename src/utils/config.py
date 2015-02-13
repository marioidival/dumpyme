import os
import shutil


class DumpyConfig(object):

    def __init__(self):
        self.dumpy_file = self.verify_dumpy_file()

    @classmethod
    def verify_dumpy_file(cls):
        """Verify if exists dumpy file in home user """
        home_dir = os.path.expanduser("~")
        file_exist = os.path.exists(os.path.join(home_dir, ".dumpyme.ini"))

        if file_exist:
            return os.path.join(home_dir, ".dumpyme.ini")

        return file_exist

    def move_config_file(self, default_file):
        """Move default dumpy file to user home"""
        if self.dumpy_file:
            return False

        shutil.copy(default_file, os.path.expanduser("~") + "/.dumpyme.ini")
        return True

    def dumpylocation(self, dumpy_local):
        """Create or return dumpylocation"""
        if not os.path.exists(dumpy_local):
            os.makedirs(dumpy_local)

        return dumpy_local
