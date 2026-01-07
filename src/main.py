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
motor_intake_2 = Motor(Ports.PORT19, False)
intake_motors = MotorGroup(motor_intake)
intake_outtake_motors = MotorGroup(motor_intake, motor_intake_2)
match_load = Pneumatics(brain.three_wire_port.d)
outtake_launcher = Pneumatics(brain.three_wire_port.c)
wing = Pneumatics(brain.three_wire_port.a)

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
    drivetrain.set_drive_velocity(77, RPM)
    #1: Take 3 balls
    intake_motors.spin(FORWARD, 100, PERCENT)
    drivetrain.drive_for(FORWARD, 528, MM)
    wait(400, MSEC) 
    intake_motors.stop()
    #2: Put balls in the upper goal
    drivetrain.turn_for(LEFT, 103, DEGREES)            
    drivetrain.drive_for(REVERSE, 185, MM)
    intake_outtake_motors.spin(FORWARD, 100, PERCENT)
    wait(700, MSEC)
    intake_outtake_motors.stop()
    wait(50, MSEC)
    #3: Go to ball pillar
    drivetrain.set_drive_velocity(90, RPM)
    match_load.open()  
    drivetrain.turn_for(LEFT, 17, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    wait(50, MSEC)
    outtake_launcher.open() 
    #4: Matchload, take 3 balls
    drivetrain.set_drive_velocity(100, RPM)
    drivetrain.turn_for(LEFT, 38, DEGREES)
    #match_load.open()
    intake_motors.spin(FORWARD, 150, PERCENT)
    drivetrain.set_drive_velocity(50,RPM)
    drivetrain.drive_for(FORWARD, 215, MM)
    wait(400, MSEC)
    intake_motors.stop()
    #5: Go to the long goal, put 3 balls in.
    drivetrain.set_drive_velocity(80, RPM)
    drivetrain.drive_for(REVERSE, 465, MM)
    #outtake_launcher.open()
    intake_outtake_motors.spin(FORWARD, 150, PERCENT)
    wait(1300, MSEC)
    match_load.close()
    outtake_launcher.close()
    intake_outtake_motors.stop()
    #Done
    print("auton done")

    wait(20, MSEC)  

    
def auton_long_goal_left():
    """auton2"""
    drivetrain.set_drive_velocity(77, RPM)
    #1: Take 3 balls
    intake_motors.spin(FORWARD, 100, PERCENT)
    drivetrain.drive_for(FORWARD, 528, MM)
    wait(500, MSEC) 
    intake_motors.stop()
    #2: Put balls in the upper goal
    drivetrain.turn_for(LEFT, 77, DEGREES)  
    ###################i worked till here          
    drivetrain.drive_for(REVERSE, 199, MM)
    intake_motors.spin(FORWARD, 100, PERCENT)
    wait(1200, MSEC)
    intake_motors.stop()
    wait(50, MSEC)
    #3: Go to ball pillar
    drivetrain.set_drive_velocity(90, RPM)
    match_load.open()  
    drivetrain.turn_for(LEFT, 17, DEGREES)
    drivetrain.drive_for(FORWARD, 830, MM)
    wait(50, MSEC)
    outtake_launcher.open() 
    #4: Matchload, take 3 balls
    drivetrain.set_drive_velocity(100, RPM)
    drivetrain.turn_for(LEFT, 142, DEGREES)
    #match_load.open()
    intake_motors.spin(FORWARD, 150, PERCENT)
    drivetrain.set_drive_velocity(50,RPM)
    drivetrain.drive_for(FORWARD, 173, MM)
    wait(1000, MSEC)
    intake_motors.stop()
    #5: Go to the long goal, put 3 balls in.
    drivetrain.set_drive_velocity(80, RPM)
    drivetrain.drive_for(REVERSE, 475, MM)
    #outtake_launcher.open()
    intake_outtake_motors.spin(FORWARD, 150, PERCENT)
    wait(1500, MSEC)
    match_load.close()
    outtake_launcher.close()
    intake_outtake_motors.stop()
    #Done
    print("auton done")
    

def auton_long_goal_lower_right():
    """Auton Lower goal"""
    drivetrain.set_drive_velocity(100)
    drivetrain.drive_for(FORWARD, 640, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    intake_motors.spin(FORWARD, 150, PERCENT)
    drivetrain.drive_for(FORWARD, 840, MM)
    wait(50, MSEC)
    intake_motors.stop()
    intake_motors.spin(REVERSE, 150, PERCENT)
    wait(300, MSEC)
    intake_motors.stop()
    drivetrain.drive_for(REVERSE, 1160, MM)
    match_load.open()
    intake_motors.spin(FORWARD, 150, PERCENT)
    drivetrain.turn_for(LEFT, 135, DEGREES)
    drivetrain.drive_for(FORWARD, 240, MM)
    wait(500, MSEC)
    intake_motors.stop()
    outtake_launcher.open()
    drivetrain.drive_for(REVERSE, 600, MM)
    intake_outtake_motors.spin(FORWARD, 150, PERCENT)
    wait(1000, MSEC)
    intake_outtake_motors.stop()
    #DONE



   
#Driving skill
def driver_control():
   #x axis
   
    toggle_state = False
    #match load
    last_pressed = False
    #outtake
    toggle_state_2 = False
    last_pressed_2 = False
    #wing
    toggle_stage_3 = False
    last_pressed_3 = False
    #Drive
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
        speed = controller.axis3.position() *0.9
        turn = controller.axis1.position()  *0.9

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
        elif controller.buttonR2.pressing():
            intake_motors.spin(FORWARD, -100, PERCENT)
        else:
            intake_motors.stop(COAST)
        
        if controller.buttonL1.pressing():
            motor_intake_2.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL2.pressing():
            motor_intake_2.spin(FORWARD, -100, PERCENT)
        else:
            motor_intake_2.stop(COAST)
        
        #Codes for Pneumatics, matchload
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

        #wing
        if controller.buttonA.pressing() and last_pressed_3 == False:
            toggle_stage_3 = not toggle_stage_3
            if toggle_stage_3:
                wing.open()
            else:
                wing.close()
        last_pressed_3 = controller.buttonA.pressing()
    
        wait(20, MSEC)

    


# Tell VEX what *functions* we want to run when
Competition(driver_control, auton_long_goal_lower_right)




