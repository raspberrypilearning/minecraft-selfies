## Taking a picture

camera = PiCamera()
camera.resolution = (80,60)
camera.start_preview()
sleep(15)
camera.capture('selfie.jpg')
camera.close()

