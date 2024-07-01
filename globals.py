from tkinter import font as tkf

SCREEN_WIDTH = None
SCREEN_HEIGHT = None
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def setScreenDim(dim: tuple[int, int]):
    global SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN_WIDTH = dim[0]
    SCREEN_HEIGHT = dim[1]

def getScreenDim() -> tuple[int, int]:
    global SCREEN_WIDTH, SCREEN_HEIGHT
    return (SCREEN_WIDTH, SCREEN_HEIGHT)