from Model import *
from View import *
from ViewMenu import *
from Controller import *

from Utils.Const import *

import os
clear = lambda: os.system('cls')
clear()

if __name__ == "__main__":
    model = Model()
    view = View(model)
    viewM = ViewMenu()
    controller = MainController(model, view, viewM)

    if controller.GiveStateToMain() == 0:
        while controller.running:
            controller.ProcessMenuInput()
            viewM.Blit()


    