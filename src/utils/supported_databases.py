"""
File with commands and supported databases by dumpyme
"""


dump_commands = {
    "mongodb": "mongodump --db {0} --out {1}",
}

SUPPORTED = dump_commands.keys()
