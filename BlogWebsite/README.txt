# ./blogwebsite/Scripts/activate


As of Flask-SQLAIchemy 3.0, all access to db. engine (and db. Session) requires an active Flask application context.
db.create_all uses db. engine, so it requires an app context.

with app.app_context():
db.create_all()

When Flask handles requests or runs CLI commands, a context is automatically pushed. You only need to push one manually
outside of those situations, such as while setting up the app.

Instead of calling create_al1 in your code, you can also call it manually in the shell. Use flask shel to start a Python
shell that already has an app context and the db object imported.

$ flask shell
>>> db.create_all()

Or push a context manually if using a plain python shell.

$ python

>>> from project import app, db
>>> app.app_context().push()
>>> db.create_all() a
