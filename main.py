import sys



import src.core as core
import src.ui.interface as gui

DEBUGMODE = False

def main():
    gameCore = core.Core()
    gameCore.activate()

    gameUI = gui.UserInterface(gameCore)
    gameUI.launch()
    
    gameCore.run()

if __name__ == "__main__":
    if DEBUGMODE:
        import cProfile
        cProfile.run('main()','zpg.prof')
    else:
        main()
    sys.exit()