from wizconsole.controller.light import WizLightController
import yaml

class Controller:

    def __init__(self, view, model, asyncio_loop):
        self.__model = model
        self.__view = view
        self.__view.submit_button.config(command=self.__submit)
        # Open the configuration file and read the IP addresses of the lights
        # Config is a YAML file with LIGHT section and ip address
        with open("config.yaml") as config_file:
            config = yaml.safe_load(config_file)
        ip = config["LIGHT"]["ip_address"]
        # Create the light controller for the configured light
        self.__light_controller = WizLightController(ip, asyncio_loop)

    def __submit(self):
        # Retrieve the selected color from the model
        r, g, b = self.__model.color
        brightness = self.__model.brightness.get()
        self.__light_controller.set_color(r, g, b, brightness)
