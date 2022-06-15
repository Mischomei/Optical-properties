import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import sys
from tkinter import filedialog as fd
import tkinter as tk

class Plotter:
    def __init__(self, data):
        self.data = data
    
    def plot_reflection(self):
        fig, ax1 = plt.subplots()
        plot1 = ax1.plot(self.data["nm"], self.data["%R"], label="reflection")
        ax1.set_xlabel("nm")
        ax1.set_ylabel("%R")
        ax1.set_ylim(0, 100)
        plt.show()

    def plot_refraction_index(self):
        fig, ax2 = plt.subplots()
        ax2.set_ylabel("refractive index")
        plot2 = ax2.plot(self.data["nm"], brechungsindex(self.data, 8), color="red", label="refractive index")
        plt.show()
    
    def plot_reflection_refractive_index(self):
        fig, ax1 = plt.subplots()
        plot1 = ax1.plot(self.data["nm"], self.data["%R"], label="reflection")
        ax1.set_xlabel("nm")
        ax1.set_ylabel("%R", color="blue")
        ax1.set_ylim(0, 100)
        ax1.tick_params(axis="y", labelcolor="blue")

        ax2 = ax1.twinx()
        ax2.set_ylabel("refractive index", color="red")
        plot2 = ax2.plot(self.data["nm"], brechungsindex(self.data, 8), color="red", label="refractive index")
        ax2.tick_params(axis="y", labelcolor="red")

        ln = plot1+plot2
        labels= [l.get_label() for l in ln]
        plt.legend(ln, labels, loc=0)
        plt.show()
        if len(sys.argv) >= 2:
            plt.savefig(sys.argv[1], dpi=600)

    def plot_comparison_onetwo(self, data2):
        fig, ax1 = plt.subplots()
        plot1 = ax1.plot(self.data["nm"], self.data["%R"], label="reflection")
        plot2 = ax1.plot(data2["nm"], data2["%R"], label="reflection")
        ax1.set_xlabel("nm")
        ax1.set_ylabel("%R")
        ax1.set_ylim(0, 100)
        plt.show()
        plt.savefig("comparison.png", dpi=500)


        

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
    plotter = Plotter(data1)
    plotter.plot_comparison_onetwo(data2)
