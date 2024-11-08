# Whether the robot is sped up or slowed down
# -1 = slowed
# 0 = normal speed
# 1 = sped up
speed_modifier = 0

# Default motor speed (percent) for drive motors
drive_speed = 75

# Whether the drive motors are reversed
drive_reversed = True

curvespy = str(bytes(brain.sdcard.loadfile('GRS/GRS_modules/driving_curves.py')), 'UTF-8')
exec(curvespy)

wait(1000, MSEC)

def set_drive_speed():
    global drive_speed

    if not speed_modifier:
        drive_speed = 75
    elif speed_modifier == 1:
        drive_speed = 125
    elif speed_modifier == 25:
        drive_speed = 25

def shift():
    global drive_speed
    global speed_modifier
    prev_mod = speed_modifier


    if controller.buttonL1.pressing():
        speed_modifier = -1
        drive_speed = 25
    elif controller.buttonR1.pressing():
        speed_modifier = 1
        drive_speed = 125

    if controller.buttonL1.pressing() and controller.buttonR1.pressing():
        speed_modifier = 0
        drive_speed = 75
    elif prev_mod == speed_modifier:
        speed_modifier  = 0
        drive_speed = 75

def dual_motor_drive():
    left_drive.spin(FORWARD, 0)
    right_drive.spin(FORWARD, 0)
    while True:
        set_drive_speed()
        get_driving_curve()

        if drive_reversed:
            l_velocity = (caxis1 - caxis3) * drive_speed / -100
            r_velocity = (caxis1 + caxis3) * drive_speed / -100
        else:
            l_velocity = (caxis1 + caxis3) * drive_speed / 100
            r_velocity = (caxis1 - caxis3) * drive_speed / 100
        left_drive.set_velocity(l_velocity, PERCENT)
        right_drive.set_velocity(r_velocity, PERCENT)

def quad_motor_drive():
    left_drive.spin(FORWARD, 0)
    right_drive.spin(FORWARD, 0)
    left_drive2.spin(FORWARD, 0)
    right_drive2.spin(FORWARD, 0)

    current_l_velocity = 0
    current_r_velocity = 0
    acceleration_step = 2

    while True:

        set_drive_speed()
        get_driving_curve()

        if drive_reversed:
            target_l_velocity = (caxis3 - caxis1) * drive_speed / -100
            target_r_velocity = (caxis3 + caxis1) * drive_speed / -100
        else:
            target_l_velocity = (caxis3 + caxis1) * drive_speed / 100
            target_r_velocity = (caxis3 - caxis1) * drive_speed / 100

        if current_l_velocity < target_l_velocity:
            current_l_velocity += acceleration_step
            if current_l_velocity > target_l_velocity:
                current_l_velocity = target_l_velocity
        elif current_l_velocity > target_l_velocity:
            current_l_velocity -= acceleration_step
            if current_l_velocity < target_l_velocity:
                current_l_velocity = target_l_velocity

        if current_r_velocity < target_r_velocity:
            current_r_velocity += acceleration_step
            if current_r_velocity > target_r_velocity:
                current_r_velocity = target_r_velocity
        elif current_r_velocity > target_r_velocity:
            current_r_velocity -= acceleration_step
            if current_r_velocity < target_r_velocity:
                current_r_velocity = target_r_velocity

        left_drive.set_velocity(current_l_velocity, PERCENT)
        right_drive.set_velocity(current_r_velocity, PERCENT)
        left_drive2.set_velocity(current_l_velocity, PERCENT)
        right_drive2.set_velocity(current_r_velocity, PERCENT)
        wait(5, MSEC)


        set_drive_speed()
        get_driving_curve()

        """if drive_reversed:
            l_velocity = (caxis3 - caxis1) * drive_speed / -100
            r_velocity = (caxis3 + caxis1) * drive_speed / -100
        else:
            l_velocity = (caxis3 + caxis1) * drive_speed / 100
            r_velocity = (caxis3 - caxis1) * drive_speed / 100
        left_drive.set_velocity(l_velocity, PERCENT)
        right_drive.set_velocity(r_velocity, PERCENT)
        left_drive2.set_velocity(l_velocity, PERCENT)
        right_drive2.set_velocity(r_velocity, PERCENT)"""

def toggle_reverse():
    global drive_reversed
    drive_reversed = not drive_reversed

def drive():
    if drive_motors == '2':
        dual_motor_drive()
    elif drive_motors == '4':
        quad_motor_drive()
    else:
        dual_motor_drive()