from time import sleep
from tkinter import *
import tkinter.ttk as ttk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename
from active_move import*
from detect1 import*

import config
from comms import *
from constants import *
from handler import Handler
from map import *
from hamiltonianPath import *
import re
import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
import time
import os
from bullseyeTurn import*
from communicator.androidComm import AndroidToRpi

#N = 0 
#E = 90
#S = 180
#W = 270

robot = [0,0,90]
#obstacle_android = [[1,8,90],[5,4,270],[0,18,90],[13,10,180],[6,15,180]]
obstacle_android = AndroidToRpi()

#TODO  @nyi need to add this to convert dict into a 1d list
#displayList = []
#for camId,coord in d1.items():
#    displayList.append(str(k))
#    for num in v:
#        displayList.append(str(num))
#======endToDo



hamiltonianPath = shortestPath(obstacle_android)
print('Obstacle List: ',obstacle_android)
print('Hamiltonian Path: ',hamiltonianPath) #hamiltonian Path

end = hamiltonianPath 
for i in range(0, len(hamiltonianPath)): 
    map_sim[19-end[i][1]][end[i][0]] = 1

class ObstacleID:
    k = 0

class Simulator:
    def __init__(self):
        self.robot_simulation = True

        self.root = Tk()
        self.root.title("Robot Car Simulator")
        self.root.resizable(False, False)
        self.job = None

        self.map_start_end = PhotoImage(file=config.image_paths['red'])
        self.map_unexplored = PhotoImage(file=config.image_paths['gray'])
        self.map_obstacle_unexplored = PhotoImage(file=config.image_paths['blue'])
        self.map_free = PhotoImage(file=config.image_paths['green'])
        self.map_obstacle = PhotoImage(file=config.image_paths['pink'])

        self.handler = Handler(self)
        self.map = self.handler.map
        self.core = self.handler.core
        self.robot = self.handler.get_robot()
        self.robot_n = []
        self.robot_e = []
        self.robot_s = []
        self.robot_w = []
        for i in range(3):
            self.robot_n.append([])
            self.robot_e.append([])
            self.robot_s.append([])
            self.robot_w.append([])
            for j in range(3):
                self.robot_n[i].append(config.robot_grid['north'][i][j])
                self.robot_e[i].append(config.robot_grid['east'][i][j])
                self.robot_s[i].append(config.robot_grid['south'][i][j])
                self.robot_w[i].append(config.robot_grid['west'][i][j])
        
        t = Toplevel(self.root)
        t.title("Controller")
        t.geometry('+610+0')
        t.resizable(False, False)

        self.canvas = Canvas(self.root, width=40 * config.map_size['width'], height=40 * config.map_size['height'])
        self.canvas.pack()

        self.control_panel = ttk.Frame(t, padding=(20, 20))
        self.control_panel.grid(row=0, column=1, sticky="snew")

        control_pane_window = ttk.Panedwindow(self.control_panel, orient=VERTICAL)
        control_pane_window.grid(column=0, row=0, sticky=(N, S, E, W))
        parameter_pane = ttk.Frame(control_pane_window)
        action_pane = ttk.Frame(control_pane_window)
        parameter_pane.grid(column=0, row=0, sticky=(N, S, E, W))
        action_pane.grid(column=0, row=1, pady=(10, 0), sticky=(N, S, E, W))

        self.steps_per_second = StringVar()
        self.coverage_figure = StringVar()
        self.time_limit = StringVar()
        self.waypoint_x = StringVar()
        self.waypoint_y = StringVar()
        self.goal_x = StringVar()
        self.goal_y = StringVar()
        self.ip_addr = StringVar()

        #explore_button = ttk.Button(action_pane, text='Explore', command=self.explore, width=20)
        #explore_button.grid(column=0, row=0, sticky="ew",padx=5, pady=10)
        algo_label = ttk.Label(action_pane, text="Algorithm: ")
        algo_label.grid(column=0, row=0, sticky="ew",padx=0, pady=0)
        start_button = ttk.Button(action_pane, text='Hamiltonian Path', command=self.start, width=30)
        start_button.grid(column=0, row=1, sticky="ew",padx=5, pady=20)
        startall_button = ttk.Button(action_pane, text='Hamiltonian Path', command=self.start, width=30)
        startall_button.grid(column=0, row=5, sticky="ew",padx=5, pady=20)

        #fastest_path_button = ttk.Button(action_pane, text='Fastest Path', command=self.findFP)
        #fastest_path_button.grid(column=0, row=1, sticky="ew")
        
        move_button = ttk.Button(action_pane, text='Move', command=self.move)
        move_button.grid(column=0, row=5, sticky="ew")
        left_button = ttk.Button(action_pane, text='Left', command=self.left)
        left_button.grid(column=0, row=3, sticky="ew")
        right_button = ttk.Button(action_pane, text='Right', command=self.right)
        right_button.grid(column=0, row=4, sticky="ew")
        #load_button = ttk.Button(action_pane, text='Load Map', command=self.load)
        #load_button.grid(column=0, row=6, sticky="ew")
        #reset_button = ttk.Button(action_pane, text='Reset', command=self.reset)
        #reset_button.grid(column=0, row=7, sticky="ew")
        
        #self.text_area = scrolledtext.ScrolledText(control_pane_window, wrap=WORD, width=35, height=10)
        #self.text_area.grid(row=2, column=0, pady=(20, 10))

        #step_per_second_label = ttk.Label(parameter_pane, text="Steps Per Second:")
        #step_per_second_label.grid(column=0, row=0, sticky="ew")
        #step_per_second_entry = ttk.Entry(parameter_pane, textvariable=self.steps_per_second, width=33)
        #step_per_second_entry.grid(column=0, row=1, pady=(0, 10), sticky="ew")

        #coverage_figure_label = ttk.Label(parameter_pane, text="Coverage Figure(%):")
        #coverage_figure_label.grid(column=0, row=2, sticky="ew")
        #coverage_figure_entry = ttk.Entry(parameter_pane, textvariable=self.coverage_figure)
        #coverage_figure_entry.grid(column=0, row=3, pady=(0, 10), sticky="ew")

        #time_limit_label = ttk.Label(parameter_pane, text="Time Limit(s):")
        #time_limit_label.grid(column=0, row=4, sticky="ew")
        #time_limit_entry = ttk.Entry(parameter_pane, textvariable=self.time_limit)
        #time_limit_entry.grid(column=0, row=5, pady=(0, 10), sticky="ew")

        #waypoint_label = ttk.Label(parameter_pane, text="Waypoint(x,y):")
        #waypoint_label.grid(column=0, row=6, sticky="ew")
        #waypoint_frame = ttk.Frame(parameter_pane)
        #waypoint_x_entry = ttk.Entry(waypoint_frame, textvariable=self.waypoint_x, width=16)
        #waypoint_y_entry = ttk.Entry(waypoint_frame, textvariable=self.waypoint_y, width=16)
        #waypoint_frame.grid(column=0, row=7)
        #waypoint_x_entry.grid(column=0, row=0, pady=(0, 10), sticky="w")
        #waypoint_y_entry.grid(column=1, row=0, pady=(0, 10))

        #goal_label = ttk.Label(parameter_pane, text="Goal(x,y):")
        #goal_label.grid(column=0, row=8, sticky=EW)
        #goal_frame = ttk.Frame(parameter_pane)
        #goal_x_entry = ttk.Entry(goal_frame, textvariable=self.goal_x, width=16)
        #goal_y_entry = ttk.Entry(goal_frame, textvariable=self.goal_y, width=16)
        #goal_frame.grid(column=0, row=9)
        #goal_x_entry.grid(column=0, row=0, pady=(0, 10), sticky=W)
        #goal_y_entry.grid(column=1, row=0, pady=(0, 10))

        control_label = ttk.Label(action_pane, text="Manual Control: ")
        control_label.grid(column=0, row=2, sticky="ew")
        #self.exploration_dropdown = ttk.Combobox(parameter_pane, state="readonly",
        #                                         values=["Left Wall Hugging", "Left Wall Hugging (Return Home)",
        #                                                 "Left Wall Hugging (Optimized, Return Home)",
        #                                                 "Image Recognition", "Image Recognition (Return Home)",
        #                                                 "Image Recognition (Partial, Return Home)"])
        #self.exploration_dropdown.current(3)
        #self.exploration_dropdown.grid(column=0, row=11, pady=(0, 10), sticky=EW)

        #fp_algo_label = ttk.Label(parameter_pane, text="FP Algo:")
        #fp_algo_label.grid(column=0, row=12, sticky=EW)
        #self.fp_dropdown = ttk.Combobox(parameter_pane, state="readonly",
        #                                values=["A* Search", "A* Search (With Diagonals)", "Left Wall Hugging"])
        #self.fp_dropdown.current(1)
        #self.fp_dropdown.grid(column=0, row=13, pady=(0, 10), sticky=EW)

        #self.ip_addr.set('192.168.20.1')
        #ip_addr_label = ttk.Label(parameter_pane, text="IP Address:")
        #ip_addr_label.grid(column=0, row=14, sticky=EW)
        #ip_addr_entry = ttk.Entry(parameter_pane, textvariable=self.ip_addr)
        #ip_addr_entry.grid(column=0, row=15, pady=(0, 0), sticky=EW)

        #self.connect_button = ttk.Button(parameter_pane, text='Connect', command=self.connect)
        #self.connect_button.grid(column=0, row=16, pady=(0, 10), sticky=EW)

        self.coverage_figure.set(100)
        self.time_limit.set(360)
        self.steps_per_second.set(-1)
        self.waypoint_x.set(0)
        self.waypoint_y.set(0)
        self.goal_x.set(13)
        self.goal_y.set(1)

        #self.control_panel.columnconfigure(0, weight=1)
        #self.control_panel.rowconfigure(0, weight=1)

        self.update_map(full=True)
        self.event_loop()
        self.root.mainloop()
        
    def checkmove(self,count):
        if count == 2:
            active_car('w2')
        elif count == 3:
            active_car('w3')
        elif count == 4:
            active_car('w4')
        elif count == 5:
            active_car('w5')
        elif count == 6:
            active_car('w6')
        elif count == 7:
            active_car('w7')
        elif count == 8:
            active_car('w8')
        elif count == 9:
            active_car('w9')
        elif count == 10:
            active_car('w10')
        else:
            active_car('w1')
            
    def avoidgoal(self,robot):
        if robot[2] == 0:
            Simulator.turnRight(robot,self)
            Simulator.move()
            Simulator.move()
            Simulator.turnLeft(robot, self)
            robot[0] = robot[0]+2
        elif robot[2] == 90:
            Simulator.turnRight(robot,self)
            Simulator.move()
            Simulator.move()
            Simulator.turnLeft(robot, self)
            robot[1] = robot[1]-2
        elif robot[2] == 180:
            Simulator.turnRight(robot, self)
            Simulator.move()
            Simulator.move()
            Simulator.turnLeft(robot, self)
            robot[0] = robot[0] - 2
        elif robot[2] == 270:
            Simulator.turnRight(robot,self)
            Simulator.move()
            Simulator.move()
            Simulator.turnLeft(robot, self)
            robot[1] = robot[1]+2   
    
    def event_loop(self):

        while not general_queue.empty():
            msg = general_queue.get()

            if msg[:3] == START_EXPLORATION:
                logging.debug('Starting exploration')
                self.explore()
            elif msg[:3] == START_FASTEST_PATH:
                logging.debug('Starting fp')
                self.findFP()
            elif msg[:3] == WAYPOINT:
                logging.debug('Waypoint set')
                xy = msg.split('|')
                self.waypoint_x.set(int(xy[1]))
                self.waypoint_y.set(abs(19 - int(xy[2])))
                logging.debug('Waypoint set: ' + str(self.waypoint_x.get()) + ", " + str(self.waypoint_y.get()))
            elif msg[:3] == RESET:
                self.reset()
            elif msg[:3] == GET_MAP:
                self.robot.send_map()
            elif msg == STOP_IR:
                self.core.explorer.stop_ir()
                logging.debug('Stopping IR')

        self.root.after(200, self.event_loop)

    def explore(self):
        self.core.explore(int(self.steps_per_second.get()), int(self.coverage_figure.get()),
                          int(self.time_limit.get()), self.exploration_dropdown.get())

    def findFP(self):
        self.core.findFP(int(self.steps_per_second.get()), int(self.goal_x.get()), int(self.goal_y.get()),
                         int(self.waypoint_x.get()), int(self.waypoint_y.get()), self.fp_dropdown.get())

    def update_cell(self, x, y):
        # Start & End box
        #if x==15:
        #    color = 'pink'

        if map_is_explored[y][x] == 0:
            if map_sim[y][x] == 0:
                color = 'pink'
            else:
                color = 'red'
        else:
            if self.map.is_free(x, y, False):
                color = 'pink'
            else:
                color = 'red'

        if not config.map_cells[y][x]:
            config.map_cells[y][x] = self.canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill=color)
            self.canvas.bind('<ButtonPress-1>', self.on_click)
        else:
            self.canvas.itemconfig(config.map_cells[y][x], fill=color)

    def on_click(self, event):
        x = event.x // 40
        y = event.y // 40

        if map_sim[y][x] == 0:
            map_sim[y][x] = 1
        else:
            map_sim[y][x] = 0
        self.update_cell(x, y)

    def put_robot(self, x, y, bearing):
        if bearing == Bearing.NORTH:
            front_coor = (x * 40 + 15, y * 40 - 10, x * 40 + 25, y * 40)
        elif bearing == Bearing.NORTH_EAST:
            front_coor = (x * 40 + 35, y * 40 - 5, x * 40 + 45, y * 40 + 5)
        elif bearing == Bearing.EAST:
            front_coor = (x * 40 + 40, y * 40 + 10, x * 40 + 50, y * 40 + 20)
        elif bearing == Bearing.SOUTH_EAST:
            front_coor = (x * 40 + 35, y * 40 + 35, x * 40 + 45, y * 40 + 45)
        elif bearing == Bearing.SOUTH:
            front_coor = (x * 40 + 15, y * 40 + 40, x * 40 + 25, y * 40 + 50)
        elif bearing == Bearing.SOUTH_WEST:
            front_coor = (x * 40 - 5, y * 40 + 35, x * 40 + 5, y * 40 + 45)
        elif bearing == Bearing.WEST:
            front_coor = (x * 40 - 10, y * 40 + 10, x * 40, y * 40 + 20)
        else:
            front_coor = (x * 40 - 5, y * 40 - 5, x * 40 + 5, y * 40 + 5)

        try:
            self.canvas.delete(self.robot_body)
            self.canvas.delete(self.robot_header)
        except:
            pass

        self.robot_body = self.canvas.create_oval(x * 40 - 20, y * 40 - 20, x * 40 + 60, y * 40 + 60,
                                                  fill="dodger blue", outline="")
        self.robot_header = self.canvas.create_oval(front_coor[0], front_coor[1], front_coor[2], front_coor[3],
                                                    fill="white", outline="")

    def update_map(self, radius=2, full=False):
        if full:
            y_range = range(config.map_size['height'])
            x_range = range(config.map_size['width'])
        else:
            y_range = range(
                max(0, self.robot.y - radius),
                min(self.robot.y + radius, config.map_size['height'] - 1) + 1
            )
            x_range = range(
                max(0, self.robot.x - radius),
                min(self.robot.x + radius, config.map_size['width'] - 1) + 1
            )

        for y in y_range:
            for x in x_range:
                try:
                    self.update_cell(x, y)
                except IndexError:
                    pass

        self.put_robot(self.robot.x, self.robot.y, self.robot.bearing)

    # Robot's movement manual control
    def move(self):
        self.handler.move(True, False)
        self.update_map()
        print('Go straight')
        active_car('w1')
        time.sleep(0.2)
    
    def start(self):
        
        print('----------------------Obstacle ',ObstacleID.k + 1,'----------------------')
        Simulator.moveFinal(robot,end[ObstacleID.k],self)
        ObstacleID.k = ObstacleID.k+1
        time.sleep(3)
        #Simulator.avoidgoal(self,robot)
        
    def startall(self):
        
        for i in range(5):
            print('----------------------Obstacle ',ObstacleID.k + 1,'----------------------')
            Simulator.moveFinal(robot,end[ObstacleID.k],self)
            ObstacleID.k = ObstacleID.k+1
            time.sleep(3)
        #Simulator.avoidgoal(self,robot)

    def left(self):
        self.handler.left(True, False)
        self.update_map()
        print('Turn left')
        active_car('a')
        time.sleep(1)
        
        

    def right(self):
        self.handler.right(True, False)
        self.update_map()
        print('Turn Right')
        active_car('d')
        time.sleep(1)

    def turnRight(robot,self):
    #turn right
        #Simulator.move(self)
        Simulator.right(self)
        if robot[2] == 0:
            robot[2] = 180
        else:
            robot[2] = robot[2] -0
        
    def turnLeft(robot,self):
        #turn left
        Simulator.left(self)
        if robot[2] == 180:
            robot[2] = 0
        else:
            robot[2] = robot[2] +0
            
    def turn180(robot,self):
        #turn 180
        Simulator.right(self)
        Simulator.right(self)
        if robot[2] == 180:
            robot[2] = 0
        elif robot[2] == 1:
            robot[2] = 0
        else:
            robot[2] = robot[2] + 1
            
    def mov1(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y2 - y1 - 1
        for i in range(0, y2 - y1 ):
            Simulator.move(self)
        robot[1] = robot[1] + y2 - y1 
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for x2 - x1 - 5
        for i in range(0, x2 - x1 - 3):
            Simulator.move(self)
        robot[0] = robot[0] +  x2 - x1 - 3

    def mov2(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x2 - x1 - 1
        for i in range(0, x2 - x1 - 1):
            Simulator.move(self)
        robot[0] = robot[0] + x2 - x1 
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for y2 - y1 - 5
        for i in range(0, y2 - y1 - 5):
            Simulator.move(self)
        robot[1] = robot[1] +  y2 - y1 - 3

    def mov3(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x2 - x1 + 3
        for i in range(0, x2 - x1 + 3):
            Simulator.move(self)
        robot[0] = robot[0] + x2 - x1 + 3
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for y2 - y1 - 1
        for i in range(0, y2 - y1 ):
            Simulator.move(self)
        robot[1] = robot[1] +  y2 - y1 
        #turn left
        Simulator.turnLeft(robot,self)

    def mov4(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y2 - y1 + 3
        for i in range(0, y2 - y1 + 3):
            Simulator.move(self)
        robot[1] = robot[1] + y2 - y1 + 3
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for x2 - x1 - 1
        for i in range(0, x2 - x1 ):
            Simulator.move(self)
        robot[0] = robot[0] +  x2 - x1 
        #turn right
        Simulator.turnRight(robot,self)
        
    def mov5(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x1 - x2 + 5
        for i in range(0, x1 - x2 + 3):
            Simulator.move(self)
        robot[0] = robot[0] + x1 - x2 + 3
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for y2 - y1 - 1
        for i in range(0, y2 - y1 - 1):
            Simulator.move(self)
        robot[1] = robot[1] +  y2 - y1 - 1
        #turn right
        Simulator.turnRight(robot,self)

    def mov6(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x1 - x2 + 1
        for i in range(0, x1 - x2 + 1):
            Simulator.move(self)
        robot[0] = robot[0] + x1 - x2 + 1
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for y2 - y1 - 5
        for i in range(0, y2 - y1 - 3):
            Simulator.move(self)
        robot[1] = robot[1] +  y2 - y1 - 3

    def mov7(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y2 - y1 -1
        for i in range(0, y2 - y1 -1):
            Simulator.move(self)
        robot[1] = robot[1] + y2 - y1 -1
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for x1 - x2 - 3
        for i in range(0, x1 - x2 - 3):
            Simulator.move(self)
        robot[0] = robot[0] +  x1 - x2 - 3

    def mov8(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y2 - y1 + 3
        for i in range(0, y2 - y1 + 3):
            Simulator.move(self)
        robot[1] = robot[1] + y2 - y1 + 3
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for x1 - x2 + 1
        for i in range(0, x1 - x2 + 1):
            Simulator.move(self)
        robot[0] = robot[0] +  x1 - x2 + 1
        #turn left
        Simulator.turnLeft(robot,self)

    def mov9(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y1 - y2 + 1
        for i in range(0, y1 - y2 + 1):
            Simulator.move(self)
        robot[1] = robot[1] + y1 - y2 + 1
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for x2 - x1 - 5
        for i in range(0, x2 - x1 - 3):
            Simulator.move(self)
        robot[0] = robot[0] + x2 - x1 - 3

    def mov10(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y1 - y2 + 5
        for i in range(0, y1 - y2 + 3):
            Simulator.move(self)
        robot[1] = robot[1] + y1 - y2 + 3
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for x2 - x1 - 1
        for i in range(0, x2 - x1 - 1):
            Simulator.move(self)
        robot[0] = robot[0] + x2 - x1 - 1
        #turn left
        Simulator.turnLeft(robot,self)
        
    def mov11(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x2 - x1 + 3
        for i in range(0, x2 - x1 + 3):
            Simulator.move(self)
        robot[0] = robot[0] + x2 - x1 + 3
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for y1 - y2 + 1
        for i in range(0, y1 - y2 + 1):
            Simulator.move(self)
        robot[1] = robot[1] +  y1 - y2 + 1
        #turn right
        Simulator.turnRight(robot,self)
        
    def mov12(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x2 - x1 - 1
        for i in range(0, x2 - x1 - 1):
            Simulator.move(self)
        robot[0] = robot[0] + x2 - x1 - 1
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for y1 - y2 - 3 
        for i in range(0, y1 - y2 - 3):
            Simulator.move(self)
        robot[1] = robot[1] + y1 - y2 - 3 

    def mov13(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x1 - x2 + 5
        for i in range(0, x1 - x2 + 3):
            Simulator.move(self)
        robot[0] = robot[0] + x1 - x2 + 3
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for y1 - y2 + 1
        for i in range(0, y1 - y2 + 1):
            Simulator.move(self)
        robot[1] = robot[1] +  y1 - y2 + 1
        #turn left
        Simulator.turnLeft(robot,self)

    def mov14(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y1 - y2 + 5
        for i in range(0, y1 - y2 + 3):
            Simulator.move(self)
        robot[1] = robot[1] + y1 - y2 + 3
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for x1 - x2 + 1
        for i in range(0, x1 - x2 + 1):
            Simulator.move(self)
        robot[0] = robot[0] + x1 - x2 + 1
        #turn right
        Simulator.turnRight(robot,self)

    def mov15(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for y1 - y2 + 1
        for i in range(0, y1 - y2 + 1):
            Simulator.move(self)
        robot[1] = robot[1] + y1 - y2 + 1
        #turn right
        Simulator.turnRight(robot,self)
        #go straight for x1 - x2 - 3
        for i in range(0, x1 - x2 - 3):
            Simulator.move(self)
        robot[0] = robot[0] + x1 - x2 - 3

    def mov16(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        #go straight for x1 - x2 + 1
        for i in range(0, x1 - x2 + 1):
            Simulator.move(self)
        robot[0] = robot[0] + x1 - x2 + 1
        #turn left
        Simulator.turnLeft(robot,self)
        #go straight for y1 - y2 - 3
        for i in range(0, y1 - y2 - 3):
            Simulator.move(self)
        robot[1] = robot[1] +  y1 - y2 - 3
    
    def moveFinal(robot,end,self):
        x1 = robot[0]
        x2 = end[0]
        y1 = robot[1]
        count=0
        y2 = end[1]
        theta1 = robot[2]
        theta2 = end[2]
        print('Origin',robot)
        if y2>y1: #top 
            if x2>x1: #right 
                print('Des is top right of robot')
                if theta2 == 270:
                    if theta1 == 90:
                        Simulator.mov1(robot,end,self)
                    elif theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov1(robot,end,self)
                    elif theta1 == 180:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov1(robot,end,self)
                    else:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov1(robot,end,self)
                elif theta2 == 180:
                    if theta1 == 90:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov2(robot,end,self)
                    elif theta1 == 90:
                        Simulator.mov2(robot,end,self)
                    elif theta1 == 180:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov2(robot,end,self)
                    else:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov2(robot,end,self)
                elif theta2 == 90:
                    if theta1 == 90:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov3(robot,end,self)
                    elif theta1 == 90:
                        Simulator.mov3(robot,end,self)
                    elif theta1 == 180:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov3(robot,end,self)
                    else:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov3(robot,end,self)
                else:
                    if theta1 == 90:
                        Simulator.mov4(robot,end,self)
                    elif theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov4(robot,end,self)
                    elif theta1 == 180:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov4(robot,end,self)
                    else:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov4(robot,end,self)
            elif x2<x1: #left 
                print('Des is top left of robot')
                if theta2 == 270:
                    if theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov5(robot,end,self)
                    elif theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov5(robot,end,self)
                    elif theta1 == 180:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov5(robot,end,self)
                    else:
                        Simulator.mov5(robot,end,self)
                elif theta2 == 180: 
                    if theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov6(robot,end,self)
                    elif theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov6(robot,end,self)
                    elif theta1 == 180:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov6(robot,end,self)
                    else:
                        Simulator.mov6(robot,end,self)
                elif theta2 == 90:
                    if theta1 == 90:
                        Simulator.mov7(robot,end,self)
                    elif theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov7(robot,end,self)
                    elif theta1 == 180:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov7(robot,end,self)
                    else:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov7(robot,end,self)
                else:
                    if theta1 == 90:
                        Simulator.mov8(robot,end,self)
                    elif theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov8(robot,end,self)
                    elif theta1 == 180:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov8(robot,end,self)
                    else:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov8(robot,end,self)
        elif y2<y1: #bottom 
            if x2>x1: #right 
                print('Des is bottom right of robot')
                if theta2 == 270:
                    if theta1 == 0:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov9(robot,end,self)
                    elif theta1 == 90:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov9(robot,end,self)
                    elif theta1 == 180:
                        Simulator.mov9(robot,end,self)
                    else:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov9(robot,end,self)
                elif theta2 == 180: 
                    if theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov10(robot,end,self)
                    elif theta1 == 90:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov10(robot,end,self)
                    elif theta1 == 180:
                        Simulator.mov10(robot,end,self)
                    else:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov10(robot,end,self)
                elif theta2 == 90: 
                    if theta1 == 90:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov11(robot,end,self)
                    elif theta1 == 90:
                        Simulator.mov11(robot,end,self)
                    elif theta1 == 180:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov11(robot,end,self)
                    else:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov11(robot,end,self)
                else: 
                    if theta1 == 90:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov12(robot,end,self)
                    elif theta1 == 90:
                        Simulator.mov12(robot,end,self)
                    elif theta1 == 180:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov12(robot,end,self)
                    else:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov12(robot,end,self)
            elif x2<x1: #left 
                print('Des is bottom left of robot')
                if theta2 == 270:
                    if theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov13(robot,end,self)
                    elif theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov13(robot,end,self)
                    elif theta1 == 180:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov13(robot,end,self)
                    else:
                        Simulator.mov13(robot,end,self)
                elif theta2 == 180: 
                    if theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov14(robot,end,self)
                    elif theta1 == 90:
                    #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov14(robot,end,self)
                    elif theta1 == 180:
                        Simulator.mov14(robot,end,self)
                    else:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov14(robot,end,self)
                elif theta2 == 90: 
                    if theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov15(robot,end,self)
                    elif theta1 == 90:
                    #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov15(robot,end,self)
                    elif theta1 == 180:
                        Simulator.mov15(robot,end,self)
                    else:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov15(robot,end,self)
                else: 
                    if theta1 == 90:
                        #turn left
                        Simulator.turnLeft(robot,self)
                        Simulator.mov16(robot,end,self)
                    elif theta1 == 90:
                        #turn 180
                        Simulator.turn180(robot,self)
                        Simulator.mov16(robot,end,self)
                    elif theta1 == 180:
                        #turn right
                        Simulator.turnRight(robot,self)
                        Simulator.mov16(robot,end,self)
                    else:
                        Simulator.mov16(robot,end,self)
        print('end',robot)
        
        
        proId = main1()
        
        print("here", proId) #recived id from camera #TODO drop the probability
        print('Hamiltonian Path: ',hamiltonianPath[count])
        #TODO change the dict to a 1d list
        proid2 ={proId : hamiltonianPath[count]}
        print(proid2)
        displayList = []
        for proId,coord in proid2.items():
            displayList.append(str(proId))
            for num in v:
                displayList.append(str(num))
        print(displayList)
        return proId,


    def reset(self):
        if self.job:
            self.root.after_cancel(self.job)
        while not arduino_queue.empty():
            arduino_queue.get()
        self.handler.reset()
        self.update_map(full=True)

    def connect(self):
        if self.connect_button.cget('text') == 'Connect':
            self.robot_simulation = False
            self.map.clear_map_for_real_exploration()
            self.update_map(full=True)
            if self.handler.connect(self.ip_addr.get()):
                self.robot = self.handler.get_robot()
                self.connect_button.config(text='Disconnect')
                return

        self.robot_simulation = True
        self.connect_button.config(text='Connect')
        self.handler.disconnect()
        self.reset()

        self.handler = Handler(self)
        self.map = self.handler.map
        self.core = self.handler.core
        self.robot = self.handler.get_robot()

    def load(self):
        Tk().withdraw()
        filename = askopenfilename()

        f = open(filename, "r")

        self.map.decode_map_descriptor(f.readline())
        self.update_map(full=True)
