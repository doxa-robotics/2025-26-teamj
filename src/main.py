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
motor_left_1 = Motor(Ports.PORT3, True)
motor_left_2 = Motor(Ports.PORT4, True)
motor_left_3 = Motor(Ports.PORT5, False)
motor_right_1 = Motor(Ports.PORT9, False)
motor_right_2 = Motor(Ports.PORT8, False)
motor_right_3 = Motor(Ports.PORT7, True)



#for match_load 1 is extend and 2 is retract
left_motors = MotorGroup(motor_left_1, motor_left_2, motor_left_3)
right_motors = MotorGroup(motor_right_1, motor_right_2, motor_right_3)
motor_intake = Motor(Ports.PORT10, False)
motor_intake_2 = Motor(Ports.PORT20, False)
intake_motors = MotorGroup(motor_intake)
intake_outtake_motors = MotorGroup(motor_intake, motor_intake_2)
match_load = Pneumatics(brain.three_wire_port.d)
outtake_launcher = Pneumatics(brain.three_wire_port.c)

#Gyroscope
inertial = Inertial(Ports.PORT11)

drivetrain = SmartDrive(
    left_motors,
    right_motors,
    inertial,
    300,
    320,
    320,
    MM
)


    
#Autonomous
brain.screen.clear_screen()
brain.screen.print("autonomous code")
     

def auton_long_goal_right():
    """Auton"""
    drivetrain.set_drive_velocity(75, RPM)
    #1: Take 3 balls
    intake_motors.spin(FORWARD, 100, PERCENT)
    drivetrain.drive_for(FORWARD, 528, MM)
    wait(500, MSEC) 
    intake_motors.stop()
    #2: Put balls in the upper goal
    drivetrain.turn_for(LEFT, 103, DEGREES)            
    drivetrain.drive_for(REVERSE, 230, MM)
    intake_outtake_motors.spin(FORWARD, 100, PERCENT)
    wait(1600, MSEC)
    intake_outtake_motors.stop()
    wait(50, MSEC)
    #3: Go to ball pillar
    drivetrain.set_drive_velocity(74, RPM)
    match_load.open()  
    drivetrain.turn_for(LEFT, 17, DEGREES)
    drivetrain.drive_for(FORWARD, 850, MM)
    wait(50, MSEC)
    outtake_launcher.open() 
    #4: Matchload, take 3 balls
    drivetrain.set_drive_velocity(100, RPM)
    drivetrain.turn_for(LEFT, 38, DEGREES)
    #match_load.open()
    intake_motors.spin(FORWARD, 100, PERCENT)
    drivetrain.set_drive_velocity(50,RPM)
    drivetrain.drive_for(FORWARD, 300, MM)
    wait(1500, MSEC)
    intake_motors.stop()
    #5: Go to the long goal, put 3 balls in.
    drivetrain.set_drive_velocity(85, RPM)
    drivetrain.drive_for(REVERSE, 655, MM)
    #outtake_launcher.open()
    intake_outtake_motors.spin(FORWARD, 150, PERCENT)
    wait(1500, MSEC)
    match_load.close()
    outtake_launcher.close()
    intake_outtake_motors.stop()
    #Done
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
    left_actual = 0
    right_actual = 0
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    #Driver_ctrl, can manage the speed depending on how much I tilt the joysticks
   
    def scale_input(x):
        return (x * abs(x)) / 100
    
    def fast_rate_limit(current_speed, target_speed, step=5):
        if target_speed > current_speed + step:
            return current_speed + step
        elif target_speed < current_speed - step:
            return current_speed - step
        else:
            return target_speed
        
    while True:
        speed = controller.axis3.position()
        turn = controller.axis1.position()

        #exp
        if -5 < speed < 5   :
            speed = 0
        if -5 < turn < 5:
            turn = 0

        forward = scale_input(speed)
        rotate = scale_input(turn)

        left_speed = forward + rotate
        right_speed = forward - rotate

        left_actual = fast_rate_limit(left_actual, left_speed, step=5)
        right_actual = fast_rate_limit(right_actual, right_speed, step=5)

        left_motors.spin(DirectionType.FORWARD, left_actual, VelocityUnits.PERCENT)
        right_motors.spin(DirectionType.FORWARD, right_actual, VelocityUnits.PERCENT)



        '''
        left_motors.spin(DirectionType.FORWARD, left_speed, VelocityUnits.PERCENT)
        right_motors.spin(DirectionType.FORWARD, right_speed, VelocityUnits.PERCENT)
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
                match_load.open()
            else:
                match_load.close()
        last_pressed = controller.buttonX.pressing()
       
        #Outtake piston 
        if controller.buttonUp.pressing() and last_pressed_2 == False:
            toggle_state_2 = not toggle_state_2
            if toggle_state_2:
                outtake_launcher.open()
            else:
                outtake_launcher.close()     
        last_pressed_2 = controller.buttonUp.pressing()   

 
    
        wait(20, MSEC)

    


# Tell VEX what *functions* we want to run when
Competition(driver_control, auton_long_goal_right)





