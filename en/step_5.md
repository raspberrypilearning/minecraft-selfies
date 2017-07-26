## Taking a selfie

The first stage is fairly simple. You're just going to use the Pi Camera to take a selfie.

- Below your module imports you can set up the `camera` object and set its resolution with the following two lines:

	``` python
	camera = PiCamera()
	camera.resolution = (80,60)
	```

You could use a larger resolution but the code takes much longer to run, even on a Pi 3.

- Next, you're going to start a preview of the camera, wait a little bit, then capture an image and save it as `selfie.jpg`:

	``` python
	camera.start_preview()
	sleep(5)
	camera.capture('selfie.jpg')
	camera.close()
	```
- That's the first part of the script finished. You can run this and take a photo of yourself to test it out. The image will appear in whichever directory you've saved your Python script. It will appear to be very low-resolution, but that's okay.

![image](images/selfie.jpg)

