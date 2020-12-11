from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, strategy):
        self.prepare = strategy.prepare

    # context_interface
    def show(self, data):
        print(self.prepare(data))


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    # algorithm interface
    def prepare(self, some_data):
        pass


class HorizontalStrategy(Strategy):
    # algorithm interface
    def prepare(self, some_data):
        return ' '.join(some_data)


class VerticalStrategy(Strategy):
    # algorithm interface
    def prepare(self, some_data):
        return '\n'.join(some_data)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)