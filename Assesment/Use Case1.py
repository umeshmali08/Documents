#Use Case1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import datetime, timedelta

# Initialize the webdriver
driver = webdriver.Chrome()

# Step 1: Open URL
driver.get("https://erail.in/")

# Step 2: Click on from field
from_field = driver.find_element(By.ID, 'txtStationFrom')
from_field.click()

# Step 3: Clear the data from “From” field
from_field.clear()

# Step 4: Insert data “DEL” in the field to open the drop down
from_field.send_keys("DEL")
time.sleep(2)  # Wait for the drop-down to load

# Step 5: Select the station at 4th position in the dropdown & print it
dropdown_items = driver.find_elements(By.XPATH, '//*[@id="suggestions"]/ul/li')
station_name = dropdown_items[3].text  # Selecting the 4th item (index 3)
dropdown_items[3].click()
print("Selected Station: ", station_name)

# Step 6: Create an excel file with some expected station names
expected_stations = ["Station1", "Station2", "Station3", "DELHI"]
df_expected = pd.DataFrame(expected_stations, columns=["Expected Stations"])
df_expected.to_excel("expected_stations.xlsx", index=False)

# Step 7: Get the list of the data from the drop-down list & write it into an excel file & compare
from_field.send_keys("DEL")
time.sleep(2)
dropdown_items = driver.find_elements(By.XPATH, '//*[@id="suggestions"]/ul/li')
actual_stations = [item.text for item in dropdown_items]
df_actual = pd.DataFrame(actual_stations, columns=["Actual Stations"])
df_actual.to_excel("actual_stations.xlsx", index=False)

# Compare with expected stations
df_comparison = df_actual[df_actual["Actual Stations"].isin(df_expected["Expected Stations"])]
print("Matching Stations: \n", df_comparison)

# Step 8: Select 30 days from the current date in “Sort on Date”
date_field = driver.find_element(By.ID, 'txtToDate')
date_field.click()

# Calculate the date 30 days from now
thirty_days_later = datetime.now() + timedelta(days=30)
formatted_date = thirty_days_later.strftime("%d-%m-%Y")
date_field.clear()
date_field.send_keys(formatted_date)

# Report generation using ExtentReports (assuming a suitable library is available)
# from selenium_extent_report import ExtentReports, ExtentTest

# Initialize the report
# report = ExtentReports("TestReport.html")
# test = report.create_test("Test Case 1: ERAIL Automation")

# Log the steps
# test.log("INFO", "Opened ERAIL website")
# test.log("INFO", "Selected station: " + station_name)
# test.log("INFO", "Matching stations: " + str(df_comparison))

# Finalize the report
# report.flush()

# Clean up
driver.quit()
