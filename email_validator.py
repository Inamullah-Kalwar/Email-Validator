import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored  

login_url = "https://login.microsoftonline.com/"

def check_email_validity(email, df, row_index):

    driver = webdriver.Chrome()  

    driver.get(login_url)

    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "i0116"))
    )

    email_input.send_keys(email)

    ActionChains(driver).send_keys(Keys.RETURN).perform()

    time.sleep(2)

    try:

        error_element = driver.find_element(By.ID, "usernameError")
        is_valid = False  
    except:

        is_valid = True

    driver.quit()

    if is_valid:
        print(colored(f"Email {email} is valid!", 'green'))  

        df.at[row_index, 'Status'] = 'Valid'
    else:
        print(colored(f"Email {email} is invalid!", 'red'))  

        df.at[row_index, 'Status'] = 'Invalid'

    df.to_csv("highlighted_emails.csv", index=False, escapechar='\\')

csv_file_path = "emails.csv"
if not os.path.isfile(csv_file_path):
    print("The 'emails.csv' file is not found in the current directory.")
    csv_file_path = input("Please enter the full path to your CSV file: ")

df = pd.read_csv(csv_file_path)

df['Status'] = ''

for index, row in df.iterrows():
    email = row['Email']
    check_email_validity(email, df, index)