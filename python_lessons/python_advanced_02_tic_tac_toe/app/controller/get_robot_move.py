"""get move from robot """
from app.model.robot import Robot


def get_robot_move(robot, table):
    result = None
    if isinstance(robot, Robot):
        result = robot.get_choice(table)
    return result
