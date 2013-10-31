import json
import urllib2

class jizon(object):
    '''
    class to parse and manage json data from 
    cdl volunteers web form
    '''


    def __init__(self,jsonurl):
        '''
        Constructor
        '''
        self.__nbvendredi = 0
        self.__nbsamedi = 0
        self.__nbdimanche = 0
        self.__nbinscritrepas = 0
        self.__nbvolunteers = 0
        self.__jsonurl = jsonurl
        self.__list = []
        self.__emailList = []
        
    def retrieveData(self):
        '''
        retrieving data from json
        '''
        if not self.__list :
            inputd = urllib2.urlopen(self.__jsonurl).read()
            raw = json.loads(inputd)
            self.__list = raw["data"]
            
            self.__nbvolunteers = len(self.__list)
            
            for b in self.__list:
                if b["Repas"]:
                    self.__nbinscritrepas+=1
                if b["Dispo vendredi"]:
                    self.__nbvendredi +=1
                if b["Dispo samedi"]:
                    self.__nbsamedi += 1
                if b["Dispo dimanche"]:
                    self.__nbdimanche +=1
                    
    def getNbVolunteers(self):
        return self.__nbvolunteers
    
    def getNbVendredi(self):
        return self.__nbvendredi
    
    def getNbSamedi(self):
        return self.__nbsamedi
    
    def getNbDimanche(self):
        return self.__nbdimanche
    
    def getNbInscritRepas(self):
        return self.__nbinscritrepas
    
    def getEmailList(self):
        
        if not self.__emailList:
            for v in self.__list :
                self.__emailList.append(v["Email"])
        return self.__emailList
    
        
    
        