#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"SAASPhysics Fall2015"
SITEURL = 'http://markbetnel.com/courses/physics/fall2015'

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

LANDING_PAGE_ABOUT = {'details': """<div itemscope itemtype="http://schema.org/Person"><p>This is an archive copy of the course page for the Fall 2015 trimester of SAAS Physics.  If you are a current SAAS Physics student, please go to the <a href="http://markbetnel.com/courses/physics/current">Current</a> page for information about the current trimester of the class.</p></div>"""}


