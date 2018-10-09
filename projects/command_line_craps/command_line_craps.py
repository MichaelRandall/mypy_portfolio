#!/usr/local/bin/python

import datetime, random

class Craps():
    def __init__(self,p_name='Michael'):
        self.name = p_name
        self.game_id = ''
        self.game_start = ''
        self.game_end = ''
        self.dice_one = 0
        self.dice_two = 0
        self.current_point = 0
        self.current_roll = 0
        self.current_roll_count = 0
        self.role_history = []
        self.messages = ['Roller coming out','Roller rolling','Craps','Win']
        # self.status = messages[0]
        self.status = 'Roller coming out'

    def rollDice(self):
        roll = (random.randint(1,9), random.randint(1,9))
        return roll

    # Set methods
    def setGameId(self,p_gameid):
        self.game_id = p_gameid
    
    def setStartTime(self,p_gamestart):
        self.game_start = p_gamestart
        
    def setEndTime(self,p_gameend):
        self.game_end = p_gameend
        
    
    # Get methods
    def getCurrentRollCount(self):
        return self.current_roll_count
    
    def getRollHistory(self):
        return self.role_history
    
    def getCurrentPoint(self):
        return self.current_point

    
    def startautoplay(self):
        self.setGameId(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
        self.setStartTime(datetime.datetime.now())
        while (self.status != self.messages[2] or self.status != self.messages[3]):
            (d1,d2) = self.rollDice()
            self.dice_one = random.randint(1, 9)
            self.dice_two = random.randint(1, 9)
            self.current_roll = (self.dice_one,self.dice_two)
            self.current_roll_value = sum(list(self.current_roll))
            self.current_roll_count = self.current_roll_count + 1
            self.role_history.append(self.current_roll)
        
            if self.current_roll_count == 1:
                if self.current_roll_value in [7,11]:
                    self.status = self.messages[3]
                    print('Roller coming out roll is: ' + str(self.current_roll_value) + ' and dice ' + str(self.current_roll[0]) + ', ' + str(self.current_roll[1]))
                    print('Roller Wins on Come Out!')
                    self.setEndTime(datetime.datetime.now())
                    break
                else:
                    self.current_point = self.current_roll_value
                    self.status = self.messages[1]
                    print('Roller coming out roll is: ' + str(self.current_roll_value) + ' and dice ' + str(self.current_roll[0]) + ', ' + str(self.current_roll[1]))
            else:
                if self.current_roll_value == self.current_point:
                    self.status = self.messages[3]
                    print(self.status + ', ' + str(self.current_roll[0]) + ', ' + str(self.current_roll[1]))
                    print('Roller Wins!')
                    self.setEndTime(datetime.datetime.now())
                    break
                elif self.current_roll_value in [7,11]:
                    self.status = self.messages[2]
                    print(self.status + ', ' + str(self.current_roll[0]) + ', ' + str(self.current_roll[1]))
                    print('Roller Loses')
                    self.setEndTime(datetime.datetime.now())
                    break
                else:
                    self.status = self.messages[1]
                    print(self.status + ', ' + str(self.current_roll[0]) + ', ' + str(self.current_roll[1]))
                    print('Roller Continues Rolling')
         
                
        return self.status

mycraps = Craps()
mycraps.startautoplay()