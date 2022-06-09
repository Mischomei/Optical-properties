import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

print(sys.argv)


south = pd.read_csv(
    "20220609_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1080 South.Sample.Raw.csv")
north = pd.read_csv(
    "20220609_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1083 North.Sample.Raw.csv")
center = pd.read_csv(
    "20220609_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1084 Center.Sample.Raw.csv")
east = pd.read_csv(
    "20220609_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1082 East.Sample.Raw.csv")
west = pd.read_csv(
    "20220609_SiWafer/Scan URA 8° 08 June 2022 23_31 Mitteleuropäische Sommerzeit/Sample1081 West.Sample.Raw.csv")


def brechungsindex(data):
    #Brechungsindex berechnen
    reflexion = south[" %R"] / 100
    einfallswinkel = 8 * np.pi / 180
    brechungswinkel = 30 * np.pi / 180
    sbrechungsindex = (1*np.cos(einfallswinkel)-1*np.sqrt(reflexion)*np.cos(einfallswinkel))/(np.sqrt(reflexion)*np.cos(brechungswinkel)+np.cos(brechungswinkel))
    pbrechungsindex = np.sqrt(np.cos(einfallswinkel)**2*(1+np.sqrt(reflexion))**2/(1-np.sqrt(reflexion))**2+np.sin(einfallswinkel)**2)
    return pbrechungsindex

print(brechungsindex(south).median())
meandata = pd.DataFrame()
plt.plot(south["nm"], south[" %R"], label="South")
plt.plot(east["nm"], east[" %R"], label="East")
plt.plot(north["nm"], north[" %R"], label="North")
plt.plot(west["nm"], west[" %R"], label="West")
plt.plot(center["nm"], center[" %R"], label="Center")

plt.legend(loc="upper right")
plt.ylabel("Reflektion")
plt.xlabel("Wellenlänge")
plt.show()


if len(sys.argv) == 1:
    pass
else:
    plt.savefig(sys.argv[1])