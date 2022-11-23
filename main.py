import colorgram
from turtle import Turtle, Screen, colormode

colors = colorgram.extract('image.jpg', 15)

rgb_colors = []
for color in colors:
    rgb = color.rgb
    rgb_colors.append(rgb)

print(rgb_colors)
