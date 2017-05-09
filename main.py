from story import story
from gui import gui

w = 1200
h = 650

ws = gui.winfo_screenwidth()
hs = gui.winfo_screenheight()

x = (ws/5) - (w/2)
y = (hs/2) - (h/2)

gui.geometry('+200+200')

gui.update_blurb(story)
gui.mainloop()