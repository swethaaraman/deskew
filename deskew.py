import cv2
import numpy
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path = r"/Users/swethaa/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.dropbox.com/login")
driver.find_element_by_name("login_email").send_keys("aahtews2018@gmail.com")
time.sleep(2)
password = driver.find_element_by_name("login_password")
password.send_keys("cellphone@123")
time.sleep(2)
password.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_class_name("recents-item__heading").click()
time.sleep(4)
driver.find_element_by_xpath("""//*[@id="react-file-viewer"]/div/div/div[1]/div/div[2]/div[2]/div/div/button/div/button""").click()
driver.find_element_by_xpath("""//*[@id="react-file-viewer"]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/nav/div/button""").click()
image = cv2.imread('ab.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
pixel = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
pixelcoordinates = numpy.column_stack(numpy.where(pixel > 0))
angle = cv2.minAreaRect(pixelcoordinates)[-1]
(height, width) = image.shape[:2]

if angle < -45:
    angle = -(90 + angle)
else:
    angle = - angle
matrix = cv2.getRotationMatrix2D((width / 9, height / 9), angle, 1.0)
rotatedimage = cv2.warpAffine(image, matrix, image.shape[:2],
                              cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
print("angle:{:.4f}".format(angle))
outputwindow = cv2.resize(rotatedimage, (500, 500))
cv2.imshow("Output", outputwindow)
inputwindow = cv2.resize(image, (500, 500))
cv2.imshow("Input", inputwindow)
cv2.waitKey(0)
