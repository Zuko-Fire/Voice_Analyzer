#import RPi.GPIO as IO
import time
import board
import neopixel


class Rasberry():
    def __init__(self):

        self.pixel_noun = neopixel.NeoPixel(board.D18, 6, 0.5 , False, neopixel.RGB)
        self.pixel_adjectives = neopixel.NeoPixel(board.D7, 6, 0.5 , False, neopixel.RGB)
        self.pixel_verb = neopixel.NeoPixel(board.D10, 6, 0.5, False, neopixel.RGB)



    def onPin(self, noun, adjectives, verb):

        print(noun, adjectives, verb)

        self.pixel_noun[noun] = (255, 0, 0)
        self.pixel_adjectives[adjectives] = (0, 255, 0)
        self.pixel_verb[verb] = (0, 0, 255)

    def offPin(self):

        self.pixel_noun.fill = (0, 0, 0)
        self.pixel_adjectives.fill = (0, 0, 0)
        self.pixel_verb.fill = (0, 0, 0)

