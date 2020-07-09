from enum import Enum
from time import sleep
from datetime import datetime
import logging
import random


class Logger():

    def __init__(self,
                 file='{}.log'.format(datetime.now().strftime("%d-%m-%Y_%H-%M-%S")),
                 time=True,
                 to_console=False):
        logging.basicConfig(filename=file,
                            level=logging.INFO,
                            format='%(asctime)s ### %(message)s' if time else '%(message)s')
        self.to_console = to_console

    def log(self, string):
        logging.info(string)
        if self.to_console:
            print(string)


class Event(Enum):
    OBSTACLE = 1,
    RED_LIGHT = 2,
    SAFE_SPEED_CHANGE = 3,
    TURN = 4


class Environment():

    def __init__(self, name, min_speed, max_speed):
        self.name = name
        self.min_speed = min_speed
        self.max_speed = max_speed

    def generate_event(self):
        event = random.choice(list(Event))
        if event == Event.OBSTACLE:
            return event, random.randint(3, 20)
        elif event == Event.RED_LIGHT:
            return event, random.randint(3, 15)
        elif event == Event.SAFE_SPEED_CHANGE:
            return event, random.randint(self.min_speed, self.max_speed)
        elif event == Event.TURN:
            return event, random.choice(['left', 'right'])


class Car():
    def __init__(self, environment):
        self.wheel_angle = 0
        self.speed = 0
        self.safe_speed = environment.min_speed
        self.environment = environment
        self.logger = Logger()

        self.logger.log(self.initial_status())

    def test_run(self):
        try:
            while True:
                self.go_forward(3)
                self.act(*self.environment.generate_event())
        except KeyboardInterrupt:
            self.logger.log(self.keyboard_interruption_info())
            exit(0)

    def act(self, event, data=0):
        if event == Event.OBSTACLE:
            self.manage_obstacle(data)
        elif event == Event.RED_LIGHT:
            self.manage_red_light(data)
        elif event == Event.SAFE_SPEED_CHANGE:
            self.safe_speed = data
            self.adjust_speed()
        elif event == Event.TURN:
            self.manage_turn(data)

    def manage_obstacle(self, time):
        self.logger.log('EVENT: OBSTACLE!')
        self.breaking()
        if time < 10:
            sleep(time)
        else:
            self.turn(-30)
            self.go_forward(2)
            self.turn(60)
            self.go_forward(2)
            self.turn(-30)

    def manage_red_light(self, time):
        self.logger.log('EVENT: RED LIGHT!')
        self.breaking()
        sleep(time)
        self.go_forward(3)

    def manage_turn(self, side):
        self.logger.log('EVENT: TURN!')
        angle = -90 if side.lower() == 'left' else 90
        self.turn(angle)
        self.go_forward(2)
        self.turn(-angle)

    def breaking(self):
        while self.speed:
            self.speed -= 1
            self.logger.log(self.speed_info())
            sleep(0.05)
        self.logger.log('Car stopped')

    def go_forward(self, time):
        t = 0.0
        while t < time:
            if self.speed < self.safe_speed:
                self.speed += 3
            self.logger.log(self.speed_info())
            t += 0.5
            sleep(0.5)

    def turn(self, angle):
        self.wheel_angle += angle
        self.logger.log(self.wheel_angle_info())

    def adjust_speed(self):
        if self.speed > self.safe_speed:
            self.logger.log('Speed to high. Going slower')
            while self.speed > self.safe_speed:
                self.speed -= 1
                self.logger.log(self.speed_info())
                sleep(0.05)
        else:
            self.logger.log('Speed can be higher. Going faster')
            while self.speed < self.safe_speed:
                self.speed += 1
                self.logger.log(self.speed_info())
                sleep(0.05)

    def speed_info(self):
        return 'Car current speed: {s}'.format(s=self.speed)

    def wheel_angle_info(self):
        return 'Car current wheel angle: {s}'.format(s=self.wheel_angle)

    def initial_status(self):
        return 'Starting car with wheel angle: {wa}, and speed: {s}'.format(wa=self.wheel_angle, s=self.speed)

    def keyboard_interruption_info(self):
        return "\n Keyboard Interrupt. Shutting down the simulation"

    def change_environment(self, environment):
        self.environment = environment
        self.safe_speed = environment.min_speed
        self.adjust_speed()


if __name__ == '__main__':
    env = Environment('Outside the City', 40, 120)
    car = Car(env)
    car.test_run()
