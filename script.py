'''P3
4 3
255
255 0 0 255 0 0 255 0 0 255 0 0
0 255 0 0 255 0 0 255 0 0 255 0
0 0 255 0 0 255 0 0 255 0 0 255
'''

def triplets(width, height):
    string = "P3\n" + str(width) + " " + str(height) + "\n255\n"
    R = 0
    G = 0
    B = 0
    for x in range(0, height):
        for y in range(0, width):
            string +=  str(R + 255.0 / (width*height)) + " " + str(G + 255.0 / (width*height)) + " " + str(B + 255.0 / (width*height)) + " "
            # string +="255 255 255 "
        string += "\n"
    return string

fd = open("hw.ppm", "w")
fd.write(str(triplets(300,300)))
fd.close()