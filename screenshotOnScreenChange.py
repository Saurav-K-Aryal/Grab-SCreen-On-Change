from time import sleep, time
import PIL.ImageGrab
import PIL.Image

screenSize = PIL.ImageGrab.grab().size
print(screenSize)

mustSaveNextFrame = False
imageNum = 1
experimentSessionStart = time()
while True:
	grab = PIL.ImageGrab.grab()
	targetPixelColor = grab.load()[0, 0]
	if (targetPixelColor and (len(targetPixelColor) == 3) and (targetPixelColor[0] == 33) and (targetPixelColor[1] == 115) and (targetPixelColor[2] == 70)):
		if mustSaveNextFrame:
			grab.save(r"C:\Users\Summer2018\Documents\Image_{0}_{1}.png".format(experimentSessionStart, imageNum))
			print("Saved img num:", imageNum)
			imageNum += 1
			mustSaveNextFrame = False
			sleep(0.5) # Sleep for half second
	else:
		mustSaveNextFrame = True
		print("Not saving with color:", targetPixelColor)
