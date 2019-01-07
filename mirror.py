#external modules
from collections import namedtuple
import cv2

#local modules
from DuckieBotModes import Driver

class Mirror(Driver):
    '''
    '''
    def __init__(self, camera=None, car=None):
        '''
        '''
        Driver.__init__(self, camera=camera, car=car)

    def tick(self, keys_pressed):
        '''
        '''
        #starting values (to be compared later)
        start_speed = self.speed
        start_omega = self.omega

        if "W" in keys_pressed:#up
            self.speed += self.speed_forces.applied
        if "S" in keys_pressed:#down
            self.speed -= self.speed_forces.applied
        if "A" in keys_pressed:#left
            self.omega -= self.omega_forces.applied
        if "D" in keys_pressed:#right
            self.omega += self.omega_forces.applied
        self.speed = self.drag(self.speed, self.speed_forces.drag)
        self.omega = self.drag(self.omega, self.omega_forces.drag)
        #deaccelerates items

        #reflect changes in car
        if start_speed != self.speed:
            self.car.set_speed(self.speed)
        if start_omega != self.omega:
            self.car.set_omega(self.omega)

    def frame(self, frame):
        '''
        '''
        frame = cv2.flip( frame, 1 )
        return frame
