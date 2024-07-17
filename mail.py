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
        from_id = input("Your Email: ")
        from_pass = input("Your Password: ")
        to_email = input("To email: ")
        cc_email = input("CC email: ")
        Github_repo = input("Link to Github Repo: ")
        Past_work = input("Link to Past Work: ")
        Resume = input("Resume Link: ")
        
        message = f'''Yes, I am available to work for the next 3-6 months as full-time.\nGitHub Repo Link: {Github_repo}\nPast Work Link: {Past_work}\nResume Link: {Resume}\nScreenshot and Approach Document are Attached Below'''

        mail(from_id, from_pass, to_email, cc_email, message)
    except Exception as e:
        print(f"An error occurred: {e}")

def mail(from_id, from_pass, to_email, cc_email, message):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service('chromedriver.exe')
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://mail.google.com/mail/u/0/#inbox")

        # Fill in email and click next
        email_xpath = '//*[@id="identifierId"]'
        wait_and_fill(driver, email_xpath, from_id)

        next_xpath = '//*[@id="identifierNext"]/div/button/span'
        wait_and_click(driver, next_xpath)

        # Fill in password and click next
        pass_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
        wait_and_fill(driver, pass_xpath, from_pass)

        next_xpath = '//*[@id="passwordNext"]/div/button/span'
        wait_and_click(driver, next_xpath)

        # Compose email
        compose_xpath = "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div"
        wait_and_click(driver, compose_xpath)

        # Fill in recipient and CC
        to_email_xpath = '//*[@id=":tl"]'
        wait_and_fill(driver, to_email_xpath, to_email)

        cc_xpath = '//span[text()="Cc"]'
        wait_and_click(driver, cc_xpath)

        cc_info_xpath = '//div[@class="aH9"]//input[@aria-label="CC recipients"]'
        wait_and_fill(driver, cc_info_xpath, cc_email)

        # Fill in subject and message body
        subject_xpath = '//*[@id=":py"]'
        wait_and_fill(driver, subject_xpath, "Python (Selenium) Assignment - Hitesh Singh")

        body_xpath = '//*[@id=":r8"]'
        wait_and_fill(driver, body_xpath, message)

        # Attach files
        attach_files(driver)

        # Send email
        send_xpath = '//*[@id=":po"]'
        wait_and_click(driver, send_xpath)

        print("Email sent successfully.")
        time.sleep(5)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

def wait_and_fill(driver, xpath, value):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(value)

def wait_and_click(driver, xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def attach_files(driver):
    file_paths = [
        r"C:\Users\pc\Desktop\Screenshot\Submission.png"
    ]
    input_file_xpath = '//input[@type="file"]'
    
    for file_path in file_paths:
        input_file = driver.find_element(By.XPATH, input_file_xpath)
        input_file.send_keys(file_path)
        time.sleep(3)  # Adding a short delay to ensure file uploads correctly


main()
