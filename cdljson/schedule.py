# -*- coding: utf-8 -*-

import json
import urllib2
import datetime
#~ import pytz

class JizonSchedule(object):
    """
    Class to manage schedule from Lanyrd
    """
    
    def __init__(self,jsonurl, days):
        '''
        Constructor
        '''
        self.__sessions = []
        self.__timezone = ""
        self.__days = []
        self.__conferences = []
        self.__workshops = []
        self.__jsonurl = jsonurl
        
    def retrieveData(self):
        '''
        retrieving data from json
        '''
        if not self.__sessions :
            inputd = urllib2.urlopen(self.__jsonurl).read()
            raw = json.loads(inputd)
            self.__sessions = raw["sessions"]

            for session in self.__sessions:
                self.__days.append(session['day'])
                if self.__days[0] in session['day'] and len(session['sessions']) != 0:
                    self.__conferences = session['sessions']
                elif self.__days[1] in session['day']:
                    self.__workshops = session['sessions']
            
    def getConferences(self):
        """Get all conferences, on day 1
        """
        return self.__conferences

    def getWorkshops(self):
        """Get all workshops
        """
        return self.__workshops
