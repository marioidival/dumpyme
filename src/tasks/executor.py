from fabric.api import env, execute, run, cd, settings, get

from ..utils.reader import DumpyReader
from ..utils.supported_databases import dump_commands


class DumpyExecutor(object):

    def __init__(self, project):
        dumpreader = DumpyReader()
        self.project_data = dumpreader.section_infos(project)
        self.local_info = dumpreader.section_infos('local_info')

    def dump_command(self, db_type, database, dumpy_folder):
        """Format dump command of project"""
        command = dump_commands[db_type]
        command = command.format(database, dumpy_folder)
        gzip_command = "gzip > {}.gz".format(dumpy_folder)

        return "{} | {}".format(command, gzip_command)

    def task_runner(self):
        """Execute task to user"""
        database = self.project_data["db"]
        db_type = self.project_data["db_name"]
        dump_folder = 'dumpy_{}'.format(database)
        gzip_dump_folder = 'dumpy_{}.gz'.format(database)

        host_string = "{}@{}".format(
            self.project_data['user'],
            self.project_data['host']
        )
        with settings(host_string=host_string):
            with cd("/tmp"):
                # Make dump
                run(self.dump_command(db_type, database, dump_folder))
                # Copy to user directory
                get(gzip_dump_folder, self.local_info['dump_location'])

    def run(self):
        """Execute fabric task"""
        execute(self.task_runner)
