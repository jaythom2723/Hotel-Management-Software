from globals import getScreenDim, WINDOW_WIDTH, WINDOW_HEIGHT
from app import App

import backend.sqlapi as sql

def main():
    sql.initializeSQL()

    app = App()
    dim = getScreenDim()
    center_x = int((dim[0]/2) - (800/2))
    center_y = int((dim[1]/2) - (600/2))
    app.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')
    app.title("Hotel Management Software")

    app.mainloop()

    sql.closeSQL()

if __name__ == "__main__":
    main()