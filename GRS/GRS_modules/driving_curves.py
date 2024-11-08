def set_axes():
    global axis1
    global axis2
    global axis3
    global axis4

    axis1 = controller.axis1.position()
    axis2 = controller.axis2.position()
    axis3 = controller.axis3.position()
    axis4 = controller.axis4.position()

def linear_curve():
    global caxis1
    global caxis2
    global caxis3
    global caxis4

    axes = [axis1, axis2, axis3, axis4]

    caxis1, caxis2, caxis3, caxis4 = axes

def exponential_curve():
    global caxis1
    global caxis2
    global caxis3
    global caxis4

    axes = [axis1, axis2, axis3, axis4]

    for axis in axes:
        negative = False
        if axis < 0:
            axis *= -1
            negative = True

        if axis < 10:
            axis = 0
        else:
            axis = 1.25 ** axis

        if negative:
            axis *= -1

    caxis1, caxis2, caxis3, caxis4 = axes

def quadratic_curve():
    global caxis1
    global caxis2
    global caxis3
    global caxis4

    axes = [axis1, axis2, axis3, axis4]

    for axis in axes:
        if axis < 10:
            axis = 0
        else:
            axis = axis ** 2

    caxis1, caxis2, caxis3, caxis4 = axes

def get_driving_curve():
    set_axes()
    driving_curve = 'exponential'
    if driving_curve == 'linear':
        linear_curve()
    elif driving_curve == 'exponential':
        exponential_curve()
    elif driving_curve == 'quadratic':
        quadratic_curve()
    else:
        linear_curve()