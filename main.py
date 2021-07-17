import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
from matplotlib import style
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()

root.mainloop()


class Error(Exception):
    pass


def setdate(year, month, day):
    date = [int(year), int(month), int(day)]
    return date


def plotcreator(name, startdate, enddate):
    style.use("ggplot")
    start = dt.datetime(startdate[0], startdate[1], startdate[2])
    end = dt.datetime(enddate[0], enddate[1], enddate[2])
    df = web.get_data_yahoo(name, start, end)
    df["Adj Close"].plot()
    print("Successfully plotted " + name + "!")


def plotshow(plot):
    plt.show()


def parsedate(date):
    parsed = date.split('.')
    for i in range(len(parsed)):
        parsed[i] = int(parsed[i])
        return parsed


def main():
    #### user input #####
    loop = True
    while loop:
        n = input("Enter stock ticker to plot:\n")
        name = n.upper()
        # parse start date
        while True:
            try:
                startinput = input("Enter START date in the following format: YY.MM.DD\n")
                start = parsedate(startinput)
                # parse end date
                endinput = input("Enter END date in the following format: YY.MM.DD\n")
                end = parsedate(endinput)
                if end[0] < start[0]:
                    print("invalid date entry! try again.\n")
                    continue
                elif end[0] == start[0]:
                    if end[1] < start[1]:
                        print("you cannot have an end month before a start month!")
                        continue
                    elif end[1] == start[1]:
                        print("you cannot have an end day before a start day!")
                        continue
                else:
                    print("Processing request...")
                    print("ticker " + name + " selected, plotting...")
                    break
            except:
                print('date format invalid!\n')
                continue

        try:
            plotshow(plotcreator(name, setdate(start[0], start[1], start[2]), setdate(end[0], end[1], end[2])))
            print(name + " generated plot closed.")
            while True:
                ending = input("Would you like to re-plot? Y/N\n")
                if (ending == 'y'):
                    continue
                elif (ending == 'n'):
                    loop = False
                    print("Exiting!...")
                    break
                else:
                    continue
        except:
            print('invalid parameters! try again.\n')
            continue


if __name__ == "__main__":
    main()
