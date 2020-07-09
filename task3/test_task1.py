
# Take your partners improved solution to task_1
# And make 10 tests with unittest
# Your code should be runnable as:
# "python -m unittest test_task1"
# If there is not enough code to make 10 tests,
# or the code can't be tested you need to alter the solution,
# so that it would be possible to test it.
# How to get your partners solution:
#  1. go to your own solution on github
#  2. go the adress bar in the browser
#  4. change your username, to your partners username
#  5. enjoy the easy and cheerful task of working with someone's else code
#  6. There is no point 3
#
# On your own, you need to copy his code into this repository!!!
# Remember to include it while commiting.
#
# Fill the data here in the comments
#
# I am using solution by Aureliusz13 
# from the commit master
#

import unittest

from task import Environment
from task import Car
from task import Event

class TestCar(unittest.TestCase):
    def testCarSpeed(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        self.assertEqual(car.safe_speed,40)
       
    def testTurn(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        testangle = 30
        car.turn(testangle)
        self.assertEqual(car.wheel_angle,30)

    def testEnvironment(self):
        env = Environment('Outside the City', 40, 120)
        self.assertEqual(env.name,'Outside the City')

    def testbreaking(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        car.go_forward(3)
        self.assertEqual(car.speed,18)
        car.breaking()
        self.assertEqual(car.speed,0)

    def testSpeedInfo(self):
        test = 'Car current speed: 0'
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        self.assertEqual(car.speed_info(),test)

    def testWheelAngleInfo(self):
        test = 'Car current wheel angle: 0'
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        self.assertEqual(car.wheel_angle_info(),test)


    def testObstacle(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        car.manage_obstacle(1)
        self.assertEqual(car.wheel_angle,0)
    
    def testRunAfterRedLight(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        car.manage_red_light(1)
        self.assertEqual(car.speed,18)

    def testChangeEnvironment(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        env2 = Environment('In the city', 0, 50)
        car.change_environment(env2)
        self.assertEqual(car.environment.name,'In the city')

    def testAct(self):
        env = Environment('Outside the City', 40, 120)
        car = Car(env)
        car.go_forward(3)
        car.act(Event.TURN,'left')
        self.assertEqual(car.wheel_angle,0)

if __name__ == '__main__':

    unittest.main()

