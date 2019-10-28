from PIL import Image
import random

im = Image.open('abcdefgh.png', 'r')



#im.crop((0, 200, 300, 300)).show()


pix_val = list(im.getdata())

#turn pix_val into a 2d matrix
pixels = []
for i in range(im.size[1]):
    row = []
    for j in range(im.size[0]):
        row.append(pix_val[j + im.size[0]*i])
    pixels.append(row)

# Coords are (x, y, closest-mean)
letterCoords = []

print(im.size)

im.show()

for row in range(im.size[1]):
    for col in range(im.size[0]):
        if (pixels[row][col][0] < 100 and pixels[row][col][1] < 100 and pixels[row][col][2] < 100):
            letterCoords.append([col, row, 1])
            im.putpixel((col, row), (255, 0, 0, 255))
        else :
            im.putpixel((col, row), (255, 255, 255, 255))

im.putpixel((int(im.size[0]/2), int(im.size[1]/2)), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2) + 1, int(im.size[1]/2)), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2) + 2, int(im.size[1]/2)), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2) + 3, int(im.size[1]/2)), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2) + 4, int(im.size[1]/2)), (0, 255, 0, 255))

im.putpixel((int(im.size[0]/2)+1, int(im.size[1]/2) + 1), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2)+2, int(im.size[1]/2) + 1), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2)+3, int(im.size[1]/2) + 1), (0, 255, 0, 255))
im.putpixel((int(im.size[0]/2)+4, int(im.size[1]/2) + 1), (0, 255, 0, 255))



im.show()

#Use k means clustering to find the letters
kValue = 8
k = []


incrementX = im.size[0]/kValue


for i in range(kValue):
    k.append([i * incrementX, im.size[1]/2])

for iteration in range(50):
    for i in range(len(letterCoords)):
        min = 100000
        for j in range(len(k)):
            distance = abs(k[j][0] - letterCoords[i][0]) + abs(k[j][1] - letterCoords[i][1])
            if (distance < min):
                min = distance
                letterCoords[i][2] = j
    # [[sumx, sumy, count]]
    averages = []
    for i in range(kValue):
        averages.append([0, 0, 0])
    for i in range(len(letterCoords)):
        averages[letterCoords[i][2]][0] += letterCoords[i][0]
        averages[letterCoords[i][2]][1] += letterCoords[i][1]
        averages[letterCoords[i][2]][2] += 1
    for i in range(len(k)):
        if (averages[i][2] != 0):
            k[i][0] = averages[i][0] / averages[i][2]
            k[i][1] = averages[i][1] / averages[i][2]

print(k[0][0], k[0][1])
print(k[1][0], k[1][1])
print(k[2][0], k[2][1])


for i in range(len(k)):
    im.crop((k[i][0]-100, k[i][1]-100, k[i][0] + 100, k[i][1] + 100)).show()
