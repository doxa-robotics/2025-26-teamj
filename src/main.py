# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Programer                                                    #
# 	Created:      10/28/2025, 4:46:14 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller = Controller()
#Motors on ports 1 through 6
#Motors(port: Port, reversed: bool)
#One side(either left or right) has to be all false while the other side is all true; so that it doesn't rotate, staying in one spot
#-for our robot right is false;left is true

#intake PORT14
#1-front, 2-bottom, 3-top
#right front-11, right bottom 12, right top 13... Left front 3, Left bottom 4, Left top 5)
motor_left_1 = Motor(Ports.PORT3, True)
motor_left_2 = Motor(Ports.PORT4, True)
motor_left_3 = Motor(Ports.PORT5, False)
motor_right_1 = Motor(Ports.PORT11, False)
motor_right_2 = Motor(Ports.PORT12, False)
motor_right_3 = Motor(Ports.PORT13, True)

#creating motor groups
#match_loa 1 is extend and 2 is retract
left_motors = MotorGroup(motor_left_1, motor_left_2, motor_left_3)
right_motors = MotorGroup(motor_right_1, motor_right_2, motor_right_3)
motor_intake = Motor(Ports.PORT14, True)
motor_intake_2 = Motor(Ports.PORT15, True)
match_load = Pneumatics(brain.three_wire_port.b)
match_load_2 = Pneumatics(brain.three_wire_port.a) 




def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here
    #needs extra help
    left_motors.spin(FORWARD, 100, PERCENT)
    right_motors.spin(FORWARD, 100, PERCENT)
    wait(2000, MSEC)

    motor_intake.spin(FORWARD, 100, PERCENT)
    wait(1000, MSEC)
    motor_intake.stop()

    left_motors.spin(FORWARD, -100, PERCENT)
    right_motors.spin(FORWARD, -100, PERCENT)
    wait(1500, MSEC)

    #stopping everthing
    left_motors.stop()
    right_motors.stop()
    motor_intake.stop()
    brain.screen.print('Autonomous round done')    
    wait(1000, MSEC)

def driver_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    #Driver_ctrl
    while True:
        speed = controller.axis3.position()
        turn = controller.axis1.position()

        left_motors.spin(FORWARD, speed - turn, PERCENT)
        right_motors.spin(FORWARD, speed + turn, PERCENT)
        
        if controller.buttonR1.pressing():
            motor_intake.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL1.pressing():
           motor_intake.spin(FORWARD, -100, PERCENT)
        else:
            motor_intake.stop(COAST)

        if controller.buttonR2.pressing():
            motor_intake_2.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL2.pressing():
            motor_intake_2.spin(FORWARD, -100, PERCENT)
        else:
            motor_intake_2.stop(COAST)

        #Codes for Pneumatics (toggle)
        if controller.buttonX.pressing():
            match_load.open
            match_load_2.close
        elif controller.buttonY.pressing():
            match_load.close
            match_load_2.open
        
    
        wait(20, MSEC)



# Tell VEX what *functions* we want to run when
Competition(driver_control, autonomous)

