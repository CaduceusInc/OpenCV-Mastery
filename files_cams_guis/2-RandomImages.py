import cv2
import numpy
import os

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('chapter02/RandomGray.png', grayImage)

# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('chapter02/RandomColor.png', bgrImage)

gray_image_alt = numpy.random.randint(0, 256, 450000).reshape(900, 500)
cv2.imwrite('chapter02/RandGray.png', gray_image_alt)

#color_image_alt = numpy.random.randint(0, 256, 450000)
#color_i = color_image_alt.reshape(300, 500, 3)
#cv2.imwrite("\chapter02\RandColor.png", color_image_alt)
