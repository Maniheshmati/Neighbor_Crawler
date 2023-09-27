import requests
import sqlite3
from selenium import webdriver
from scrape import scrape_data

connection = sqlite3.connect('neighbors.db')
cursor = connection.cursor()


def main_app():
    user_selection = input("Would you like to scrape? (y/n) ")
    if user_selection == 'y':
        scrape_data()
    elif user_selection == 'n':
        exit()
    else:
        print("Invalid input")

main_app()