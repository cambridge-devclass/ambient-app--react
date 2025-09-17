It seems we decided to go with Python and MySQL for this project: https://discord.com/channels/1250951867891187813/1404210601613328457

For DB schema changes, I suggest storing SQL in /migrations and run them with Python script. Will make an example for https://github.com/cambridge-devclass/ambient-app--react/issues/1

Sqlite setup (temporary):
The application can be run using sqlite for the database. This makes the setup process a little easier, because sqlite is built-in to python. 
To create a local sqlite database file in this directory, run the \_sqilite-setup.py script: `python _sqlite-setup.py`
This should create a "local.db" file, which the server will use as long as it retrieves DB\_URL from config/sqlite.py. 

A GUI database client is generally useful for backend development, it makes it easy to look up or change records/schema for debugging or prototyping.
HeidiSQL is pretty good but there are many alternatives. Here are some that support sqlite:
https://heidisql.com
https://dbeaver.io
https://sqlitebrowser.org
