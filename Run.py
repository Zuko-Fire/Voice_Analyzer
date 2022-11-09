#import PyQt5.QtWidgets

import Analysis_Logic

import time

#import RasberryPY_SystemLogic
import Suggestion_Generator




def run():
 word = Suggestion_Generator.wheel_rotation_random()

 #word = ['cat','happi','run']

 #self.ui.WordEdit.setText(f"{word[0]} {word[1]} {word[2]}")

 startTime = time.time()


 print(word[0],word[1],word[2])
 #RasberryPY_SystemLogic.onPin(word[3],word[4],word[5])
 sec = 10
 while sec > 0:
  print(sec)
  sec -=1
  time.sleep(1)

 Analysis_Logic.Step_One(word)

 Time = time.time() - startTime
 print(Time)
 t = open("person_buffer.txt")
 t.write(Time)
 t.close()
 #RasberryPY_SystemLogic.offPin()

run()







