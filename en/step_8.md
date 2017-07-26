## Converting to Lab colour space

- The `skimage` module makes conversion to Lab colour space from RGB colour space easy. You just need these two additional lines:

	``` python
	selfie_lab = color.rgb2lab(selfie_rgb)
	map_lab = color.rgb2lab(map_rgb)
	```

