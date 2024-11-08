ALRS = str(brain.sdcard.loadfile('/GRS/script/autonomous.alrs'), 'UTF-8').replace(' ','').replace('\n',';').split(';')

def run_ALRS(stop_event=Event()):
    stopped = False
    stop_event(stopped = True)
    i = 0
    while True:
        if stopped: break
        
        interpret_snapshot(i)
        i += 1

        wait(25, MSEC)


def interpret_snapshot(index):
    # Sets all axis values
    # Activates events for all button presses
    # No return values

    global axis1
    global axis2
    global axis3
    global axis4

    snapshot = ALRS[index].split(',')

    axis1 = int(snapshot[0])
    axis2 = int(snapshot[1])
    axis3 = int(snapshot[2])
    axis4 = int(snapshot[3])

    for i in range(4, 16):
        if snapshot[i] != '0':
            if snapshot[i] == '1':
                buttons.get_button(i).press()
            elif snapshot[i] == '2':
                buttons.get_button(i).release()



    
