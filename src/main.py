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
motor_left_1 = Motor(Ports.PORT9, False)
motor_left_2 = Motor(Ports.PORT8, False)
motor_left_3 = Motor(Ports.PORT7, True)
motor_right_1 = Motor(Ports.PORT3, True)
motor_right_2 = Motor(Ports.PORT4, True)
motor_right_3 = Motor(Ports.PORT5, False)


#match_load 1 is extend and 2 is retract
left_motors = MotorGroup(motor_left_1, motor_left_2, motor_left_3)
right_motors = MotorGroup(motor_right_1, motor_right_2, motor_right_3)
motor_intake = Motor(Ports.PORT10, False)
motor_intake_2 = Motor(Ports.PORT13, False)
intake_motors = MotorGroup(motor_intake)
match_load = Pneumatics(brain.three_wire_port.d)
outtake_launcher = Pneumatics(brain.three_wire_port.c)

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


    
#Autonomous_2
brain.screen.clear_screen()
brain.screen.print("autonomous code")
     

def auton_long_goal_right():
    """Auton"""
    while True:
        #1
        drivetrain.drive_for(FORWARD, 480 , MM)
        intake_motors.spin(FORWARD, 100, PERCENT)
        drivetrain.drive_for(FORWARD, 200 , MM)
        #2
        drivetrain.turn_for(RIGHT, 122, DEGREES)
        drivetrain.drive_for(REVERSE, 280, MM)
        motor_intake_2.spin(FORWARD, 100, PERCENT)
        drivetrain.drive_for(FORWARD, 1280, MM)
        #3
        drivetrain.turn_for(LEFT, 38, DEGREES)
        intake_motors.spin(FORWARD, 100, PERCENT)
        drivetrain.drive_for(REVERSE, 640, MM)
        motor_intake_2.spin(FORWARD, 100, PERCENT)
        
        #is this essential
        print("auton done")

        wait(20, MSEC)  
    
    

    


   
#Driving skill
def driver_control():
    toggle_state = False
    #match load
    last_pressed = False
    #outtake
    toggle_state_2 = False
    last_pressed_2 = False
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    #Driver_ctrl, can manage the speed depending on how much I tilt the joysticks
   
    def scale_input(x):
        return (x * abs(x)) / 100
    while True:
        speed = controller.axis3.position()
        turn = controller.axis1.position()

        #exp
        if -5 < speed < 5:
            speed = 0
        if -5 < turn < 5:
            turn = 0

        forward = scale_input(speed)
        rotate = scale_input(turn)

        left_speed = forward - rotate
        right_speed = forward + rotate

        left_motors.spin(DirectionType.FORWARD, left_speed, VelocityUnits.PERCENT)
        right_motors.spin(DirectionType.FORWARD, right_speed, VelocityUnits.PERCENT)
        

        '''
        left_motors.spin(FORWARD, speed - turn, PERCENT)
        right_motors.spin(FORWARD, speed + turn, PERCENT) 
        '''
         #codes from intake motors
        if controller.buttonR1.pressing():
            intake_motors.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL1.pressing():
            intake_motors.spin(FORWARD, -100, PERCENT)
        else:
            intake_motors.stop(COAST)
        
        if controller.buttonY.pressing():
            motor_intake_2.spin(FORWARD, 100, PERCENT)
        elif controller.buttonRight.pressing():
            motor_intake_2.spin(FORWARD, -100, PERCENT)
        else:
            motor_intake_2.stop(COAST)
        
        #Codes for Pneumatics
        if controller.buttonX.pressing() and last_pressed == False:
            toggle_state = not toggle_state
            if toggle_state:
                match_load.close()
            else:
                match_load.open()
        last_pressed = controller.buttonX.pressing()
        #Outtake piston 
        if controller.buttonUp.pressing() and last_pressed_2 == False:
            toggle_state_2 = not toggle_state_2
            if toggle_state_2:
                outtake_launcher.close()
            else:
                outtake_launcher.open()     
        last_pressed_2 = controller.buttonUp.pressing()   

 
    
        wait(20, MSEC)

    


# Tell VEX what *functions* we want to run when
Competition(driver_control, auton_long_goal_right)

