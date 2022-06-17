from functools import reduce

import pandas as pd
import numpy as np
from tkinter import filedialog as fd
import tkinter as tk
import Plotter

def filereader():
    root = tk.Tk()
    root.withdraw()
    files = fd.askopenfilenames(title='Choose files')
    filedata =[pd.read_csv(i, names=["nm", "%T"], delimiter="	") for i in files]
    return filedata


data = filereader()[0]
data["%T"] *= 100
plotter = Plotter.Plotter(data)
plotter.plot("nm", "%T", "Transmission")
