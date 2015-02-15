"""
File with commands and supported databases by dumpyme
"""


# Dict with types and commands to create dumps
# {0} - database name
# {1} - folder with dump
dump_commands = {
    "mongodb": "mongodump --db {0} --out {1}",
}

# const with list of supported database types
SUPPORTED = dump_commands.keys()
