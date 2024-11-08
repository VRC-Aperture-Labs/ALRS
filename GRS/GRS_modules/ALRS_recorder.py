brain.sdcard.savefile(alrs, bytearray())

def rec_ALRS(stop_event=Event()):
    stopped = False
    stop_event(stopped = True)
    brain.sdcard.appendFile(alrs, new_snapshot())
    alrs = new_snapshot()
    previous = button_event_wrapper(controller)

    i = 0
    while True:
        if stopped: break
        
        alrs[i] = create_snapshot(previous)
        previous = buttons
        i += i

        wait(25, MSEC)

    brain.sdcard.appendFile(alrs, alrs)

def new_snapshot():
    snapshot = []
    snapshot[0:16] = 0
    return snapshot

def create_snapshot(previous):
    # Returns current snapshot
    # Takes previous "buttons" object as argument

    global axis1
    global axis2
    global axis3
    global axis4

    snapshot = new_snapshot

    snapshot[0] = axis1
    snapshot[1] = axis2
    snapshot[2] = axis3
    snapshot[3] = axis4

    for i in range(4, 16):
        if buttons.get_button(i).pressing() != previous.get_button(i).pressing():
            if previous.get_button(i).pressing() == True:
                snapshot[i] = 2
            else:
                snapshot[i] = 1

    return snapshot
        
