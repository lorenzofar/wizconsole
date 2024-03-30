from wizconsole.controller import Controller
from wizconsole.model import Model
from wizconsole.view import View

import tkinter as tk
import asyncio

if __name__ == "__main__":
    app = tk.Tk()
    app.title("WizConsole")
    # Make the window fit the controls
    app.geometry("400x150")
    model = Model()
    view = View(app, model)
    # Create an asyncio loop
    loop = asyncio.get_event_loop()
    controller = Controller(view, model, loop)
    app.mainloop()

