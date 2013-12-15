# -*- coding: utf-8 -*-

import os
from datetime import datetime
from cdljson.schedule import JizonSchedule
from pelican import utils as putils


def get_time_from_epoch(epoch):
    dtime = datetime.fromtimestamp(epoch)
    return dtime.strftime('%H:%M')


days = ['23','24']
scheduleurl = "http://localhost:8000/files/capitole-du-libre-schedule.json"
donnee = JizonSchedule(scheduleurl, days)
print "retrieving information ..."
donnee.retrieveData()
BASEDIR = "/home/numahell/Dev/pelican/capitoledulibre-site/src/pages/schedule"

try:
    os.mkdir(BASEDIR)
except:
    pass
os.chdir(BASEDIR)

conferences = donnee.getConferences()


for w in conferences[0:3]:
    
    title = w['title']
    rstheading = u"="*len(title)
    start = get_time_from_epoch(w['start_time_epoch'])
    end = get_time_from_epoch(w['end_time_epoch'])
    wid = putils.slugify(w['title'])
    space = w['space']
    abstract = w['abstract']
    speakers = ""
    
    file_name = "%s.rst" % wid
    
    output = '\n'.join([rstheading, 
                        title, 
                        rstheading, 
                        u"",
                        u""":space: %s""" % space,
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
