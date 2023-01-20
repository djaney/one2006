import os


AUTHOR = 'Zen Mabelin'
SITENAME = 'One 2006'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False

THEME = os.path.join(os.path.dirname(__file__), 'themes/one2006')

PLUGINS = ['plugins.members']

STATIC_PATHS = ['extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True