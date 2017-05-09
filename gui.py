import tkinter as tk


class Keyboard(tk.Frame):

    main_font = ("Times New Roman", 16)

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.dynamic_buttons = []

    def callback_factory(self, blurb):
        def callback():
            return self.parent.update_blurb(blurb)
        return callback

    def new_options(self):
        for button in self.dynamic_buttons:
            button.destroy()

        for child in self.parent.blurb.get_children():
            newButton = tk.Button(self, text=child, font=self.main_font, command=self.callback_factory(child))
            self.dynamic_buttons.append(newButton)
            newButton.pack()



class Gui(tk.Tk):

    main_font = ("Times New Roman", 16)

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.blurb = ""

        self.display_text = tk.StringVar()
        self.display_text.set("hello world")
        
        self.screen = tk.Label(self, textvariable=self.display_text, justify=tk.LEFT, bg="#ECD6A4", font=self.main_font)
        self.screen.pack()

        self.keyboard = Keyboard(self)
        self.keyboard.pack()

    def update_blurb(self, blurb):
        self.blurb = blurb
        self.display_text.set(blurb.to_string())
        self.keyboard.new_options()



gui = Gui()