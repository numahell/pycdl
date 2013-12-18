# -*- coding: utf-8 -*-

import os
from datetime import datetime
from cdljson.schedule import JizonSchedule
from pelican import utils as putils


def get_time_from_epoch(epoch):
    dtime = datetime.fromtimestamp(epoch)
    return dtime.strftime('%H:%M')


days = ['23','24']
scheduleurl = "http://localhost:8000/files/francejs-schedule.json"
donnee = JizonSchedule(scheduleurl, days)
print "retrieving information ..."
donnee.retrieveData()
BASEDIR = "/home/numahell/Dev/pelican/capitoledulibre-site/src/pages/schedule"
VIDEO_URLBASE = "http://toulibre.org/pub/2013-11-23-capitole-du-libre/videos"
THEMES = {
    "A001": u"grand-public",
    "A002": u"multimedia-bureautique",
    "A201": u"Technique",
    "A202": u"france-js",
    "A203": u"multimedia-bureautique",
    "C002": u"internet-libre",
    "C103": u"akademy-fr",
}

try:
    os.mkdir(BASEDIR)
except:
    pass
os.chdir(BASEDIR)

conferences = donnee.getConferences()


for w in conferences:
    
    title = w['title']
    rstheading = u"="*len(title)
    start = get_time_from_epoch(w['start_time_epoch'])
    end = get_time_from_epoch(w['end_time_epoch'])
    wid = putils.slugify(w['title'])
    space = w['space']
    #~ theme = THEMES[w['space']]
    theme = "france-js"
    abstract = w['abstract']
    speakers = ""
    if w.has_key('speakers'):
        speakers_names = [s['name'] for s in w['speakers']]
        speakers = ', '.join(speakers_names)
    
    file_name = "%s.rst" % wid
    
    output = '\n'.join([rstheading, 
                        title, 
                        rstheading, 
                        u"",
                        u""":url: conferences/%s/%s.html""" % (theme, wid),
                        u""":save_as: conferences/%s/%s.html""" % (theme, wid),
                        u""":video_url: %s/%s""" % (VIDEO_URLBASE, theme),
                        u""":speakers: %s""" % speakers,
                        u":template: conference",
                        u"",
                        u""".. html::""",
                        u"",
                        u" %s" % abstract.replace('\n',''),
                        u"",
                        u"",
                        ])

    f = open(file_name, 'w')
    f.write(output.encode('utf8'))
    f.close()

    print '%s file written' % file_name
