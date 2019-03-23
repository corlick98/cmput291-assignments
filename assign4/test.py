import pandas as pd
import sqlite3
import folium
import numpy as np
import matplotlib.pyplot as plt

def main():
    dname = input("Enter the database name: ")
    conn = sqlite3.connect(dname)
    while True:
        printoptions()
        choice = input("enter which option you want to run: ")
        if choice == '1':
            f1(conn)
        elif choice == '2':
            f2(conn)
        elif choice == '3':
            f3(conn)
        elif choice == '4':
            f4(conn)
        elif choice == '5':
            return
        else:
            print("Please enter a valid selection")
def printoptions():
    print("1: Creates a bar plot of the monthwise total of a type of crime in a range of years")
    print("2: Shows the N most and least populous neighborhoods on a map")
    print("3: Shows the top N neighborhoods in terms of a particular type of crime")
    print("4: Shows the top N neighborhoods with highest crime to population ratios between a set of years also gives most frequent crime tyes and rations in these neighborhoods")
    print("5: quit")
    return

main()