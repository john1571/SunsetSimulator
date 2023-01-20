# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example turns on the little red LED."""
from adafruit_circuitplayground import cp
import time


class Light:
    def __init__(self, number, rgb):
        self.number = number
        self.red, self.green, self.blue = rgb
        self.target_red = red
        self.target_blue = blue
        self.target_green = green
        cp.pixels[number] = self.Get_color()

    def set_target(self, rgb):
        self.target_red, self.target_green, self.target_blue = rgb

    def update_color(self, color, target, jump=1):
        if target > color + jump:
            color += jump
        elif target < color - jump:
            color -= jump
        else:
            color = target
        return color

    def Update(self, jump = 1):
        self.red = self.update_color(self.red, self.target_red, jump)
        self.blue = self.update_color(self.blue, self.target_blue, jump)
        self.green = self.update_color(self.green, self.target_green, jump)
        cp.pixels[self.number] = self.Get_color()

    def Get_color(self):
        return (self.red, self.green, self.blue)



# CHange t0 1 for single-tap detection
cp.detect_taps = 1
on = False
i = 0
First = True
cp.pixels.brightness = 0.1
red = 0
green = 0
blue = 0
sky_blue = (10,10,150)
blues = range(255,0,-2)
reds = range(0,150,1)
greens = [0]
colors = [(255,0,0),(0,255,0),(0,0,255),(150, 20, 0),(125,0,125), (125,125,0)]
i = 0
def set_color(iterator, color_array):
    if iterator < len(color_array) -1:
        return color_array[iterator]
    else:
        return color_array[-1]

sun_bright = .3
sun_array   = [(255, 255, 200), (200, 200, 100), (190, 190, 90), (180, 180, 80),  (170, 170, 70),  (160, 160, 60),  (150, 150,  25), (150, 100,  10), (100, 50,   5),
               (75,   25,   0), ( 50,   0,  50), ( 40,   0,  50), ( 20,   0,  40), (0,   0,  25), (0,0,20), (0,0,15),
               (0,0,10), (0,0,5), (0,0,0)]
flank_array = [(200, 200, 255), (200, 175,  70), (180, 150,  70), (170, 125,  70), (160, 100,  50), (165,  75,  30), (150,  50,   0), (100,  25,   0),
                ( 50,   0,  50), ( 40,   0,  50), ( 20,   0,  40), (0,   0,  25), (0,0,20), (0,0,15), (0,0,10), (0,0,5), (0,0,0)]
two_array   = [(100, 100, 255), (200, 100,  70), (170, 70,  70), (140, 70,  70), ( 75,  75, 200), ( 50,  50, 175), ( 25,  25, 125), ( 50,  0, 50), (50,  0, 25),
                (0,   0,  25), (0,0,20), (0,0,15), (0,0,10), (0,0,5), (0,0,0),]
three_array = [(100, 100, 255), (100, 100, 255), ( 65,  65, 180), ( 40,  40, 155), ( 20,  20, 105), ( 10,  0, 30),
                (0,   0,  25), (0,0,20), (0,0,15), (0,0,10), (0,0,5), (0,0,0)]

lights = []
lights.append(Light(0, two_array[0]))
lights.append(Light(1, flank_array[0]))
lights.append(Light(2, sun_array[0]))
lights.append(Light(3, flank_array[0]))
lights.append(Light(4, two_array[0]))
lights.append(Light(5, three_array[0]))
lights.append(Light(9, three_array[0]))

iterator = 0
while True:
    cp.pixels.brightness = sun_bright
    color = (0, 0, 0)
    cp.pixels[6:9] = [color] * 3

    for light in lights:
        light.Update()

    if iterator % 50 == 0:
        lights[6].set_target(set_color(i, three_array))
        lights[5].set_target(set_color(i, three_array))
        lights[0].set_target(set_color(i, two_array))
        lights[4].set_target(set_color(i, two_array))
        lights[1].set_target(set_color(i, flank_array))
        lights[3].set_target(set_color(i, flank_array))
        lights[2].set_target(set_color(i, sun_array))
        i += 1
        if (i > len(sun_array) -1):
            time.sleep(10)
            i = 0
    iterator += 1
    time.sleep(0.05)

