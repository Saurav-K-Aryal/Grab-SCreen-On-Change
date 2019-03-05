from time import sleep, time
import PIL.ImageGrab
import PIL.Image
import tkinter as tk

## Globals ##
screenSize = PIL.ImageGrab.grab().size ## Not used rn
imageNum = 1  ## used to serialize image by order of time in each session
experimentSessionStart = time() ## Each Game has different sessionstart time

def save_image():
        global imageNum, experimentSessionStart
        grab = PIL.ImageGrab.grab()
        grab.save(r"C:\Users\Summer2018\Documents\Image_{0}_{1}.png".format(experimentSessionStart, imageNum))
        print("Saved img num:", imageNum)
        imageNum += 1

def start_new_session():
        global experimentSessionStart, imageNum
        print("New session")
        experimentSessionStart = time()
        imageNum = 1

root = tk.Tk()
root.attributes("-topmost", True)
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="New Game", 
                   fg="green",
                   command=start_new_session)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Save",
                   fg="red",
                   command=save_image)
slogan.pack(side=tk.LEFT)

root.mainloop()

##screenSize = PIL.ImageGrab.grab().size
##print(screenSize)
##
##mustSaveNextFrame = False
##imageNum = 1
##experimentSessionStart = time()
##while True:
##	grab = PIL.ImageGrab.grab()
##	targetPixelColor = grab.load()[0, 0]
##	if (targetPixelColor and (len(targetPixelColor) == 3) and (targetPixelColor[0] == 33) and (targetPixelColor[1] == 115) and (targetPixelColor[2] == 70)):
##		if mustSaveNextFrame:
##			grab.save(r"C:\Users\Summer2018\Documents\Image_{0}_{1}.png".format(experimentSessionStart, imageNum))
##			print("Saved img num:", imageNum)
##			imageNum += 1
##			mustSaveNextFrame = False
##			sleep(0.5) # Sleep for half second
##	else:
##		mustSaveNextFrame = True
##		print("Not saving with color:", targetPixelColor)
