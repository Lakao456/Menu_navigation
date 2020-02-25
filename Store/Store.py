import mysql.connector
from tkinter import *
from tkinter import messagebox
from pygame import mixer
import sys
import os

root = Tk()
root.title('Store')
root.geometry("600x600")
root.configure(bg="black")

mixer.init()

main_frame = LabelFrame(root, bg='black', bd=5)
main_frame.place()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="aman.singh456",
    database="Store"
)

mycursor = mydb.cursor()
mycursor.execute("USE Store")


def get_input(prompt="a number ", data_type="int"):
    if data_type.lower() == "int":
        return int(input("Enter " + prompt + "::"))
    if data_type.lower() == "float":
        return float(input("Enter " + prompt + "::"))
    if data_type.lower() == "str":
        return input("Enter " + prompt + "::")


print("Select an option")
print("1. Add customer")
print("2. Add item")
print("3. Place order")
print("4. Clear a table")
x = int(input("Select a number::"))

if x == 1:
    count = 0
    while (count == 0):
        name = get_input("Name", "str")
        age = get_input("Age", "int")
        phone_num = get_input("Phone number", "int")
        print("Do you want to add another entry ? ::")
        if "y" in get_input("Y/N", "str").lower():
            values = (name, age, phone_num)
            mycursor.execute("INSERT INTO customers (Name, Age, Phone_number)")
        elif "n" in get_input("Y/N", "str").lower():
            count = 1

if x == 4:
    print("1. Clear Customers")
    print("2. Clear Items")
    print("3. Clear Orders")
    print("4. Clear all")

    clear_tables = get_input()

    if clear_tables == 1:
        mycursor.execute("DROP TABLE IF EXISTS Customers")
        mycursor.execute(
            "CREATE TABLE(C_ID int PRIMARY KEY, Customer_Name VARCHAR(20), Price int, Phone_number int(10))")
    if clear_tables == 2:
        mycursor.execute("DROP TABLE IF EXISTS Items")
        mycursor.execute("CREATE TABLE(I_ID int IDENTITY(1,1) PRIMARY KEY, Item_Name VARCHAR(20), price int)")
    if clear_tables == 3:
        mycursor.execute("DROP TABLE IF EXISTS Orders")
        mycursor.execute("CREATE TABLE(C_ID int, I_ID int, Qty int, Amount int")
    if clear_tables == 4:
        mycursor.execute("DROP TABLE IF EXISTS Customers")
        mycursor.execute(
            "CREATE TABLE(C_ID int IDENTITY(1,1) PRIMARY KEY, Customer_Name VARCHAR(20), Price int, Phone_number int(10))")

        mycursor.execute("DROP TABLE IF EXISTS Items")
        mycursor.execute("CREATE TABLE(I_ID int IDENTITY(1,1) PRIMARY KEY, Item_Name VARCHAR(20), price int)")

        mycursor.execute("DROP TABLE IF EXISTS Orders")
        mycursor.execute("CREATE TABLE(C_ID int, I_ID int, Qty int, Amount int")
