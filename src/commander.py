import os
import click

from utils.config import DumpyConfig
from utils.reader import DumpyReader
from utils.supported_databases import SUPPORTED
from tasks.executor import DumpyExecutor


@click.group()
def dumpy():
    """Command Line package to get dumps of database"""


@dumpy.command()
def init():
    """Create dumpyfile and move to home directory.
       `dumpyfile` is configuration file of dumpyme, there exists informations
       of projects like host, user, database to get dump, database types
       (mongodb, postgresql).
    """
    if init:
        dumpy_conf = DumpyConfig()
        we_file = os.path.join(os.path.dirname(__file__),
                               'templates/tmp_dumpyme.ini')
        result = dumpy_conf.move_config_file(we_file)

        dumpy_reader = DumpyReader()
        default_dir = os.path.expanduser("~") + "/dumpys/"
        dumpy_reader.update_infos('local_info', 'dump_location', default_dir)

        if result:
            click.echo("Creating dumpyfile...")
            click.echo("dumpyfile in your home directory as ~/.dumpyfile.ini")
        else:
            click.echo("dumpyfile already exists in home directory")


@dumpy.command()
@click.option("--project", prompt="Project name")
@click.option("--host", prompt="Host of project")
@click.option("--user", prompt="User of host")
@click.option("--db", prompt="Name of db")
@click.option("--db_name", prompt="DB Type (e.g: mongodb, postgresql...)",
              type=click.Choice(SUPPORTED))
def add(project, host, user, db, db_name):
    """ Add new project in dumpfile.
    If you want, you can add manually in ~/.dumpyfile.ini.

       [project_name]

        host = host_to_project

        user = user_of_host

        db = database_name

        db_name = database_type (e.g: mongodb, postgresql...)

    """
    dumpy_reader = DumpyReader()
    if dumpy_reader.dumpyfile:
        result = dumpy_reader.add_section_project(
            project=project, host=host, user=user, db=db, db_name=db_name
        )
        if result:
            click.echo("Adding in dumpyfile:")
            click.echo("\tProject: {}".format(project))
            click.echo("\tHost: {}".format(host))
            click.echo("\tDatabase: {}".format(db))
            click.echo("\tDatabase Type: {}".format(db_name))
        # Error message


@dumpy.command()
@click.argument("project")
def delete(project):
    """Delete project of dumpfile"""
    dumpy_reader = DumpyReader()
    if dumpy_reader.dumpyfile:
        result = dumpy_reader.remove_section_project(project)

        if result:
            click.echo("Project removed sucessfully")


@dumpy.command()
@click.argument("project")
def me(project):
    """Get dump database of project"""
    executor = DumpyExecutor(project)
    executor.run()
