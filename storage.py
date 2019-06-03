#!/usr/bin/python3

import random
import datetime

from netservices import OutingService


class Storage:
	voteMaps = {}
	registrations = {}
	votings = []
	resultsMap = {}
	outboundService = OutingService()

	def __init__(self):
		self.NAME = random.randint(0, 10)
		

	def registerVoting(self, voting):
		self.voting.append(voting)
		self.registrations[voting.name] = list()
		self.voteMaps[voting.name] = list()

	def vote(self):
		voting = None
		for vot in self.votings:
			if vot.name == vote.getName():
				voting = vot
		if voting == None:
			print("Unknown vote for voting:" + vote.getName())
			return None

		registrations = [] # list of registrations
		register = None
		for reg in registrations:
			if reg.getSender() == vote.getSender():
				register = reg
		if register == None:
			print("Received vote which is not registered" + vote.getName())
			return None
		now = datetime.date.today()
		starttime = voting.getStartTime()
		isNotTimeYet = starttime > now
		votes = []

		if isNotTimeYet:
			print("Received vote but it's not time for voting yet, name:" + vote.getName())
			return None

		elif voteMaps[vote.getName()]:
			votes =Storage.voteMaps[vote.getName()]
			votes.append(vote)

		if len(votes) == len(registrations):
			print("All registered have voted, making result")
			res = Storage.getresult(voting.getName())
			outboundService.result(res)

	def register(self, register):
		votingObj = None
		for voting in self.votings:
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

		result = None # should be a result instance todo
		votes = Storage.voteMaps[voting]
		results = {} # {str: list}

		for vote in votes:
			option = vote.getOptions()
			if option in results:
				results[option] = results[options] + 1
			else:
				results[option] = 1

		result.setVotes(results)
		result.setName(voting)
		result.setSender(self.NAME)

		self.resultsMap[result.name] = result
	pass