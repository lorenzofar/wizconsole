import logging
# Import the base object for a UI component
from tkinter import Frame
from tkinter import Scale, HORIZONTAL

LOGGER = logging.getLogger()


class ColorSlider(Frame):
    """
    A slider that allows the user to select a color.
    It is based on the Scale widget and uses the RGB color model.
    """

    def __init__(self, master, model):
        """
        Create a new ColorSlider.

        Arguments:
            master: The parent widget.
        """

        # Declare the variables storing the color components
        super().__init__(master)
        # Create the sliders for each color component

        # Pack the sliders
        self._r_slider.pack()
        self._g_slider.pack()
        self._b_slider.pack()
        self._brightness_slider.pack()
