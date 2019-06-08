#!/usr/bin/python3

import random
import datetime

import netservices


class Storage:
    voteMaps = {}
    registrations = {}
    votings = []
    resultsMap = {}
    outboundService = netservices.OutingService()

    def __init__(self):
        self.NAME = random.randint(0, 10)

    @classmethod
    def registerVoting(cls, voting):
        cls.voting.append(voting)
        cls.registrations[voting.name] = list()
        cls.voteMaps[voting.name] = list()

    @classmethod
    def vote(cls):
        voting = None
        for vot in cls.votings:
            if vot.name == cls.vote.getName():
                voting = vot
        if voting == None:
            print("Unknown vote for voting:" + cls.vote.getName())
            return None

        registrations = []  # list of registrations
        register = None
        for reg in registrations:
            if reg.getSender() == cls.vote.getSender():
                register = reg
        if register == None:
            print("Received vote which is not registered" + cls.vote.getName())
            return None
        now = datetime.date.today()
        starttime = voting.getStartTime()
        isNotTimeYet = starttime > now
        votes = []

        if isNotTimeYet:
            print("Received vote but it's not time for voting yet, name:" + cls.vote.getName())
            return None

        elif cls.voteMaps[cls.vote.getName()]:
            votes = Storage.voteMaps[cls.vote.getName()]
            votes.append(cls.vote)

        if len(votes) == len(registrations):
            print("All registered have voted, making result")
            res = Storage.getresult(voting.getName())
            cls.outboundService.result(res)

    @classmethod
    def register(cls, register):
        votingObj = None
        for voting in cls.votings:
            if voting.name == register.name:
                votingObj = voting

        if votingObj == None:
            print("Unknown register for voting:" + register.name)
            return None

        registerList = Storage.registrations[register.name]
        if registerList == None:
            print("Unknown register for voting:" + register.name)
        else:
            registerList.append(register)

    def getresult(self, voting):
        if self.resultsMap[voting]:
            print("Resuld already sent:" + voting)
            return None

        result = None  # should be a result instance todo
        votes = Storage.voteMaps[voting]
        results = {}  # {str: list}

        for vote in votes:
            option = vote.getOptions()
            if option in results:
                results[option] = results[self.options] + 1
            else:
                results[option] = 1

        result.setVotes(results)
        result.setName(voting)
        result.setSender(self.NAME)

        self.resultsMap[result.name] = result
