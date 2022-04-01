# Warming stripes by Ed Hawkings
# author: Tommaso Olivero

# Inspiration code:
# https://matplotlib.org/matplotblog/posts/warming-stripes/

# import library matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap


def main():
    # Open and read the CSV file

    # Data from:
    # https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool+

    f = open("./Temperature_Anomaly.csv", "r")

    for _ in range(5):
        intest = f.readline()

    righe = f.readlines()

    # reading and saving data in lists
    year, temp = [], []

    for riga in righe:
        dati = riga.split(",")
        year.append(float(dati[0]))
        temp.append(float(dati[1]))

    # colomap creation
    cmap = ListedColormap([
        '#08306b', '#08519c', '#2171b5', '#4292c6',
        '#6baed6', '#9ecae1', '#c6dbef', '#deebf7',
        '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
        '#ef3b2c', '#cb181d', '#a50f15', '#67000d',
    ])

    # We create a figure with a single axes object that fills the full area of the figure and
    # does not have any axis ticks or labels.
    fig = plt.figure(figsize=(16, 9))

    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()

    # create a collection with a rectangle for each year
    FIRST = 1880
    LAST = 2017

    listaRett = [Rectangle((y, 0), 1, 1)for y in range(FIRST, LAST + 1)]
    col = PatchCollection(listaRett)

    # set data, colormap and color limits
    col.set_array(temp)
    col.set_cmap(cmap)
    ax.add_collection(col)

    ax.set_ylim(0, 1)
    ax.set_xlim(FIRST, LAST + 1)
    
    plt.savefig("Warming_Stripes.png")


if __name__ == "__main__":
    main()