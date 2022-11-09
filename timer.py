import time


def start(countChanged):
    x = 10
    while x > 0:
        time.sleep(1)
        countChanged.emit(str(x))
        x -=1
