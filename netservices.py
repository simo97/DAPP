#!/usr/bin/python3

"""
what we need to do: launch 2 services (thread) one to listen the network and other one to 
send data over it
"""

import threading
import time
import socket
import random
import sys
import json
import datetime

from timer import Timer, TimerTask
from storage import Storage
from models import *

UDP_IP = "10.42.0.1"
UDP_PORT = 4002
MESSAGE = "Hello, world!"


class OutingService:

    def __init__(self, conn):
        self.threadId = random.randint(0, 10)
        self.connexion = conn

    def register(self, register):
        self.send(register)

    def create(self, voting):
        Storage.register_voting(voting)
        timer = Timer()
        outboundService = self

        class TaskRunner(TimerTask):

            def run(self):
                print("Timer out voting it's time is results id:" + voting.get_name())
                result = Result()
                result = Storage.get_result(voting.get_name())
                if result is not None:
                    outboundService.result(result)

        task = TaskRunner()
        timer.schedulePeriodic(task, voting.get_result_time())
        self.send(voting)

    def vote(self, vote):
        self.send(vote)

    def send(self, obj):
        try:
            json_obj = json.dumps(obj.__dict__)
            self._send(json_obj)
        except:
            print('Exception catch when dumping the object')

    def _send(self, message):
        self.connexion.send(message.encode('Utf-8'))

    def result(self, result):
        self.send(result)


class InboundingService(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.threadId = random.randint(0, 10)
        self.connexion = conn
        self.outboundService = OutingService()

    def register(self, register):
        Storage.register(register)

    def result(self, result):
        pass

    def registerForNewVoting(self, voting):
        register = Voting()
        register.setSender(Storage.NAME)
        register.setName(voting.getName())
        print('Register for :' + voting.getName())
        self.outboundService.register(register)

        vote = Vote()
        vote.setName(voting.getName())
        vote.setSender(Storage.NAME)
        vote.setReceiveTime(datetime.datetime.today())
        options = voting.getOptions()
        index = random.randint(0, len(options))
        vote.setOption(options[abs(index)])
        out = self.outboundService

        timer = Timer()

        class TaskRunner(TimerTask):

            def run(self):
                print("Timer out voting time is come id:" + voting.get_name())
                out.vote(vote)

        task = TaskRunner()
        timer.schedulePeriodic(task, voting.getStartTime())

    def vote(self, vote):
        Storage.vote(vote)

    def serve(self, json_):
        try:
            data = json.loads(json_)
            typeString = str(data['type'])
            type_ = Type.value(typeString)

            if type_ == Type.VOTE:
                vote = Vote()
                vote.setReceiveTime(datetime.now())
                vote.setOption(data['option'])
                vote.setName(data['name'])
                vote.setSender(data['sender'])
                vote.setType(data['type'])
                self.vote(vote)
            elif type_ == Type.OPEN_VOTING:
                voting = Voting()
                voting.setStartTime(data['startTime'])
                voting.setResultTime(data['resultTime'])
                voting.setOptions(data['options'])
                voting.setName(data['name'])
                voting.setSender(data['sender'])
                voting.setType(data['type'])
                self.registerForNewVoting(voting)
            elif type_ == Type.RESULT:
                result = Result()
                result.setVotes(data['votes'])
                result.setName(data['name'])
                result.setSender(data['sender'])
                result.setType(data['type'])
                self.result(result)
            elif type_ == Type.REGISTER:
                register = Register()
                register.setVotes(data['votes'])
                register.setName(data['name'])
                register.setSender(data['sender'])
                register.setType(data['type'])
                self.register(register)
            else:
                print("Error, unknown message type: " + typeString)
        except :
            print('e')

    def run(self):
        print(' inbound service is working')
        while True:
            message_recu = self.connexion.recv(1024).decode('Utf-8')

            self.serve(message_recu)
            print('----->' + message_recu)
            if message_recu.upper() == "OK":
                print('No more message. Exiting : ' + message_recu)
                break
        self.connexion.close()
