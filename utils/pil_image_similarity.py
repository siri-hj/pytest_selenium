from PIL import Image
import math
from functools import reduce
import operator
def image_similarity(filepath1, filepath2):
    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    #计算两个图片的差值有多少
    rms = math.sqrt(reduce(operator.add, list(map(lambda a, b:(a-b) ** 2, h1, h2))) / len(h1))
    return rms