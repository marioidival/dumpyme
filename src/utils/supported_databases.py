"""
File with commands and supported databases by dumpyme
"""


# Dict with types and commands to create dumps
# {0} - database name
# {1} - folder with dump
dump_commands = {
    "mongodb": "mongodump --db {0} --out {1}",
}

"""
POSTGRESQL : pg_dump -d database -U user/owner > file.sql
    variações:
        --table=nome_da_tabela
        --table=nome_da_tabela --table=nome_da_outra_tabela

        --exclude=nome_da_tabela
        --exclude=nome_da_tabela --exclude=nome_da_outra_tabela
"""

# const with list of supported database types
SUPPORTED = dump_commands.keys()
