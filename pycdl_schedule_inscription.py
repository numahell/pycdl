# -*- coding: utf-8 -*-
from datetime import datetime
from cdljson.schedule import JizonSchedule
'''

testing main file ! soon be better
'''

def get_time_from_epoch(epoch):
    dtime = datetime.fromtimestamp(epoch)
    return dtime.strftime('%H:%M')
    
    
    
days = ['23','24']
scheduleurl = "http://2013.capitoledulibre.org/files/capitole-du-libre-schedule.json"
donnee = JizonSchedule(scheduleurl, days)
print "retrieving information ..."
donnee.retrieveData()

workshops = donnee.getWorkshops()


for w in workshops:
    
    title = w['title']
    start = get_time_from_epoch(w['start_time_epoch'])
    wid = w['id']
    if len(w['topics']) != 0:
        tag = '%s-%s' % (w['topics'][0]['slug'], wid,)
    else:
        tag = wid
    wurl = 'http://2013.capitoledulibre.org/programme/ateliers.html#%s' % wid
    end = get_time_from_epoch(w['end_time_epoch'])
    file_name = "%s.txt" % wid

    f = open(file_name, 'w')
    f.write((u"====== %s ======" % title).encode('utf8'))
    f.write((u"\nCet atelier aura lieu le dimanche 24 novembre 2013, **de %s à %s**." % (start,end,)).encode('utf8'))
    f.write((u"\nRetrouvez [[%s|les détails de cet ateliers]] sur le site du Capitole du Libre." % wurl).encode('utf8'))
    f.write('\n\n{{page>capitoledulibre2013:repas}}')
    f.write((u"\n\nLe formulaire d'inscription ci-dessous est relatif à l'atelier **%s**. \nL'inscription est gratuite." % title).encode('utf8'))
    f.write((u"\n\n<phpinc=inscription?eventid=2013-11-24-atelier-%s&limit=15>\n" % tag).encode('utf8'))

    f.close()

    print '%s.txt file written' % wid
