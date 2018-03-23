import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):  # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'mybase.db')
    print (SQLALCHEMY_DATABASE_URI)

#    SQLALCHEMY_DATABASE_URI = '/Users/askhat/projects/sysadminjob/crowler/mybase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
