import requests
import sqlite3
from selenium import webdriver

connection = sqlite3.connect('neighbors.db')
cursor = connection.cursor()


def main_app():
    user_selection = input("Would you like to scrape or view data? (s/v) ")
    if user_selection == 's':
        # scrape_data()
        pass
    elif user_selection == 'v':
        pass
        # view_data()
    else:
        print("Invalid input")
