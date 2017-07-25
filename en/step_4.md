## Importing some modules

For this project you'll need to begin by importing a few modules. Most of them are pre-installed in Raspbian, but you need to install `skimage` yourself by following the instructions on the [software installation page](https://projects.raspberrypi.org/en/projects/minecraft-selfies/requirements/software/).

- Open up Python 3 (IDLE) from the Menu.
- Create a new file by clicking on *File* > *New File*.
- Now write the following lines in your new file to import the required modules:

	``` python
	from picamera import PiCamera
	from mcpi.minecraft import Minecraft
	from time import sleep
	from skimage import io, color
	```

- Save your file as `minecraft_selfies.py`, and then run it (by pressing *F5*) to make sure that you have all the required modules installed.

