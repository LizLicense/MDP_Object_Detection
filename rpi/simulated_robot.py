from robot import *
from utils import *


class SimulatedRobot(Robot):
    def __init__(self, handler):
        super().__init__(handler)
        self.map = handler.map
        self.handler = handler

    def get_front_middle(self):
        detect_range = config.sensor_range['front_middle']
        robot_x, robot_y = self.handler.robot.get_location()
        direction = self.handler.robot.bearing
        if direction == Bearing.SOUTH:
            sensor_location = [robot_x, robot_y + 1]
            ret = self.get_sensor_data(sensor_location, Bearing.SOUTH, detect_range)
        elif direction == Bearing.NORTH:
            sensor_location = [robot_x, robot_y - 1]
            ret = self.get_sensor_data(sensor_location, Bearing.NORTH, detect_range)
        elif direction == Bearing.EAST:
            sensor_location = [robot_x + 1, robot_y]
            ret = self.get_sensor_data(sensor_location, Bearing.EAST, detect_range)
        elif direction == Bearing.WEST:
            sensor_location = [robot_x - 1, robot_y]
            ret = self.get_sensor_data(sensor_location, Bearing.WEST, detect_range)
        else:
            print("    [ERROR] Invalid direction!", sep='; ')
            return
        # return [sensor_location, ret]
        return ret

    def get_front_left(self):
        detect_range = config.sensor_range['front_left']
        robot_x, robot_y = self.handler.robot.get_location()
        direction = self.handler.robot.bearing
        if direction == Bearing.WEST:
            sensor_location = [robot_x - 1, robot_y + 1]
            ret = self.get_sensor_data(sensor_location, Bearing.WEST, detect_range)
        elif direction == Bearing.EAST:
            sensor_location = [robot_x + 1, robot_y - 1]
            ret = self.get_sensor_data(sensor_location, Bearing.EAST, detect_range)
        elif direction == Bearing.SOUTH:
            sensor_location = [robot_x + 1, robot_y + 1]
            ret = self.get_sensor_data(sensor_location, Bearing.SOUTH, detect_range)
        elif direction == Bearing.NORTH:
            sensor_location = [robot_x - 1, robot_y - 1]
            ret = self.get_sensor_data(sensor_location, Bearing.NORTH, detect_range)
        else:
            print("    [ERROR] Invalid direction!")
            return
        # return [sensor_location, ret]
        return ret

    def get_front_right(self):
        detect_range = config.sensor_range['front_right']
        robot_x, robot_y = self.handler.robot.get_location()
        direction = self.handler.robot.bearing
        if direction == Bearing.EAST:
            sensor_location = [robot_x + 1, robot_y + 1]
            return self.get_sensor_data(sensor_location, Bearing.EAST, detect_range)
        elif direction == Bearing.WEST:
            sensor_location = [robot_x - 1, robot_y - 1]
            return self.get_sensor_data(sensor_location, Bearing.WEST, detect_range)
        elif direction == Bearing.SOUTH:
            sensor_location = [robot_x - 1, robot_y + 1]
            return self.get_sensor_data(sensor_location, Bearing.SOUTH, detect_range)
        elif direction == Bearing.NORTH:
            sensor_location = [robot_x + 1, robot_y - 1]
            return self.get_sensor_data(sensor_location, Bearing.NORTH, detect_range)
        else:
            print("    [ERROR] Invalid direction!")

    def get_left_front(self):
        detect_range = config.sensor_range['left_front']
        robot_x, robot_y = self.handler.robot.get_location()
        direction = self.handler.robot.bearing
        if direction == Bearing.NORTH:
            sensor_location = [robot_x - 1, robot_y - 1]
            return self.get_sensor_data(sensor_location, Bearing.WEST, detect_range)
        elif direction == Bearing.SOUTH:
            sensor_location = [robot_x + 1, robot_y + 1]
            return self.get_sensor_data(sensor_location, Bearing.EAST, detect_range)
        elif direction == Bearing.WEST:
            sensor_location = [robot_x - 1, robot_y + 1]
            return self.get_sensor_data(sensor_location, Bearing.SOUTH, detect_range)
        elif direction == Bearing.EAST:
            sensor_location = [robot_x + 1, robot_y - 1]
            return self.get_sensor_data(sensor_location, Bearing.NORTH, detect_range)
        else:
            print("    [ERROR] Invalid direction!")

    def get_left_middle(self):
        detect_range = config.sensor_range['left_middle']
        robot_x, robot_y = self.handler.robot.get_location()
        direction = self.handler.robot.bearing
        if direction == Bearing.NORTH:
            sensor_location = [robot_x - 1, robot_y]
            return self.get_sensor_data(sensor_location, Bearing.WEST, detect_range)
        elif direction == Bearing.SOUTH:
            sensor_location = [robot_x + 1, robot_y]
            return self.get_sensor_data(sensor_location, Bearing.EAST, detect_range)
        elif direction == Bearing.WEST:
            sensor_location = [robot_x, robot_y + 1]
            return self.get_sensor_data(sensor_location, Bearing.SOUTH, detect_range)
        elif direction == Bearing.EAST:
            sensor_location = [robot_x, robot_y - 1]
            return self.get_sensor_data(sensor_location, Bearing.NORTH, detect_range)
        else:
            print("    [ERROR] Invalid direction!")

    def get_right(self):
        detect_range = config.sensor_range['right']
        robot_x, robot_y = self.handler.robot.get_location()
        direction = self.handler.robot.bearing
        if direction == Bearing.NORTH:
            sensor_location = [robot_x + 1, robot_y]
            return self.get_sensor_data(sensor_location, Bearing.EAST, detect_range)
        elif direction == Bearing.SOUTH:
            sensor_location = [robot_x - 1, robot_y]
            return self.get_sensor_data(sensor_location, Bearing.WEST, detect_range)
        elif direction == Bearing.WEST:
            sensor_location = [robot_x, robot_y - 1]
            return self.get_sensor_data(sensor_location, Bearing.NORTH, detect_range)
        elif direction == Bearing.EAST:
            sensor_location = [robot_x, robot_y + 1]
            return self.get_sensor_data(sensor_location, Bearing.SOUTH, detect_range)
        else:
            print("    [ERROR] Invalid direction!")

    def get_sensor_data(self, location, sensor_bearing, detect_range):
        # print('detect_range:', detect_range)
        dis = 0
        if sensor_bearing == Bearing.SOUTH:
            # while (within boundary) and (block is free) and (not exceeding sensor range)
            while location[1] + dis + 1 < 20 and self.map.is_free(location[0],
                                                                  location[1] + dis + 1) and dis < detect_range:
                dis += 1
        elif sensor_bearing == Bearing.NORTH:
            while location[1] - dis - 1 >= 0 and self.map.is_free(location[0],
                                                                  location[1] - dis - 1) and dis < detect_range:
                dis += 1
        elif sensor_bearing == Bearing.EAST:
            while location[0] + dis + 1 < 15 and self.map.is_free(location[0] + dis + 1,
                                                                  location[1]) and dis < detect_range:
                dis += 1
        elif sensor_bearing == Bearing.WEST:
            while location[0] - dis - 1 >= 0 and self.map.is_free(location[0] - dis - 1,
                                                                  location[1]) and dis < detect_range:
                dis += 1

        # print("dis=", dis)

        if dis > detect_range:
            dis = -detect_range

        # print("loc=", location, "sb=", sensor_bearing, "range=", detect_range, "steps=", dis)

        return dis

    # ----------------------------------------------------------------------

    # ----------------------------------------------------------------------
    #     Function get_all_sensor_data
    # ----------------------------------------------------------------------
    # return:
    #     a list containing all sensor datas following get_sensor_data() format
    #     the order is as follows:
    #         front_middle,
    #         front_left,
    #         front_right,
    #         left,
    #         right
    # ----------------------------------------------------------------------
    def receive(self):
        out = [self.get_front_left(),
               self.get_front_middle(),
               self.get_front_right(),
               self.get_left_front(),
               self.get_left_middle(),
               self.get_right()]

        return out