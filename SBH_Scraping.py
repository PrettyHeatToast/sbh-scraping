from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from seleniumrequests import Chrome
from tqdm import tqdm
import img2pdf
import os

target = "C:/Users/???"
tmp = "c:/Windows/Temp"
index = []

mail = "???"
password = "???"

titel = 'Onderwijs en maatschappij'
pages = 100
urlbase = "https://content.standaardstudentshop.be/CMS/CDS/Standaard%20Boekhandel/Published%20content/AHS/2220160076716%20Onderwijs%20en%20maatschappij/js/../Resources/1565f966-2b84-4191-be5d-211563a9520e.pdf_/"


# Sets up the selenium scraping
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = Chrome(options=chrome_options)
browser.get('https://arteveldehs.standaardstudentshop.be/Login?returnUrl=https://ecursus.standaardstudentshop.be/Security/SAML2/AssertionConsumerService.aspx&threeShips=True&relaystate=1184f3a7-88d1-43d1-9a88-8edc7e91f88a&relayid=_f1c595d8-2c11-4e3c-9651-5c90b9cdab88')
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "i0116"))).send_keys(mail)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "i0118"))).send_keys(password)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
browser.get(urlbase + '1.png')

# Runs through every page and downloads the corresponding .png
for page in tqdm(range(1, pages), desc="Downloading files"):
    url = urlbase + str(page) + ".png"
    filename = tmp + "/" + str(page) + ".png"

    response = browser.request('GET', url)

    file = open(filename, "wb")
    file.write(response.content)
    file.close()  

    index.append(filename)

# Exits the selenium browser
browser.quit()

# Converts all .pngs to a single .pdf
for i in tqdm([1], desc="Compiling PDF"):
    with open(target + titel + ".pdf","wb") as f:
        f.write(img2pdf.convert(index))

# Removes all redundant files
for i in tqdm(index, desc="Deleting redundant files"):
    os.remove(i)

print("Done!")













