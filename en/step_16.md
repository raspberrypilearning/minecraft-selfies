## Iterate over image and then over map. Find closest colour from map, and then look up that block and place

mc = Minecraft.create()
x, y, z = mc.player.getPos()

for i, selfie_column in enumerate(selfie_lab):
	for j, selfie_pixel in enumerate(selfie_column):
		distance = 300
		for k, map_column in enumerate(map_lab):
			for l, map_pixel in enumerate(map_column):
				delta = color.deltaE_cie76(selfie_pixel,map_pixel)
				if delta < distance:
					distance = delta
					block = colours[(k,l)]
		mc.setBlock(x-j, y-i+60, z+5, block[0], block[1])
```

