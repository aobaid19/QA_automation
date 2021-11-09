# -*- coding: utf-8 -*-
"""

@author: Asad
"""

"""Scenario: Validate job description on careers page
	Given I open google chrome
	When I open www.labcorp.com
	And I wait 3 seconds
	When I search Careers
	Then search results for Careers should appear
	When I search term as QA Test Automation Developer
	And I wait 3 seconds
	Then search results for QA Test Automation Developer should appear
    Then I validate “The right candidate for this role will participate in the test automation technology development and best practice models.”
    Then I validate second bullet point under Management Support as “Prepare test plans, budgets, and schedules.” 
    Then I validate third requirement as “5+ years of experience in QA automation development and scripting.” """


from selenium import webdriver

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



#chrome driver
driver = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)


driver.get("https://www.labcorp.com")


driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()

 
# careerPage = driver.find_element_by_link_text("Careers").click()
careerPage = driver.find_element_by_partial_link_text("Careers").click()

#driver.find_element_by_xpath("//button[text()='Accept']").click()

inputElement = search = driver.find_element_by_name("Keyword Search").click()
inputElement.send_keys('1234')

#driver.find_element(By.linkText("Careers")).click();					



#elems = driver.find_elements_by_xpath("//a[@href]")
# elems = driver.find_elements_by_xpath("Labcorp")

# for elem in elems:
    # print(elem.get_attribute("href"))
    
time.sleep(3)
#assert text on page
element1 = driver.find_element_by_tag_name('h1')
assert element1.text == "The right candidate for this role will participate in the test automation technology development and best practice models."
element2 = driver.find_element_by_tag_name('h2')
assert element2.text == "Prepare test plans, budgets, and schedules."
element3 = driver.find_element_by_tag_name('h3')
assert element3.text == "5+ years of experience in QA automation development and scripting."
driver.close()


"""Scenario: Validate job description on careers page
	Given: user calls post API to load employee data with request <json>
	When I make the post call
	Then I validate a 201 response code is returned by the API
	Then I validate the database fields with JSON request
	When I make the second get call to get data back from server
	Then I validate a 200 response code is returned by API
	Then I validate response matches input json request
	Example:
	|request|
|employee.json|
|Invalidemployee.json|"""

# read input file
file = open (file location)
json_input = json.loads(json_input)
request_json = json.loads(json_input)

#make post call
response = requests.post(postURL, request_json)

#validate response code
 assert response.status_code == 201  

#getURL = “https://6143a99bc5b553001717d06a.mockapi.io/testapi/v1//Users”

#send get request

getResponse = requests.get(getURL)

#validate response 
assert getResponse.content ==employee.json

