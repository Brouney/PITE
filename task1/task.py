import random
import time
class Car:
    def __init__(self):
        self.angle = 0
        self.speed = 0
        self.distance = 0.
        self.time = 0
    def act(self,event,angl):
        event.run(angl)

class TurnLeft:
    def run(self,angl):
        angl.angle -= random.randint(0,20)
        angl.time += 1
        angl.distance +=  angl.speed

class TurnRight:
    def run(self,angl):
        angl.angle += random.randint(0,20)
        angl.time += 1
        angl.distance +=  angl.speed

class SpeedUp:
      def run(self,angl):
            angl.speed += random.randint(0,20)    
            angl.time += 1
            angl.distance +=  angl.speed

class SpeedDown:
      def run(self,angl):
            angl.speed -= random.randint(0,20)
            angl.time += 1
            angl.distance +=  angl.speed


left = TurnLeft()
right = TurnRight()
up = SpeedUp()
down = SpeedDown()
car1 = Car()
temp = [left,right,up,down]
file = open("Output.txt","w")
if __name__ =="__main__":
    print("if you want to stop, press : ctrl + c ")
    while True:
        active = random.randint(0,3)
        car1.act(temp[active],car1)
        print("speed: {} m/s angle: {} distance: {}".format(str(car1.speed),str(car1.angle),str(car1.distance)))
        file.write("speed: {} m/s angle: {} distance: {} \n".format(str(car1.speed),str(car1.angle),str(car1.distance)))
        time.sleep(1)
    


