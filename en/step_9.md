## Mapping the blocks

The next part involves mapping the pixels from the colour map to actual Minecraft blocks. A dictionary is used to do this.

Minecraft blocks have two values associated with them; for instance, dirt is `2, 0`. The `0` is used as there's only one type of dirt block. Wool has many types with different colours, so wool can range from `35, 0` up to `35, 15`.

- The hard work has been done for you here. Below are the pixel values from the colour map `x, y`, mapped to the correct Minecraft block. It's in two forms: the first is if you're copying and pasting from a web page, as it's slightly more condensed, and the second is if you're copying from paper, as it's easier to see the structure.

	``` python
	#for copying from a browser
	colours={(0,0):(2,0),(0,1):(3,0),(0,2):(4,0),(0,3):(5,0),(0,4):(7,0),(0,5):(14,0),(0,6):(15,0),(1,0):(16,0),(1,1):(17,0),(1,2):(21,0),(1,3):(22,0),(1,4):(24,0),(1,5):(35,0),(1,6):(35,1),(2,0):(35,2),(2,1):(35,3),(2,2):(35,4),(2,3):(35,5),(2,4):(35,6),(2,5):(35,7),(2,6):(35,8),(3,0):(35,9),(3,1):(35,10),(3,2):(35,11),(3,3):(35,12),(3,4):(35,13),(3,5):(35,14),(3,6):(35,15),(4,0):(41,0),(4,1):(42,0),(4,2):(43,0),(4,3):(45,0),(4,4):(46,1),(4,5):(47,0),(4,6):(48,0),(5,0):(49,0),(5,1):(54,0),(5,2):(56,0),(5,3):(57,0),(5,4):(58,0),(5,5):(60,0),(5,6):(61,0),(6,0):(73,0),(6,1):(79,0),(6,2):(80,0),(6,3):(82,0),(6,4):(89,0),(6,5):(103,0),(6,6):(246,0)}
	```

	``` python
	#for copying from paper
	colours = {(0, 0): (2, 0),
			   (0, 1): (3, 0),
			   (0, 2): (4, 0),
			   (0, 3): (5, 0),
			   (0, 4): (7, 0),
			   (0, 5): (14, 0),
			   (0, 6): (15, 0),
			   (1, 0): (16, 0),
			   (1, 1): (17, 0),
			   (1, 2): (21, 0),
			   (1, 3): (22, 0),
			   (1, 4): (24, 0),
			   (1, 5): (35, 0),
			   (1, 6): (35, 1),
			   (2, 0): (35, 2),
			   (2, 1): (35, 3),
			   (2, 2): (35, 4),
			   (2, 3): (35, 5),
			   (2, 4): (35, 6),
			   (2, 5): (35, 7),
			   (2, 6): (35, 8),
			   (3, 0): (35, 9),
			   (3, 1): (35, 10),
			   (3, 2): (35, 11),
			   (3, 3): (35, 12),
			   (3, 4): (35, 13),
			   (3, 5): (35, 14),
			   (3, 6): (35, 15),
			   (4, 0): (41, 0),
			   (4, 1): (42, 0),
			   (4, 2): (43, 0),
			   (4, 3): (45, 0),
			   (4, 4): (46, 1),
			   (4, 5): (47, 0),
			   (4, 6): (48, 0),
			   (5, 0): (49, 0),
			   (5, 1): (54, 0),
			   (5, 2): (56, 0),
			   (5, 3): (57, 0),
			   (5, 4): (58, 0),
			   (5, 5): (60, 0),
			   (5, 6): (61, 0),
			   (6, 0): (73, 0),
			   (6, 1): (79, 0),
			   (6, 2): (80, 0),
			   (6, 3): (82, 0),
			   (6, 4): (89, 0),
			   (6, 5): (103, 0),
			   (6, 6): (246, 0)}

	```
- With the dictionary added, you can test this out in the interpreter. Run your code, then switch to the interpreter and type the following:

	``` python
	>>> colours[(0, 0)]
	```

You should see `(2, 0)` being returned, meaning dirt block.

- If you type the following:

	``` python
	>>> colours[(3, 3)]
	```

you should see that `(35, 12)` is returned. This means a wool block with a brown colour.

