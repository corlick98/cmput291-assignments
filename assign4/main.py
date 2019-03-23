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