#  set path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from application import create_app, db
from team import models
from person import models

app = create_app(os.getenv('APP_SETTINGS') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)

# Turn on reloader
manager.add_command('runserver', Server(
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 5000))
))

# Migrations
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
