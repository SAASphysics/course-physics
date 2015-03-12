#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"TODOCourse Name on Header"
SITEURL = 'TODOhttp://full/url/toserver'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'betnelcourses'
COMMENTS_INTRO = "Is something unclear? Leave a comment below:"

DOCUTIL_CSS = True
DISPLAY_PAGES_ON_MENU = True


DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATHS = ['../../../pelican-plugins'] 
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican_vimeo', 'tipue_search', 'pelican_youtube', 'sitemap', 'latex']

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITEMAP = { 'format': 'xml'}
