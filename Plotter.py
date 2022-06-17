import matplotlib.pyplot as plt
import sys

class Plotter:
    def __init__(self, data):
        self.data = data

    def plot(self, tag1, tag2, label):
        fig, ax1 = plt.subplots()
        plot1 = ax1.plot(self.data[tag1], self.data[tag2], label="reflection")
        ax1.set_xlabel(tag1)
        ax1.set_ylabel(tag2)
        ax1.set_ylim(0, 100)
        plt.show()

    def plot_refraction_index(self, brechungsindex):
        fig, ax2 = plt.subplots()
        ax2.set_ylabel("refractive index")
        plot2 = ax2.plot(self.data["nm"], brechungsindex, color="red", label="refractive index")
        plt.show()

    def plot_reflection_refractive_index(self, brechungsindex, save=None):
        fig, ax1 = plt.subplots()
        plot1 = ax1.plot(self.data["nm"], self.data["%R"], label="reflection")
        ax1.set_xlabel("nm")
        ax1.set_ylabel("%R", color="blue")
        ax1.set_ylim(0, 100)
        ax1.tick_params(axis="y", labelcolor="blue")

        ax2 = ax1.twinx()
        ax2.set_ylabel("refractive index", color="red")
        plot2 = ax2.plot(self.data["nm"], brechungsindex, color="red", label="refractive index")
        ax2.tick_params(axis="y", labelcolor="red")

        ln = plot1 + plot2
        labels = [l.get_label() for l in ln]
        plt.legend(ln, labels, loc=0)
        plt.show()
        if save is not None:
            plt.savefig(save, dpi=600)

    def plot_comparison_onetwo(self, data2, label1, label2, tag1, tag2, tag21, tag22, xlabel, ylabel, min=0, max=100):
        fig, ax1 = plt.subplots()
        plot1 = ax1.plot(self.data[tag1], self.data[tag2], label=label1)
        plot2 = ax1.plot(data2[tag21], data2[tag22], label=label2)
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)
        ax1.set_ylim(min, max)
        ax1.legend()
        plt.savefig("comparison.png", dpi=700)
        plt.show()
