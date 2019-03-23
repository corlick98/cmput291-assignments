import pandas as pd
import sqlite3
import folium
import numpy as np
import matplotlib.pyplot as plt
def main():
    dname = input("Enter the database name: ")
    conn = sqlite3.connect(dname)
    q1count=0
    q2count=0
    q3count=0
    q4count=0
    while True:
        printoptions()
        choice = input("Enter which option you want to run: ")
        if choice == '1':
            q1count = f1(conn,q1count)
        elif choice == '2':
            q2count = f2(conn,q2count)
        elif choice == '3':
            q3count = f3(conn,q3count)
        elif choice == '4':
            q4count = f4(conn,q4count)
        elif choice == '5':
            return
        else:
            print("Please enter a valid selection")