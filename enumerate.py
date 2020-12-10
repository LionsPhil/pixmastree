from tree import RGBXmasTree
from colorzero import Color
from time import sleep

tree = RGBXmasTree()

try:
    while True:
        for index, pixel in enumerate(tree):
            tree.off()
            pixel.color = Color('red')
            print("Lighting pixel", index)
            sleep(1)
except KeyboardInterrupt:
    tree.close()
