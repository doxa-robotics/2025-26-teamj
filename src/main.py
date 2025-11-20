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
  
#1-front, 2-bottom, 3-top
motor_left_1 = Motor(Ports.PORT10, False)
motor_left_2 = Motor(Ports.PORT9, False)
motor_left_3 = Motor(Ports.PORT8, False)
motor_right_1 = Motor(Ports.PORT3, True)
motor_right_2 = Motor(Ports.PORT4, True)
motor_right_3 = Motor(Ports.PORT5, False)

#creating motor groups
#match_loa 1 is extend and 2 is retract
left_motors = MotorGroup(motor_left_1, motor_left_2, motor_left_3)
right_motors = MotorGroup(motor_right_1, motor_right_2, motor_right_3)
motor_intake = Motor(Ports.PORT11, True)
motor_intake_2 = Motor(Ports.PORT18, True)
motor_intake_3 = Motor(Ports.PORT17, True)
intake_motors = MotorGroup(motor_intake, motor_intake_2)
match_load = Pneumatics(brain.three_wire_port.g)

#Gyro
inertial = Inertial(Ports.PORT7)

drivetrain = SmartDrive(
    left_motors,
    right_motors,
    inertial,
    300,
    320,
    320,
    MM
)

#def autonomous2():
    
#Autonomous_2
brain.screen.clear_screen()
brain.screen.print("autonomous code")
    # place automonous code here
    #needs extra help

#all = DriveTrain(left_motors,right_motors)
#all.set_timeout(4000) 


#move(FORWARD, 100)
#bmove(REVERSE, 100)

#def move(direction: DirectionType.DirectionType, distance: int, velocity=75):
        #all.drive_for(direction, distance, MM, velocity, RPM)

def autonomous():
    
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    drivetrain.drive_for(FORWARD, 500, MM, 75, PERCENT)



    


   


def driver_control():
    toggle_state = False
    last_pressed = False
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    #Driver_ctrl
    while True:
        speed = controller.axis3.position()
        turn = controller.axis1.position()

        left_motors.spin(FORWARD, speed - turn, PERCENT)
        right_motors.spin(FORWARD, speed + turn, PERCENT)
        
         #codes from intake motors
        if controller.buttonR1.pressing():
            intake_motors.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL1.pressing():
            intake_motors.spin(FORWARD, -100, PERCENT)
        else:
            intake_motors.stop(COAST)
 
        if controller.buttonR2.pressing():
            motor_intake_3.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL2.pressing():
            motor_intake_3.spin(FORWARD, -100, PERCENT)
        else:
            motor_intake_3.stop(COAST)
    
        #Codes for Pneumatics
        if controller.buttonX.pressing() and last_pressed == False:
            toggle_state = not toggle_state
            if toggle_state:
                match_load.open()
            else:
                match_load.close()
        last_pressed = controller.buttonX.pressing()
        
         
          


    
        wait(20, MSEC)

    


# Tell VEX what *functions* we want to run when
Competition(driver_control, autonomous)

