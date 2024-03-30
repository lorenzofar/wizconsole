import logging

from pywizlight import wizlight, PilotBuilder

LOGGER = logging.getLogger()


class WizLightController:

    def __init__(self, ip_address, asyncio_loop):
        self.ip_address = ip_address
        self.light = wizlight(ip_address)
        # Keep a reference to the asyncio loop so we can use it to run coroutines
        self.asyncio_loop = asyncio_loop
        print(f"Initialized light controller for {ip_address}")

    def turn_on(self):
        # Run the coroutine to turn the light on
        self.asyncio_loop.run_until_complete(self.light.turn_on(
            PilotBuilder(brightness=255, speed=10)
        ))

    def turn_off(self):
        # Run the coroutine to turn the light off
        self.asyncio_loop.run_until_complete(self.light.turn_off())

    def set_color(self, r: int, g: int, b: int, brightness: int = 255):
        print(f"Setting color to {r}, {g}, {b}")
        # Run the coroutine to set the color of the light
        self.asyncio_loop.run_until_complete(self.light.turn_on(
            PilotBuilder(rgb=(r, g, b), brightness=brightness, speed=10)
        ))
