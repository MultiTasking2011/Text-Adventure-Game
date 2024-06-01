import time
import sys

class game:
    def __init__(self, input, printing) -> None:
        self.input = input
        self.maplist = [""]
        self.health = 0
        self.objects = 0
        self.moveindex = 0
        self.maplist.asylum = [""]
        self.maplist.roof = [""]
        self.maplist.topfloor = [""]
        self.maplist.midfloormain = [""]
        self.maplist.midfloorcoridoor = [""]
        self.maplist.cafiteria = [""]
        self.maplist.office = [""]
        self.maplist.patientroomone = [""]
        self.maplist.patientroomtwo = [""]
        self.maplist.patientroomthree = [""]
        self.maplist.patientroomfour = [""]
        self.maplist.patientroomfive = [""]
        self.maplist.bottomfloormain = [""]
        self.maplist.bottomfloorcoridoor = [""]
        self.maplist.reception = [""]
        self.maplist.doctorsroom = [""]
        self.maplist.patientroomsix = [""]
        self.maplist.patientroomseven = [""]
        self.maplist.patientroomeight = [""]
        self.maplist.patientroomnine = [""]
        self.maplist.patientroomten = [""]


    def delay_print(self, printing):
        for i in self.printing():
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.01)

    def map(self):
        self.maplist.asylum = [""]
        self.maplist.roof = [""]
        self.maplist.topfloor = [""]
        self.maplist.midfloormain = [""]
        self.maplist.midfloorcoridoor = [""]
        self.maplist.cafiteria = [""]
        self.maplist.office = [""]
        self.maplist.patientroomone = [""]
        self.maplist.patientroomtwo = [""]
        self.maplist.patientroomthree = [""]
        self.maplist.patientroomfour = [""]
        self.maplist.patientroomfive = [""]
        self.maplist.bottomfloormain = [""]
        self.maplist.bottomfloorcoridoor = [""]
        self.maplist.reception = [""]
        self.maplist.doctorsroom = [""]
        self.maplist.patientroomsix = [""]
        self.maplist.patientroomseven = [""]
        self.maplist.patientroomeight = [""]
        self.maplist.patientroomnine = [""]
        self.maplist.patientroomten = [""]


    def commands(self):
        pass

    def storyline(self):
        pass

    def conditions(self):
        pass

    def gameplay(self):
        pass

    def characters(self):
        pass

    def help(self):
        pass
    
    def __str__(self) -> str:
        return ""

textinput = input("What will you do?")
gamevar = game()
