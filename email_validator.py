import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

login_url = "https://login.microsoftonline.com/"

def check_email_validity(email, driver, df, row_index):
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

    if is_valid:
        df.at[row_index, 'Status'] = 'Valid'
    else:
        df.at[row_index, 'Status'] = 'Invalid'

    df.to_csv("highlighted_emails.csv", index=False, escapechar='\\')

# Check if the file exists in the current directory
csv_file_path = "emails.csv"
if not os.path.isfile(csv_file_path):
    print("The 'emails.csv' file is not found in the current directory.")
    csv_file_path = input("Please enter the full path to your CSV file: ")

# Load the CSV file
df = pd.read_csv(csv_file_path)

df['Status'] = ''

valid_count = 0
invalid_count = 0

# Open a single browser window
driver = webdriver.Chrome()

print("\nProcessing...")

with tqdm(total=len(df), desc="Validating Emails", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", dynamic_ncols=True, colour='green') as pbar:
    for index, row in df.iterrows():
        email = row['Email']
        check_email_validity(email, driver, df, index)
        if df.at[index, 'Status'] == 'Valid':
            valid_count += 1
        else:
            invalid_count += 1
        pbar.update(1)

# Close the browser window
driver.quit()

# Display summary
print("\nSummary:")
print(f"Total emails: {len(df)}")
print(f"Valid emails: {valid_count}")
print(f"Invalid emails: {invalid_count}")