## Dependencies

- flask - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
- flask sqlalchemy - flask wrapper for Sqlalchemy, it adds Sqlalchemy support to flask apps
- psycopg2 - python postgresql adapter that provides some commands for simple CRUD queries and more on postgresql db
- flask-migrate - flask extension that handles SQLAlchemy database migration. Migration basically refers to the management of incremental, reversible changes to relational database schemas
- flask-script - provides an extension for managing external scripts in flask. This is needed in running our db migrations from the command line
- marshmallow - marshmallow is a library for converting complex datatypes to and from native Python datatypes. Simply put it is used for deserialization(converting data to application object) and serialization(converting application object to simple types).
- flask-bcrypt - we'll use this to hash our password before saving it in the db - of course, you don't want to save user's password directly into your db without hashing it
- pyjwt - python library to encode and decode JSON Web Tokens used in verifying user's authenticity