from gui import *


def main() :
    window = Tk()
    window.title('Voting App')
    window.geometry('300x325')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()