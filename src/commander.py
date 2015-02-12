import os
import click

from utils.config import DumpyConfig
from utils.reader import DumpyReader


@click.group()
def dumpy():
    """Command Line package to get dumps"""

@dumpy.command()
def init():
    """Create dumpfile to user"""
    if init:
        dumpy_conf = DumpyConfig()
        we_file = os.path.join(os.path.dirname(__file__),
                               'templates/tmp_dumpyme.ini')
        result = dumpy_conf.move_config_file(we_file)
        if result:
            click.echo("dumpyfile in your home directory as ~/.dumpyfile.ini")
        else:
            click.echo("dumpyfile already exists in home directory")

@dumpy.command()
@click.option("--project", prompt="Project name")
@click.option("--host", prompt="Host of project")
@click.option("--user", prompt="User of host")
@click.option("--db", prompt="Name of db")
@click.option("--db_name", prompt="DB Type (e.g: mongodb, postgresql...)")
def add(project, host, user, db, db_name):
    """Add new project in dumpfile"""
    dumpy_reader = DumpyReader()
    if dumpy_reader.dumpyfile:
        result = dumpy_reader.add_section_project(
            project=project, host=host, user=user, db=db, db_name=db_name
        )
        if result:
            click.echo("adding in dumpyfile")
            click.echo("Project: {}".format(project))
            click.echo("Host: {}".format(host))
            click.echo("Database: {}".format(db))
            click.echo("Database Type: {}".format(db_name))
        # Error message


@dumpy.command()
@click.option("--project", prompt="Project name")
def delete(project):
    """Delete project of dumpfile"""
    click.echo("delete {}".format(project))

@dumpy.command()
@click.argument("project")
def me(project):
    """Get dumps of project"""
