from motor import*

# Forward movement
def forward1(): #move 10cm
    move_forward1(2.439)

def forward2():
    move_forward(2.408)
    
def forward3():
    move_forward(2.909)

def forward4():
    move_forward(3.505)

def forward5():
    move_forward(4.0118)
    
def forward6():
    move_forward(4.54)
    
def forward7():
    move_forward(5.1)

def forward8():
    move_forward(5.55)
    
def forward9():
    move_forward(6.117)

def forward10():
    move_forward(6.62)
    

# Backward Movement
def backward1():
    move_backward1(2.439)

def leftTurn90():
    move_backwardRight(3)
    move_forwardLeft(2)
    move_backward1(0.7)
    move_forwardLeft(1)
    move_backwardRight(1.1)
    move_backward1(0.23)
    
def rightTurn90():
    move_backwardLeft(3)
    move_forwardRight(2.2)
    move_backward1(0.7)
    move_forwardRight(1)
    move_backwardLeft(0.9)
    move_backward1(0.6)


def active_car(msg):
        if msg == 'w1':
            forward1()
        elif msg == 'w2':
            forward2()
        elif msg == 'w3':
            forward3()
        elif msg == 'w4':
            forward4()
        elif msg == 'w5':
            forward5()
        elif msg == 'w6':
            forward6()
        elif msg == 'w7':
            forward7()
        elif msg == 'w8':
            forward8()
        elif msg == 'w9':
            forward9()
        elif msg == 'w10':
            forward10()
    
        #Backward movement    
        elif msg == 's1':
            backward1()
            
        #Left and Right Turn
        elif msg == 'a':
            leftTurn90()
        elif msg == 'd':
            rightTurn90()
        elif msg == 'p':
            mover_stop()

#def main():
#    time.sleep(0.1)
#    active_car('w1')
    
    
    
#if __name__ == "__main__":
#    main()


    

