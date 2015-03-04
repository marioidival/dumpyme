# Dumpy Me

Command line package to get dumps of databases


## Install

    pip install dumpyme

## Usage

### 1 - Create dumpyfile

    dumpy init
	Creating dumpyfile...
	dumpyfile in your home directory as ~/.dumpyfile.ini

##### Initial dumpyfile:
    [local_info]
    dump_location = /Users/marioidival/dumpys/

    [my_project]
    host = 187.111.44.100
    db_name = mongodb
    db = my_project_db
    user = root

    [my_project2]
    host = 192.191.190.89
    db_name = mongodb
    db = my_project2_db
    user = my_root

##### help:
    Usage: dumpy init [OPTIONS]

      Create dumpyfile and move to home directory. `dumpyfile` is configuration
      file of dumpyme, there exists informations of projects like host, user,
      database to get dump, database types (mongodb, postgresql).

    Options:
      --help  Show this message and exit.

### 2 - Add some project in dumpyfile

    dumpy add
	Project name: my_project
	Host of project: 187.111.44.100
	User of host: root
	Name of database: my_project_db
	Database Type (e.g: mongodb, postgresql...): mongodb

	Adding in dumpyfile:
			Project: my_project
			Host: 187.111.44.100
			Database: my_project_db
			Database Type: mongodb

##### help:
    Usage: dumpy add [OPTIONS]

      Add new project in dumpfile. If you want, you can add manually in
      ~/.dumpyfile.ini.

      [project_name]
      host = host_to_project
      user = user_of_host
      db = database_type (e.g: mongodb, postgresql...)
      db_name = database_name

    Options:
      --project TEXT
      --host TEXT
      --user TEXT
      --db_name TEXT
      --db [mongodb]
      --help          Show this message and exit.

### 3 - List projects in dumpyfile

	dumpy projects
	Projects:
	========================================
	-------> my_project
					host: 187.111.44.100
					db_name: my_project_db
					db mongodb
					user: root
	-------> my_project2
					host: 192.191.190.89
					db_name: my_project2_db
					db: mongodb
					user: my_root
	-------> project2
					host: 182.182.82.82
					db_name: project2_production
					db: mongodb
					user: riit
	========================================

or list name of projects:

	dumpy projects --name
	Projects:
	========================================
			my_project
			my_project2
			project2
	========================================

##### help:
    Usage: dumpy projects [OPTIONS]

      List informations of projects in dumpyfile

    Options:
      --name  Show only name of projects
      --help  Show this message and exit.

### 4 - Get dump of project

    dumpy me my_project

##### help:
    Usage: dumpy me [OPTIONS] PROJECT

      Get dump database of project

    Options:
      --help  Show this message and exit.

### 5 - Delete projects in dumpyfile

	dumpy delete my_project
	Project removed sucessfully

#### help:
    Usage: dumpy delete [OPTIONS] PROJECT

      Delete project of dumpfile

    Options:
      --help  Show this message and exit.

### Databases supported
* MongoDB
