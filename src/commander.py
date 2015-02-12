import os
import click

from utils.config import DumpyConfig


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
            click.echo("dumpyfile in your home directory as .dumpyfile.ini")
        else:
            click.echo("dumpyfile already exists")

@dumpy.command()
@click.argument("project")
def add(project):
    """Add new project in dumpfile"""
    click.echo("add {}".format(project))

@dumpy.command()
@click.argument("project")
def delete(project):
    """Delete project of dumpfile"""
    click.echo("delete {}".format(project))

@dumpy.command()
@click.argument("project")
def me(project):
    """Get dumps of project"""
    click.echo("me {}".format(project))
