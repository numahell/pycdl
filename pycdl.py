# -*- coding: utf-8 -*-
from cdljson.data import jizon
'''

testing main file ! soon be better
'''

donnee = jizon("http://daybed.lolnet.org/data/j8FMkkCKDgceG")
print "retrieving information ..."
donnee.retrieveData()

print "---------------------"
print "nombre d 'inscrit %d" % donnee.getNbVolunteers()
print "---------------------"


print "Nombre de benevoles vendredi : %d" %  donnee.getNbVendredi()
print "Nombre de benevoles samedi : %d" %  donnee.getNbSamedi()
print "Nombre de benevoles dimanche : %d" %  donnee.getNbDimanche()
print "---------------------"
print "Nombre de benevoles au repas : %d" %  donnee.getNbInscritRepas()
print "---------------------"

mailing = donnee.getEmailList()

print mailing

