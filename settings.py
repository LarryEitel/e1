# -*- coding: utf-8 -*-
import sys
import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# for evernote and thrift
sys.path.append(os.path.join(PROJECT_ROOT, "parts"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

# django-compressor is turned off by default due to deployment overhead for
# most users. See <URL> for more information
COMPRESS = False

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "mongo", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "ex-dev",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# couldn't get this to work
# CAFE_ROOT = os.path.join(PROJECT_ROOT, "static", "js")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media"
DEBUG_TOOLBAR_MEDIA_URL = MEDIA_URL

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Subdirectory of COMPRESS_ROOT to store the cached media files in
COMPRESS_OUTPUT_DIR = "cache"

# Make this unique, and don't share it with anybody.
SECRET_KEY = "t#alp6mgus%3q6#zjpmj!ejqx+f*hzh(m+)kx&e_x!j7pjc-#*"

ROOT_URLCONF = "ourfield.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = ""

EMAIL_BACKEND = "mailer.backend.DbBackend"

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

AUTHENTICATION_BACKENDS = [
    "",
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "what_next"
LOGOUT_REDIRECT_URLNAME = "home"

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass

