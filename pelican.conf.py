#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"SAASPhysics Winter2015-2016"
SITEURL = 'http://markbetnel.com/courses/physics/w2015-16'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'betnelcourses'
COMMENTS_INTRO = "Is something unclear? Leave a comment below:"

DOCUTIL_CSS = True

DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATHS = ['/home/mark/Sites/pelican-plugins'] 
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican_vimeo', 'tipue_search', 'pelican_youtube', 'sitemap', 'latex']

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITEMAP = { 'format': 'xml'}

LANDING_PAGE_ABOUT = {'details': """<div itemscope itemtype="http://schema.org/Person"><p>This is the archive copy of the winter2015-2016 trimester of SAAS Physics.  Please got to <a href="http://markbetnel.com/courses/physics/current">the current version</a> if you want to see the current trimester.</p></div>"""}

MATH_JAX = {'color':'blue', 'menuSettings': {"zoom": "Click"}}

HYPOTHESIS = True

