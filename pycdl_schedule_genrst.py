# -*- coding: utf-8 -*-

import os
from datetime import datetime
from cdljson.schedule import JizonSchedule
from pelican import utils as putils


def get_time_from_epoch(epoch):
    dtime = datetime.fromtimestamp(epoch)
    return dtime.strftime('%H:%M')


days = ['23','24']
scheduleurl_francejs = "http://localhost:8000/files/francejs-schedule.json"
scheduleurl_cdl = "http://localhost:8000/files/capitole-du-libre-schedule.json"
BASEDIR = "/home/numahell/Dev/pelican/capitoledulibre-site/src/pages/videos-conferences"
VIDEO_URLBASE = "http://stream.toulibre.org/cdl2013"
THEMES = {
    "A001": u"grand-public",
    "A002": u"multimedia-bureautique",
    "A201": u"technique",
    "A202": u"francejs",
    "A203": u"multimedia-bureautique",
    "C002": u"internet-libre",
    "C103": u"akademy-fr",
}

def gen_rst_pages(scheduleurl):

    donnee = JizonSchedule(scheduleurl, days)
    print "retrieving information ..."
    donnee.retrieveData()

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
        theme = THEMES[w['space']]
        theme = "francejs"
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
                            u""":video_url: %s/%s/%s""" % (VIDEO_URLBASE, theme, wid),
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


def gen_rst_lists(scheduleurl):

    donnee = JizonSchedule(scheduleurl, days)
    print "retrieving information ..."
    donnee.retrieveData()

    conferences = donnee.getConferences()
    
    conferences_list = {}
    output = ""
    themes = THEMES
    for theme in themes.values():
        conferences_list[theme] = u""
    
    for w in conferences:
        
        title = w['title']
        wid = putils.slugify(w['title'])
        theme = THEMES[w['space']]
        speakers = ""
        if w.has_key('speakers'):
            speakers_names = [s['name'] for s in w['speakers']]
            speakers = ', '.join(speakers_names)
        
        conferences_list[theme] += u"""* `%s </conferences/%s/%s.html>`_ - par %s\n""" % (title, theme, wid, speakers)

    for theme in themes.values():
        
        rstheading = u"="*len(theme)
        output = "\n".join([rstheading,
                            theme,
                            rstheading,
                            u"",
                            u":url: conferences/%s/" % theme,
                            u":save_as: conferences/%s/index.html" % theme,
                            u":template: conferences"
                            u"",
                            u"",
                            conferences_list[theme],
                            ])
        theme_basedir = '/'.join([BASEDIR, theme])
        
        try:
            os.mkdir(theme_basedir)
        except:
            pass
        os.chdir(theme_basedir)
    
        file_name = "index.rst"
        f = open(file_name, 'w')
        f.write(output.encode('utf8'))
        f.close()

        print '%s file written' % file_name

def main():
	
	#~ gen_rst_lists(scheduleurl_cdl)

if __name__ == '__main__':
	main()

