import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sqlite3

connection = sqlite3.connect('neighbors.db')
cursor = connection.cursor()


def scrape_data():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://divar.ir/s/mashhad")
    time.sleep(1)

    # Click on the relevant elements to open the menu
    driver.find_element(By.ID, "khesht-1").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "kt-action-field--small").click()
    time.sleep(1)

    unique_elements = set()  # Use a set to store unique data
    num_scrolls = 90
    popup = driver.find_element(By.CLASS_NAME, "multi-select-modal__scroll")

    for _ in range(num_scrolls):
        # Scroll a little
        driver.execute_script("arguments[0].scrollTop += 100;", popup)
        time.sleep(0.6)  # Adjust this sleep time as needed

        # Collect the data
        new_data = driver.find_elements(By.CLASS_NAME, "kt-control-row__title")

        for i in new_data:
            if i.text not in unique_elements:  # Check for duplicates
                unique_elements.add(i.text)  # Add unique data to the set
            else:
                print(f"Duplicate: {i.text}")

    # Convert the set back to a list if needed
    elements = list(unique_elements)

    for element in elements:
        # print(element)
        cursor.execute("INSERT INTO neighbors(name, city_id) VALUES (?,?)", (element, 1))
    connection.commit()


scrape_data()
