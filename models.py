#!/usr/bin/python3

import datetime
import calendar
from enum import Enum

class Type(Enum):
	OPEN_VOTING = "open_voting"
	REGISTER = 'register'
	VOTE = 'vote'
	RESULT = 'result'

	__type = ''

	def __init__(self, _type):
		self.__type = _type

	def get_type(self):
		return self.__type

	def set_type(self, __type):
		self.__type = __type

	def __str__(self):
		return self.__type


class BaseEntity:
	_type = Type()
	sender = str()
	name = str()

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def setSender(self, sender):
		self.sender = sender

	def getSender(self):
		return self.sender

	def getType(self):
		return self._type

	def setType(self, _type: Type):
		self._type = _type


class Register(BaseEntity):
	def __init__(self):
		super().setType(Type.REGISTER)


class Result(BaseEntity):
	votes = {}

	def __init__(self):
		super().setType(Type.RESULT)

	def getVotes():
		return self.votes

	def setVotes(self, votes : dict):
		self.votes = votes


class Vote(BaseEntity):
	receiveTime = None # should contain a date object
	option = str()

	def __init__(self):
		super().setType(Type.VOTE)

	def getReceiveTime(self):
		return self.receiveTime

	def setReceiveTime(self, receiveTime):
		self.receiveTime = receiveTime

	def setOption(self, option):
		self.option = option

	def getOption(self):
		return self.option
	pass


class Voting(BaseEntity):

	startTime = None
	resultTime = None
	options = str()

	def __init__(self, options):
		this.options = options
		super().setType(Type.VOTING)

	def getStartTime(self):
		return self.startTime

	def setStartTime(self, startTime):
		self.startTime = startTime

	def getResultTime(self):
		return self.resultTime

	def setResultTime(self, resultTime):
		self.resultTime = resultTime

	def setDefaultTime(self):
		"""
		invoke gregorian calendar time here
		"""
		pass

	def getOptions(self):
		return self.options

	def setOptions(self, options):
		self.options = str(options)

	def __eq__(self, other):
		name = self.get_name()
		if name is not None:
			return name.__eq__(other)
		else:
			return False

	def __hash__(self):
		name = self.get_name()
		return name.__hash__()

	pass
