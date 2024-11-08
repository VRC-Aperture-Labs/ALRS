# Central file for the GLaDOS Robotics Suite by Aperture Labs
# (c) 2024 Aperture Labs

# ---------------------------------------------------------------- #

# GLoBAL variables for controller axis value
axis1 = 0
axis2 = 0
axis3 = 0
axis4 = 0

class button:
    def __init__(self, controller_button, index):
        self.index = index
        self.pressed = Event()
        self.released = Event()
        self.pressing = False
        controller_button.pressed(self.press)
        controller_button.released(self.release)

    def press(self):
        self.pressed.broadcast()
        self.pressing = True

    def release(self, function):
        self.released.broadcast()
        self.pressing = False

    def pressing(self):
        return self.pressing

    def get_index(self):
        return self.index

# Create events for all buttons on controller
class button_event_wrapper:
    def __init__(self, controller):
        self.l1 = button(controller.buttonL1, 4)
        self.l2 = button(controller.buttonL2, 5)
        self.r1 = button(controller.buttonR1, 6)
        self.r2 = button(controller.buttonR2, 7)
        self.left = button(controller.buttonLeft, 8)
        self.up = button(controller.buttonUp, 9)
        self.down = button(controller.buttonDown, 10)
        self.right = button(controller.buttonRight, 11)
        self.y = button(controller.buttonY, 12)
        self.x = button(controller.buttonX, 13)
        self.b = button(controller.buttonB, 14)
        self.a = button(controller.buttonA, 15)

    def get_button(index=4):
        for i in vars(self):
            if i.get_index() == index:
                return i
        return self.l1
            

    
buttons = button_event_wrapper(controller)
# ---------------------------------------------------------------- #

saashvik = str(bytes(brain.sdcard.loadfile('/GRS/independent_modules/saashvik.py')), 'UTF-8')
exec(saashvik)

config = format_config(str(bytes(brain.sdcard.loadfile('/GRS/script/config.saashvik')), 'UTF-8'))
brain.sdcard.savefile('/GRS/script/config.saashvik', config)

driving_curve = parse_var('driving_curve', config)
if not driving_curve:
    driving_curve = 'linear'

drive_motors = parse_var('drive_motors', config)
if not drive_motors:
    drive_motors = '2'

drivepy = str(bytes(brain.sdcard.loadfile('GRS/GRS_modules/drive.py')), 'UTF-8')
exec(drivepy)

Thread(drive)


alrs_mode = parse_var('alrs_mode', config)
if alrs_mode:
    alrs = parse_var('alrs', config)
    if alrs:
        if alrs_mode == 'record':
            recorder = str(bytes(brain.sdcard.loadfile('GRS/GRS_modules/ALRS_recorder.py')), 'UTF-8')
            exec(recorder)
        elif alrs_mode == 'run':
            interpreter = str(bytes(brain.sdcard.loadfile('GRS/GRS_modules/ALRS_interpreter.py')), 'UTF-8')
            exec(interpreter)
    else:
        brain.screen.set_pen_color(Color.RED)
        brain.screen.print('ERROR: ALRS FILE NOT SET IN CONFIG.')


exec_mode = parse_var('exec_mode', config)
if exec_mode == 'competion':
    competion_mode = True
    test_mode = False
else:
    competion_mode = False
    test_mode = True