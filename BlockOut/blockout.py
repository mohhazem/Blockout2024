import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def block(driver):
    try:
        # Wait for the page to load and element to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'x6s0dn4 x78zum5 xdt5ytf xl56j7k')])"))
        )

        # Find the div/span element
        element = driver.find_element(By.XPATH, "(//div[contains(@class, 'x6s0dn4 x78zum5 xdt5ytf xl56j7k')])")

        # Execute JavaScript to click the element
        driver.execute_script("arguments[0].click();", element)
        
        # Wait for the button to be present
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'x7r02ix xf1ldfh x131esax xdajt7p xxfnqb6 xb88tzc xw2csxc x1odjw0f x5fp0pe')]//button)[1]"))
        )

        button = driver.find_element(By.XPATH, "(//div[contains(@class, 'x7r02ix xf1ldfh x131esax xdajt7p xxfnqb6 xb88tzc xw2csxc x1odjw0f x5fp0pe')]//button)[1]")

        button.click()

        print("First button clicked successfully.")

        # Wait for the next button to be present
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'x78zum5 xdt5ytf x1crbq5u xvrdyt3 x179zr98')]//button)[1]"))
        )

        button = driver.find_element(By.XPATH, "(//div[contains(@class, 'x78zum5 xdt5ytf x1crbq5u xvrdyt3 x179zr98')]//button)[1]")

        button.click()

        print("Second button clicked successfully.")
        
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")

def following(driver):
    print("Opening Instagram...")
    driver.get('https://www.instagram.com/blockout.2024_/')
    time.sleep(2)  # Wait for the page to load

    try:
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd')]"))
        )
        time.sleep(2)
        if len(elements) > 1:
            driver.execute_script("arguments[0].click();", elements[1])
        else:
            print("Expected elements not found on the profile page.")
            return []

        time.sleep(2)
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')]"))
        )
        print("Printing Elements.....")
        return elements
    except Exception as e:
        print(f"Could not find elements: {e}")
        return []

def start_automation(username, password):
    # Determine the path to the chromedriver executable
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        webdriver_path = os.path.join(sys._MEIPASS, 'chromedriver.exe')
    else:
        webdriver_path = 'chromedriver.exe'

    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("window-size=300,600")  # Set the window size to a minimal width and height

    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Opening Instagram...")
        driver.get('https://www.instagram.com')
        time.sleep(2)

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        time.sleep(10)  # Wait for login to complete

        print("Opening profile page...")
        driver.get('https://www.instagram.com/blockout.2024_/')
        time.sleep(3)  # Wait for the page to load

        # Find elements to click
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd')]")
        ))

        if len(elements) > 1:
            driver.execute_script("arguments[0].click();", elements[1])
        else:
            print("Expected elements not found on the profile page.")
            return

        time.sleep(4)

        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')]")
        ))
        print("Printing Elements.....")

        while True:
            try:
                if elements:
                    driver.execute_script("arguments[0].click();", elements[0])
                    print("Clicked an element")
                    time.sleep(4)
                    block(driver)
                    time.sleep(2)
                    elements = following(driver)
                else:
                    print("No elements found to click.")
                    break
            except Exception as e:
                print(f"Could not click element: {e}")
                break

        print("Finished clicking elements")

    finally:
        # Close the browser
        driver.quit()

# Create the GUI window
root = tk.Tk()
root.title("Free Palestine")
root.geometry("925x500+300+200")  # Set the window size
root.configure(bg="white")
root.resizable(False, False)

# Create a main frame for organizing layout
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Create a frame for the image on the left with extra left margin
image_frame = tk.Frame(main_frame, bg="white")
image_frame.grid(row=0, column=0, padx=(50, 10), pady=10)  # Added left margin with padx=(50, 10)

# Load and display the image
try:
    image = Image.open("signin_image.png")  # Replace with your image file
    image = image.resize((400, 300))  # Resize the image to fit the GUI
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(image_frame, image=photo, bg="white")
    image_label.image = photo  # Keep a reference to the image
    image_label.pack()
except Exception as e:
    print(f"Error loading image: {e}")

# Create a frame for the content on the right
content_frame = tk.Frame(main_frame, bg="white")
content_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Center the content frame
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Create an internal frame to center elements within content_frame
inner_frame = tk.Frame(content_frame, bg="white")
inner_frame.pack(expand=True)

# Create a label for the title
title_label = tk.Label(inner_frame, text="Sign in", font=("Helvetica", 24), bg="white")
title_label.pack(pady=10)

# Create entry widgets for username and password
username_label = tk.Label(inner_frame, text="Username:", font=("Helvetica", 14), bg="white")
username_label.pack(pady=5)
username_entry = tk.Entry(inner_frame, font=("Helvetica", 14))
username_entry.pack(pady=5)

password_label = tk.Label(inner_frame, text="Password:", font=("Helvetica", 14), bg="white")
password_label.pack(pady=5)
password_entry = tk.Entry(inner_frame, show="*", font=("Helvetica", 14))
password_entry.pack(pady=5)

# Create a label for error messages
error_label = tk.Label(inner_frame, text="", foreground="red", bg="white", font=("Helvetica", 12))
error_label.pack(pady=5)

# Create a button to start the automation
def start_button_click():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        error_label.config(text="Username and Password are required!")
    else:
        error_label.config(text="")
        start_automation(username, password)

start_button = ttk.Button(inner_frame, text="Sign in", command=start_button_click)
start_button.pack(pady=20)

# Run the GUI
root.mainloop()