#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        speed = 30
        self.car.accelerator.go_forward(speed)
        cnt = 0
        while True:
            l = self.car.line_detector.read_digital()
            if cnt <= 2:
                if self.car.distance_detector.get_distance() > 15:
                    if l == [1, 0, 0, 0, 0]:
                        self.car.steering.turn_left(78)
                    elif l == [0, 1, 0, 0, 0]:
                        self.car.steering.turn_left(83)
                    elif l == [0, 0, 0, 1, 0]:
                        self.car.steering.turn_right(127)
                    elif l == [0, 0, 0, 0, 1]:
                        self.car.steering.turn_right(132)
                    elif l == [1, 1, 0, 0, 0]:
                        self.car.steering.turn_left(63)
                    elif l == [0, 1, 1, 0, 0]:
                        self.car.steering.turn_left(88)
                    elif l == [0, 0, 1, 1, 0]:
                        self.car.steering.turn_right(92)
                    elif l == [0, 0, 0, 1, 1]:
                        self.car.steering.turn_right(97)
                    elif l == [0, 0, 1, 0, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 1, 0, 0, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [0, 0, 0, 1, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [0, 1, 0, 0, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 1, 1, 0, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [0, 1, 0, 0, 1]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 1, 1, 0, 1]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 1, 0, 0, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 0, 0, 1, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 1, 1, 0, 0]:
                        self.car.accelerator.go_forward(speed)
                    elif l == [1, 0, 0, 0, 1]:
                        self.car.accelerator.go_forward(speed)
                        time.sleep(0.2)
                    elif l == [0, 0, 0, 0, 1]:
                        self.car.accelerator.go_backward(speed)
                        time.sleep(0.2)
                    elif l == [0, 0, 0, 0, 0]:
                        self.car.steering.turn_right(130)
                        self.car.accelerator.go_backward(speed)
                        time.sleep(0.6)
                        self.car.steering.turn_left(45)
                        self.car.accelerator.go_forward(speed)
                        time.sleep(0.2)
                        continue
                    else:
                        self.car.accelerator.go_forward(speed)
                        time.sleep(0.1)

                elif 0 < self.car.distance_detector.get_distance() <= 15:
                    self.car.steering.turn_left(50)
                    self.car.accelerator.go_forward(speed+7)
                    time.sleep(1)
                    self.car.steering.turn_right(120)
                    self.car.accelerator.go_forward(speed+7)
                    time.sleep(1.8)
                    
            else:
                self.car.accelerator.power_down()



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
