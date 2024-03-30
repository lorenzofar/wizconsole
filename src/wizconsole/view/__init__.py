import tkinter as tk
from tkinter import Scale, VERTICAL

from wizconsole.view.controls import ColorSlider

SLIDER_ORIENTATION = VERTICAL


class View:

    def __init__(self, master, model):
        self._r_slider = Scale(master, label="Red", from_=0, to=255, orient=SLIDER_ORIENTATION, variable=model.r)
        self._g_slider = Scale(master, label="Green", from_=0, to=255, orient=SLIDER_ORIENTATION, variable=model.g)
        self._b_slider = Scale(master, label="Blue", from_=0, to=255, orient=SLIDER_ORIENTATION, variable=model.b)
        self._brightness_slider = Scale(master, label="Brightness", from_=0, to=255, orient=SLIDER_ORIENTATION,
                                        variable=model.brightness)

        self.__submit_button = tk.Button(master, text="Submit")

        # Define the grid layout
        self._r_slider.grid(row=0, column=0)
        self._g_slider.grid(row=0, column=1)
        self._b_slider.grid(row=0, column=2)
        self._brightness_slider.grid(row=0, column=3)
        self.__submit_button.grid(row=1, column=0)

    @property
    def submit_button(self):
        return self.__submit_button
