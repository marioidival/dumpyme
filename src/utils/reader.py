try:
    import ConfigParser as configparser
except ImportError:
    import configparser

from .config import DumpyConfig

class DumpyReader(object):

    def __init__(self):
        self.dumpyfile = DumpyConfig.verify_dumpy_file()
        self.configp = configparser.ConfigParser()
        self.expected_keys = ['project', 'host', 'user', 'db', 'db_name']

    def add_section_project(self, **infos):
        """Add new project with infos in dumpyfile"""
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
        """Remove project from dumpyfile"""
        self.configp.read(self.dumpyfile)

        result = self.configp.remove_section(project)

        if result:
            with open(self.dumpyfile, 'w') as dumpyfile:
                self.configp.write(dumpyfile)

            return result

    def section_infos(self, project):
        """Return informations of project from dumpyfile"""
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
