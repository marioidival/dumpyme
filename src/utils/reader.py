import os

try: # python 3
    import ConfigParser as configparser
except ImportError:
    import configparser

from .config import DumpyConfig


class DumpyReader(object):
    """Handler to configuration file of dumpyme."""

    def __init__(self):
        # Path to file or False
        self.dumpyfile = DumpyConfig.verify_dumpy_file()
        self.configp = configparser.SafeConfigParser()
        self.expected_keys = ['project', 'host', 'user', 'db', 'db_name']

    def add_section_project(self, **infos):
        """Add new project with infos in dumpyfile.
        dict infos:
            project = name of project
            host = host of project
            db = name of database
            db_name = database type (mongodb, postgresql)

        Write new project/section and arguments with values in configuration
        file.
        return True if success.
        """
        for exp_k in self.expected_keys:
            if exp_k not in infos:
                return False

        psection = infos["project"]
        del infos["project"]

        self.configp.add_section(psection)

        for key, val in infos.items():
            self.configp.set(psection, key, val)

        with open(self.dumpyfile, 'a') as dumpyfile:
            self.configp.write(dumpyfile)

        return True

    def remove_section_project(self, project):
        """Remove project from dumpyfile.
        Remove from configuration file project/section passed by command line.

        str project:
            name of project/section in dumpyfile

        return True if success.
        """
        self.configp.read(self.dumpyfile)

        result = self.configp.remove_section(project)

        if result:
            with open(self.dumpyfile, 'w') as dumpyfile:
                self.configp.write(dumpyfile)

            return result

    def section_infos(self, project):
        """Return informations of project from dumpyfile.
        str project:
            name of project/section in dumpyfile

        return dict dsection
        """
        dsection = {}
        config = self.configp.read(self.dumpyfile)
        infos = self.configp.options(project)

        for info in infos:
            try:
                dsection[info] = self.configp.get(project, info)
                if dsection[info] == -1:
                    pass
            except:
                dsection[info] = None

        return dsection

    def update_infos(self, project, infor, newvalue):
        """Update values of information in specific project/section in
        configuration file.

        project:
            name of project/section in config file
        infor:
            key in specific project/section
        newvalue:
            new value to infor

        """
        self.configp.read(self.dumpyfile)

        self.configp.set(project, infor, newvalue)

        with open(self.dumpyfile, 'w+') as dumpyfile:
            self.configp.write(dumpyfile)
