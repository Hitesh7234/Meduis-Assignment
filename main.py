from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def main():
    try:
        inp_name = input("Full Name: ")
        inp_contact = input("Contact Number: ")
        inp_address = input("Address: ")
        inp_email = input("Email ID: ")
        inp_pincode = input("Pincode: ")
        inp_dob = input("Date of Birth (YYYY-MM-DD): ")
        inp_gender = input("Gender: ")
        return scraper(inp_name, inp_contact, inp_address, inp_pincode, inp_dob, inp_gender, inp_email)
    except Exception as e:
        print(f"An error occurred: {e}")

def scraper(inp_name, inp_contact, inp_address, inp_pincode, inp_dob, inp_gender, inp_email):
    # Set up Chrome options and driver
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service('chromedriver.exe')
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # XPaths for the form fields
        xpaths = {
            'full_name': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'contact': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'email': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'full_address': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea',
            'pincode': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'dob': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input',
            'gender': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'code': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input',
            'submit': '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        }
        
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')
        
        # Explicit wait for the contact field to be present
        wait = WebDriverWait(driver, 10)

        # Fill in the form fields
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['full_name']))).send_keys(inp_name)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['contact']))).send_keys(inp_contact)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['email']))).send_keys(inp_email)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['full_address']))).send_keys(inp_address)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['pincode']))).send_keys(inp_pincode)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['dob']))).send_keys(inp_dob)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['gender']))).send_keys(inp_gender)
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['code']))).send_keys("GNFPYC")
        
        # Submit the form
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths['submit']))).click()
        
        # Wait for a while to let the form submit and then take a screenshot
        time.sleep(5)
        screenshot_path = r"C:\Users\pc\Desktop\Screenshot\Submission.png"
        driver.save_screenshot(screenshot_path)
        print("Form submitted and screenshot taken.")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout while waiting for element - {e}")
    finally:
        driver.quit()

# Run the main function
main()
