# Central file for the GLaDOS Robotics Suite by Aperture Labs
# (c) 2024 Aperture Labs

# ---------------------------------------------------------------- #

def null():
    # Empty function to use in callback to create events
    return

# Create events for all buttons on controller
class button_event_wrapper:
    l2_d = controller.buttonL2.pressed(null)
    l1_d = controller.buttonL1.pressed(null)
    r1_d = controller.buttonR1.pressed(null)
    r2_d = controller.buttonR2.pressed(null)
    l_d = controller.buttonLeft.pressed(null)
    u_d = controller.buttonUp.pressed(null)
    d_d = controller.buttonDown.pressed(null)
    r_d = controller.buttonRight.pressed(null)
    y_d = controller.buttonY.pressed(null)
    x_d = controller.buttonX.pressed(null)
    b_d = controller.buttonB.pressed(null)
    a_d = controller.buttonA.pressed(null)

    l1_u = controller.buttonL1.released(null)
    l2_u = controller.buttonL2.released(null)
    r1_u = controller.buttonR1.released(null)
    r2_u = controller.buttonR2.released(null)
    l_u = controller.buttonLeft.released(null)
    u_u = controller.buttonUp.released(null)
    d_u = controller.buttonDown.released(null)
    r_u = controller.buttonRight.released(null)
    y_u = controller.buttonY.released(null)
    x_u = controller.buttonX.released(null)
    b_u = controller.buttonB.released(null)
    a_u = controller.buttonA.released(null)

global buttons
buttons = button_event_wrapper()
# ---------------------------------------------------------------- #

config = str(open('/script/config.saashvik'))

