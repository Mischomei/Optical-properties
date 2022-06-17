import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import sys
from tkinter import filedialog as fd
import tkinter as tk
import Plotter

def mean_data(*args):
        nm = args[0][0].index.values
        mergedset = reduce(lambda left, right: pd.merge(left, right, "outer", "nm"), args[0])
        meandata = pd.DataFrame({"nm":nm, "%R":[np.array(i).mean() for i in [mergedset.loc[j] for j in nm]]})
        return meandata


def filereader():
    root = tk.Tk()
    root.withdraw()
    files = fd.askopenfilenames(title='Choose files')
    filedata =[pd.read_csv(i, index_col=0) for i in files]
    return filedata

def brechungsindex(data, winkel):
    reflexion = data["%R"] / 100
    if len(sys.argv) > 2:
        winkel = float(sys.argv[2])
    einfallswinkel = winkel * np.pi / 180
    return np.sqrt(np.cos(einfallswinkel)**2*(1+np.sqrt(reflexion))**2/(1-np.sqrt(reflexion))**2+np.sin(einfallswinkel)**2)

   
if __name__ == "__main__":
    files_oneside = filereader()
    files_twoside = filereader()
    data2 = mean_data(files_twoside)
    data1 = mean_data(files_oneside)

    br = brechungsindex(data1, 8)
    plotter = Plotter.Plotter(data1)
    plotter.plot_comparison_onetwo(data2, "SSP", "DSP", "nm", "%R", "nm", "%R", "nm", "%R")
