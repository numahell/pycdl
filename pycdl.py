# -*- coding: utf-8 -*-
import json
import urllib2


nbvendredi = 0
nbsamedi = 0
nbdimanche = 0
nbrepas = 0
mailinglist = ''
print "retrieving information ..."
fi = urllib2.urlopen("http://daybed.lolnet.org/data/j8FMkkCKDgceG").read()
raw = json.loads(fi)

list = raw["data"]
print "---------------------"
print "nombre d 'inscrit %s" % len(list)
print "---------------------"

for b in list:
    if b["Repas"]:
        nbrepas+=1
    if b["Dispo vendredi"]:
        nbvendredi +=1
    if b["Dispo samedi"]:
        nbsamedi += 1
    if b["Dispo dimanche"]:
        nbdimanche +=1


    mailinglist += (b["Email"] + ',')

print "Nombre de benevoles vendredi : %d" %  nbvendredi
print "Nombre de benevoles samedi : %d" %  nbsamedi
print "Nombre de benevoles dimanche : %d" %  nbdimanche
print "---------------------"
print "Nombre de benevoles au repas : %d" %  nbrepas
print "---------------------"

