#!/usr/bin/env python
from flask_script import Manager
from application import app
from flask_migrate import Migrate, MigrateCommand
from models import db

manager =  Manager(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    manager.add_command('db', MigrateCommand)
    manager.run()
