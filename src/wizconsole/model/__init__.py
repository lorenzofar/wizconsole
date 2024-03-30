import logging
from tkinter import IntVar, StringVar

LOGGER = logging.getLogger()


class Model:

    def __init__(self):
        self.r = IntVar(value=255)
        self.g = IntVar(value=255)
        self.b = IntVar(value=255)
        self.brightness = IntVar(value=125)

    @property
    def color(self):
        return self.r.get(), self.g.get(), self.b.get()

    @property
    def brightness_value(self):
        return self.brightness.get()
