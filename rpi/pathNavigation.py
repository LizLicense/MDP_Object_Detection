def turnRight(robot):
    #turn right
    if robot[2] == 0:
        robot[2] = 1.5
    else:
        robot[2] = robot[2] -0.5
        
def turnLeft(robot):
    #turn left
    if robot[2] == 1.5:
        robot[2] = 0
    else:
        robot[2] = robot[2] +0.5
        
def turn180(robot):
    #turn 180
    if robot[2] == 1.5:
        robot[2] = 0.5
    elif robot[2] == 1:
        robot[2] = 0
    else:
        robot[2] = robot[2] + 1
        
def mov1(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 - 1
    robot[1] = robot[1] + y2 - y1 - 1
    #turn right
    turnRight(robot)
    #go straight for x2 - x1 - 5
    robot[0] = robot[0] +  x2 - x1 - 5

def mov2(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    #go straight for y2 - y1 - 5
    robot[1] = robot[1] +  y2 - y1 - 5

def mov3(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go straight for y2 - y1 - 1
    robot[1] = robot[1] +  y2 - y1 - 1
    #turn left
    turnLeft(robot)

def mov4(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 + 3
    robot[1] = robot[1] + y2 - y1 + 3
    #turn right
    turnRight(robot)
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] +  x2 - x1 - 1
    #turn right
    turnRight(robot)
    
def mov5(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    robot[0] = robot[0] + x1 - x2 + 5
    #turn right
    turnRight(robot)
    #go straight for y2 - y1 - 1
    robot[1] = robot[1] +  y2 - y1 - 1
    #turn right
    turnRight(robot)

def mov6(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] + x1 - x2 + 1
    #turn right
    turnRight(robot)
    #go straight for y2 - y1 - 5
    robot[1] = robot[1] +  y2 - y1 - 5

def mov7(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 -1
    robot[1] = robot[1] + y2 - y1 -1
    #turn left
    turnLeft(robot)
    #go straight for x1 - x2 - 3
    robot[0] = robot[0] +  x1 - x2 - 3

def mov8(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 + 3
    robot[1] = robot[1] + y2 - y1 + 3
    #turn left
    turnLeft(robot)
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] +  x1 - x2 + 1
    #turn left
    turnLeft(robot)

def mov9(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] + y1 - y2 + 1
    #turn left
    turnLeft(robot)
    #go straight for x2 - x1 - 5
    robot[0] = robot[0] + x2 - x1 - 5

def mov10(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 5
    robot[1] = robot[1] + y1 - y2 + 5
    #turn left
    turnLeft(robot)
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    
def mov11(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn right
    turnRight(robot)
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] +  y1 - y2 + 1
    #turn right
    turnRight(robot)
    
def mov12(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn right
    turnRight(robot)
    #go straight for y1 - y2 - 3 
    robot[1] = robot[1] + y1 - y2 - 3 

def mov13(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    robot[0] = robot[0] + x1 - x2 + 5
    #turn left
    turnLeft(robot)
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] +  y1 - y2 + 1
    #turn left
    turnLeft(robot)

def mov14(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 5
    robot[1] = robot[1] + y1 - y2 + 5
    #turn right
    turnRight(robot)
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] + x1 - x2 + 1
    #turn right
    turnRight(robot)

def mov15(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] + y1 - y2 + 1
    #turn right
    turnRight(robot)
    #go straight for x1 - x2 - 3
    robot[0] = robot[0] + x1 - x2 - 3

def mov16(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] + x1 - x2 + 1
    #turn left
    turnLeft(robot)
    #go straight for y1 - y2 - 3
    robot[1] = robot[1] +  y1 - y2 - 3
   
def move(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    print('Origin',robot)
    if y2>y1: #top 
        if x2>x1: #right 
            print('Des is top right of robot')
            if theta2 == 1:
                if theta1 == 0.5:
                    mov1(robot,end)
                elif theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov1(robot,end)
                elif theta1 == 1.5:
                    #turn 180
                    turn180(robot)
                    mov1(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov1(robot,end)
            elif theta2 == 1.5:
                if theta1 == 0.5:
                    #turn right
                    turnRight(robot)
                    mov2(robot,end)
                elif theta1 == 0:
                    mov2(robot,end)
                elif theta1 == 1.5:
                    #turn left
                    turnLeft(robot)
                    mov2(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov2(robot,end)
            elif theta2 == 0:
                if theta1 == 0.5:
                    #turn right
                    turnRight(robot)
                    mov3(robot,end)
                elif theta1 == 0:
                    mov3(robot,end)
                elif theta1 == 1.5:
                    #turn left
                    turnLeft(robot)
                    mov3(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov3(robot,end)
            else:
                if theta1 == 0.5:
                    mov4(robot,end)
                elif theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov4(robot,end)
                elif theta1 == 1.5:
                    #turn 180
                    turn180(robot)
                    mov4(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov4(robot,end)
        elif x2<x1: #left 
            print('Des is top left of robot')
            if theta2 == 1:
                if theta1 == 0.5:
                    #turn left
                    turnLeft(robot)
                    mov5(robot,end)
                elif theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov5(robot,end)
                elif theta1 == 1.5:
                    #turn right
                    turnRight(robot)
                    mov5(robot,end)
                else:
                    mov5(robot,end)
            elif theta2 == 1.5: 
                if theta1 == 0.5:
                    #turn left
                    turnLeft(robot)
                    mov6(robot,end)
                elif theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov6(robot,end)
                elif theta1 == 1.5:
                    #turn right
                    turnRight(robot)
                    mov6(robot,end)
                else:
                    mov6(robot,end)
            elif theta2 == 0:
                if theta1 == 0.5:
                    mov7(robot,end)
                elif theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov7(robot,end)
                elif theta1 == 1.5:
                    #turn 180
                    turn180(robot)
                    mov7(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov7(robot,end)
            else:
                if theta1 == 0.5:
                    mov8(robot,end)
                elif theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov8(robot,end)
                elif theta1 == 1.5:
                    #turn 180
                    turn180(robot)
                    mov8(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov8(robot,end)
    elif y2<y1: #bottom 
        if x2>x1: #right 
            print('Des is bottom right of robot')
            if theta2 == 1:
                if theta1 == 0.5:
                    #turn 180
                    turn180(robot)
                    mov9(robot,end)
                elif theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov9(robot,end)
                elif theta1 == 1.5:
                    mov9(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov9(robot,end)
            elif theta2 == 1.5: 
                if theta1 == 0.5:
                    #turn 180
                    turn180(robot)
                    mov10(robot,end)
                elif theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov10(robot,end)
                elif theta1 == 1.5:
                    mov10(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov10(robot,end)
            elif theta2 == 0: 
                if theta1 == 0.5:
                    #turn right
                    turnRight(robot)
                    mov11(robot,end)
                elif theta1 == 0:
                    mov11(robot,end)
                elif theta1 == 1.5:
                    #turn left
                    turnLeft(robot)
                    mov11(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov11(robot,end)
            else: 
                if theta1 == 0.5:
                    #turn right
                    turnRight(robot)
                    mov12(robot,end)
                elif theta1 == 0:
                    mov12(robot,end)
                elif theta1 == 1.5:
                    #turn left
                    turnLeft(robot)
                    mov12(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov12(robot,end)
        elif x2<x1: #left 
            print('Des is bottom left of robot')
            if theta2 == 1:
                if theta1 == 0.5:
                    #turn left
                    turnLeft(robot)
                    mov13(robot,end)
                elif theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov13(robot,end)
                elif theta1 == 1.5:
                    #turn right
                    turnRight(robot)
                    mov13(robot,end)
                else:
                    mov13(robot,end)
            elif theta2 == 1.5: 
                if theta1 == 0.5:
                     #turn 180
                    turn180(robot)
                    mov14(robot,end)
                elif theta1 == 0:
                   #turn right
                    turnRight(robot)
                    mov14(robot,end)
                elif theta1 == 1.5:
                    mov14(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov14(robot,end)
            elif theta2 == 0: 
                if theta1 == 0.5:
                     #turn 180
                    turn180(robot)
                    mov15(robot,end)
                elif theta1 == 0:
                   #turn right
                    turnRight(robot)
                    mov15(robot,end)
                elif theta1 == 1.5:
                    mov15(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov15(robot,end)
            else: 
                if theta1 == 0.5:
                    #turn left
                    turnLeft(robot)
                    mov16(robot,end)
                elif theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov16(robot,end)
                elif theta1 == 1.5:
                    #turn right
                    turnRight(robot)
                    mov16(robot,end)
                else:
                    mov16(robot,end)
    print('end',robot)


