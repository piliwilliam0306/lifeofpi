from abc import ABCMeta, abstractmethod

class JointControl(metaclass=ABCMeta):
    @abstractmethod
    def set_point(self):
        pass

class PositionControl(JointControl):
    def set_point(self):
        print('control by position')

class VelocityControl(JointControl):
    def set_point(self):
        print('control by velocity')

class ControlStrategy():
    def __init__(self, jointcontrol):
        self.jointcontrol = jointcontrol

    def set_point(self):
        self.jointcontrol.set_point()

if __name__ == '__main__':
    controller = ControlStrategy(PositionControl())
    controller.set_point()

    controller = ControlStrategy(VelocityControl())
    controller.set_point()