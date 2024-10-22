global axis1
global axis2
global axis3
global axis4

ALRS = str(open('/GRS/script/autonomous.alrs')).replace(' ','').replace('\n',';').split(';')

def interpret_snapshot(index):
    # Sets all axis values
    # Activates events for all button presses
    # No return values

    global axis1
    global axis2
    global axis3
    global axis4

    global controller

    snapshot = ALRS[index].split(',')

    axis1 = int(snapshot[0])
    axis2 = int(snapshot[1])
    axis3 = int(snapshot[2])
    axis4 = int(snapshot[3])

    if snapshot[4] != '0':
        if snapshot[4] == '1':
            l1.broadcast()




    
