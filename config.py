import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

from os import urandom, environ

from app.utils import str_to_bool

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

# Application root prefix, e.g. "/app/cms"
APPLICATION_ROOT = environ["APPLICATION_ROOT"] if "APPLICATION_ROOT" in environ else "/"

# don't track modifications
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Your App secret key
# SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"
SECRET_KEY = urandom(32)

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = "OSGS"

# Uncomment to setup Setup an App icon
APP_ICON = "/static/osgs.svg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = "Admin"

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = "Public"

# Will allow user self registration
AUTH_USER_REGISTRATION = (
    str_to_bool(environ["AUTH_USER_REGISTRATION"])
    if "AUTH_USER_REGISTRATION" in environ
    else False
)

if AUTH_USER_REGISTRATION:
    RECAPTCHA_USE_SSL = (
        str_to_bool(environ["RECAPTCHA_USE_SSL"])
        if "RECAPTCHA_USE_SSL" in environ
        else False
    )
    RECAPTCHA_PUBLIC_KEY = environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = environ["RECAPTCHA_PRIVATE_KEY"]
    RECAPTCHA_OPTIONS = {"theme": "white"}
    MAIL_SERVER = environ["MAIL_SERVER"]
    MAIL_USE_TLS = (
        str_to_bool(environ["MAIL_USE_TLS"]) if "MAIL_USE_TLS" in environ else True
    )
    MAIL_USERNAME = environ["MAIL_USERNAME"]
    MAIL_PASSWORD = environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER = environ["MAIL_DEFAULT_SENDER"]

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "ReadOnly"

FAB_ROLES = {
    "ReadOnly": [
        [".*", "can_list"],
        [".*", "can_show"],
        [".*", "menu_access"],
        [".*", "can_get"],
        [".*", "can_info"],
    ],
    "ReadWrite": [
        [".*", "can_list"],
        [".*", "can_show"],
        [".*", "can_edit"],
        [".*", "can_delete"],
        [".*", "can_download"],
        [".*", "menu_access"],
        [".*", "can_get"],
        [".*", "can_put"],
        [".*", "can_post"],
        [".*", "can_delete"],
        [".*", "can_info"],
    ],
}

FAB_ROLES_MAPPING = {1: "ReadOnly", 2: "ReadWrite"}

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Português"},
}
# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/media/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/media/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/media/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
APP_THEME = "flatly.css"
# APP_THEME = "darkly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"
