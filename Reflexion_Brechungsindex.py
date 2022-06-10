import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import sys

def mean_data(*args):
        nm = args[0][0].index.values
        mergedset = reduce(lambda left, right: pd.merge(left, right, "outer", "nm"), args[0])
        meandata = pd.DataFrame({"nm":nm, "%R":[np.array(i).mean() for i in [mergedset.loc[j] for j in nm]]})
        return meandata


def filereader():
    #files = fd.askopenfilenames(parent=root, title='Choose files')
    files = ["/home/mischa/Documents/Licht-Silizium/20220609_Mikhail_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1084 Center.Sample.Raw.csv",
            "/home/mischa/Documents/Licht-Silizium/20220609_Mikhail_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1083 North.Sample.Raw.csv",
            "/home/mischa/Documents/Licht-Silizium/20220609_Mikhail_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1082 East.Sample.Raw.csv",
            "/home/mischa/Documents/Licht-Silizium/20220609_Mikhail_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1081 West.Sample.Raw.csv",
            "/home/mischa/Documents/Licht-Silizium/20220609_Mikhail_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1080 South.Sample.Raw.csv"]
    filedata =[pd.read_csv(i, index_col=0) for i in files]
    return filedata

def brechungsindex(data, winkel):
    reflexion = data["%R"] / 100
    einfallswinkel = winkel * np.pi / 180
    return np.sqrt(np.cos(einfallswinkel)**2*(1+np.sqrt(reflexion))**2/(1-np.sqrt(reflexion))**2+np.sin(einfallswinkel)**2) 

def plotter(data):
    fig, ax1 = plt.subplots()
    plot1 = ax1.plot(data["nm"], data["%R"], label="reflection")
    ax1.set_xlabel("nm")
    ax1.set_ylabel("%R", color="blue")
    ax1.set_ylim(0, 100)
    ax1.tick_params(axis="y", labelcolor="blue")
    
    ax2 = ax1.twinx()
    ax2.set_ylabel("refrective index", color="red")
    plot2 = ax2.plot(data["nm"], brechungsindex(data, 8), color="red", label="refrective index")
    ax2.tick_params(axis="y", labelcolor="red")

    ln = plot1+plot2
    labels= [l.get_label() for l in ln]
    plt.legend(ln, labels, loc=0)
    if len(sys.argv) == 2:
        plt.savefig(sys.argv[1], dpi=600)


if __name__ == "__main__":
    files = filereader()
    data = mean_data(files)
    print(data)
    plotter(data)
