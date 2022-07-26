import copy
from glob import glob

### Variable declaration
initialState = []
initialState1 = []
states = []
goalState = []
latestState =[]
numOfState = 0
roomWithVacuum = []

### clean the room with vacuum
def clean(state, k, roomWithVacuum, i):
    global states
    global goalState
    for j in range(i,k):  
        if list(state[0][j].keys())[1] == roomWithVacuum:
            if state[0][j][roomWithVacuum] == '1':
                temp = copy.deepcopy(state[0])
                states.append(temp)
                states[-1][j][roomWithVacuum] = '0'
                break
            else:
                break

### move vacuum to the room in right 
def moveRight(state, k, roomWithVacuum, i):
    global states
    p = 0
    for j in range(i, k):
        if list(state[0][j].keys())[1] == roomWithVacuum:
            p = j   # we have to find the position of the room with vacuum 
            break   # so that we will figure out if we can go right of left
        else:
            continue
    if len(states[0]) > p:
        temp = copy.deepcopy(states[-1])
        states.append(temp)
        states[-1][p][list(state[0][p+1].keys())[0]] = '0'
        states[-1][p+1][list(state[0][p+1].keys())[0]] = '1'
    return states

### move vacuum to the room in right 
def moveLeft(state, k, roomWithVacuum, i):
    global states
    p = 0
    for j in range(i, k):
        if list(state[0][j].keys())[1] == roomWithVacuum:
            p = j   # we have to find the position of the room with vacuum 
            break   # so that we will figure out if we can go right of left
        else:
            continue
    if p != 0:
        temp = copy.deepcopy(states[-1])
        states.append(temp)
        states[-1][p][list(state[0][p-1].keys())[0]] = '0'
        states[-1][p-1][list(state[0][p-1].keys())[0]] = '1'
    return states

### Recursive function to find room name with vacuum
def findVacuum(state, k, i):
    room = list(state[0][i].keys())
    if i < k:
        if state[0][i][room[0]] == '1':
            # print("Vacuum is in room " + room[1])
            return [i, room[1]]
        else:
            i = i+1
            return findVacuum(state, k, i)
    else:
        pass

def vacuumWorld():
    ### Define Initial States
    intNumOfRoom = int(input("Enter the number of room: "))
    for i in range(0, intNumOfRoom):
        roomName = input("Enter room name: ")
        dirtStatus = input("Enter status of dirt in " + roomName + " (clean/dirty - 0/1): ")    # clean/dirty (0/1)
        vacuumStatus = input("Enter status of vacuum in " + roomName + "(absent/present - 0/1): ")  # absent/present (0/1)
        initialState.append({'V': vacuumStatus, roomName: dirtStatus})  # representation: [{}, {}, ...]
    initialState1.append(initialState)  # Final representation: [[{}, {}, ...], [{}, {}, ...], ...]
    ### Initial States complete

    ### define Goal States:
    global goalState
    goalState = copy.deepcopy(initialState1)
    for i in range(0, intNumOfRoom):
        for j in range(0, intNumOfRoom):
            if i == j:
                goalState[i][j][list(goalState[i][j].keys())[1]] = '0'
                goalState[i][j][list(goalState[i][j].keys())[0]] = '1'
                continue
            else:
                goalState[i][j][list(goalState[i][j].keys())[0]] = '0'
                goalState[i][j][list(goalState[i][j].keys())[1]] = '0'
        temp = copy.deepcopy(goalState[0])
        goalState.append(temp)
    goalState.pop(-1)
    ### Goal States complete

    global states
    global latestState
    global roomWithVacuum
    states = copy.deepcopy(initialState1)
    i = 0
    roomWithVacuum = findVacuum(initialState1, intNumOfRoom, i=0)
    # Case 1:
    if roomWithVacuum[0] == 0:
        while not (states[-1] in goalState):
            latestState.append(states[-1])
            roomWithVacuum = findVacuum(latestState, intNumOfRoom, i=0)
            clean(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
            if list(states[-1][-1].keys())[1] != roomWithVacuum[1]:
                if len(states) > i:
                    i += 1
                    latestState.pop(-1)
                    latestState.append(states[-1])
                    moveRight(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                i += 1
                latestState.pop(-1)
    # Case 2:
    elif roomWithVacuum[0] == len(initialState1[0])-1:
        while not (states[-1] in goalState):
            latestState.append(states[-1])
            roomWithVacuum = findVacuum(latestState, intNumOfRoom, i=0)
            clean(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
            if list(states[-1][0].keys())[1] != roomWithVacuum[1]:
                if len(states) > i:
                    i += 1
                    latestState.pop(-1)
                    latestState.append(states[-1])
                    moveLeft(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                i += 1
                latestState.pop(-1)
    # Case 3:
    elif (roomWithVacuum[0] - 0) >= (intNumOfRoom-roomWithVacuum[0]-1):
        while not (states[-1] in goalState):
            latestState.append(states[-1])
            roomWithVacuum = findVacuum(latestState, intNumOfRoom, i=0)
            clean(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
            if roomWithVacuum[0] == len(initialState1[0])-1:
                while not (states[-1] in goalState):
                    latestState.pop(-1)
                    latestState.append(states[-1])
                    roomWithVacuum = findVacuum(latestState, intNumOfRoom, i=0)
                    clean(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                    if list(states[-1][0].keys())[1] != roomWithVacuum[1]:
                        if len(states) > i:
                            i += 1
                            latestState.pop(-1)
                            latestState.append(states[-1])
                            moveLeft(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                        i += 1
                break
            if list(states[-1][-1].keys())[1] != roomWithVacuum[1]:
                if len(states) > i:
                    i += 1
                    latestState.pop(-1)
                    latestState.append(states[-1])
                    moveRight(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                i += 1
                latestState.pop(-1)
    # Case 4
    elif (roomWithVacuum[0] - 0) < (intNumOfRoom-roomWithVacuum[0]):
        while not (states[-1] in goalState):
            latestState.append(states[-1])
            roomWithVacuum = findVacuum(latestState, intNumOfRoom, i=0)
            clean(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
            if roomWithVacuum[0] == 0:
                while not (states[-1] in goalState):
                    latestState.pop(-1)
                    latestState.append(states[-1])
                    roomWithVacuum = findVacuum(latestState, intNumOfRoom, i=0)
                    clean(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                    if list(states[-1][-1].keys())[1] != roomWithVacuum[1]:
                        if len(states) > i:
                            i += 1
                            latestState.pop(-1)
                            latestState.append(states[-1])
                            moveRight(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                        i += 1
                break
            if list(states[-1][0].keys())[1] != roomWithVacuum[1]:
                if len(states) > i:
                    i += 1
                    latestState.pop(-1)
                    latestState.append(states[-1])
                    moveLeft(latestState, intNumOfRoom, roomWithVacuum[1], i=0)
                i += 1
                latestState.pop(-1)
    else:
        print("There shouldn't be any problem. I don't know why you get this message.")
        print("I hope you figure out the bug and send a pull request. Thank you 😀😀")

    print("Initial State: ", end="")
    print(states[0])
    states.pop(0)
    for i in range(0, len(states)):
        print(states[i])
    print("Optimum number of state: " + str(len(states)))

vacuumWorld()