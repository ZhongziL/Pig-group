from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Role, Permission, Follow, Comment, Post
from flask_uploads import configure_uploads, patch_request_class
from app.auth.views import icon
from flask_moment import Moment

app = create_app('development')

configure_uploads(app, icon)
patch_request_class(app, 102400)

moment = Moment(app)
manager = Manager(app)
migrate = Migrate(app, db)

'''add command python manage.py shell'''
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission,
                Follow=Follow, Comment=Comment, Post=Post)

manager.add_command('shell', Shell(make_context=make_shell_context))

'''add command python manage.py db ..'''
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
