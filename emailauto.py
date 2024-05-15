#This project is a basic demonstration of how to use pyautogui and send emails using python.
#this follows the steps i wanted to when i had a ton of mails to send 
import pyautogui
import time
import csv

def read_emails_from_csv(csv_file):
    emails = []
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            email = row[0].strip()  
            emails.append(email)
    
    return emails

# Example usage:
csv_file = 'email.csv'  
emails = read_emails_from_csv(csv_file)

def openmailsend(mail):
    time.sleep(3)
    pyautogui.moveTo(2248, 178)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(772, 565)
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveTo(297, 396)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(445, 282)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write(mail)
    pyautogui.press('enter')
    pyautogui.moveTo(475, 942)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(301, 1436)
    pyautogui.click()
    time.sleep(7)


for email in emails:
    openmailsend(email)
