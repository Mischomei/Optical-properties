import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog as fd
import tkinter as tk
from functools import reduce


root = tk.Tk()
def mean_data(*args):
        nm = args[0][0].index.values
        mergedset = reduce(lambda left, right: pd.merge(left, right, "outer", "nm"), args[0])
        meandata = pd.DataFrame({"nm":nm, "%R":[np.array(i).mean() for i in [mergedset.loc[j] for j in nm]]})
        return meandata


def filereader():
    files = fd.askopenfilenames(parent=root, title='Choose files')
    filedata =[pd.read_csv(i, index_col=0) for i in files]
    return filedata


if __name__ == "__main__":
    files = filereader()
    data = mean_data(files)
    print(data)
    plt.plot(data["nm"], data["%R"])
    plt.show()