from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def go_to_amazon(browser):
    browser.get("http://www.amazon.com")
    assert "Amazon" in browser.title

def go_to_search_results(browser, target):
    assert "Amazon" in browser.title
    input_element = browser.find_element_by_id('twotabsearchtextbox')   
    assert input_element != None
    input_element.clear()
    input_element.send_keys(target)
    input_element.send_keys(Keys.RETURN)
    time.sleep(3)

def scrape_search_results(browser):
    assert "Amazon" in browser.title
    search_list = browser.find_element_by_id("s-results-list-atf")
    assert search_list != None
    search_items = search_list.find_elements_by_tag_name("li")
    assert type(search_items) is list
    assert len(search_items) >= 1
    search_titles = []
    for item in search_items:
        headers = item.find_elements_by_tag_name("h2")
        if len(headers) == 1:
            search_titles.append(headers[0].text)
    return search_titles
 
if __name__ == "__main__":
    browser = webdriver.Chrome()
    go_to_amazon(browser)
    go_to_search_results(browser,"computer")
    results = scrape_search_results(browser)
    browser.close()
    for result in results[0:10]:
        if "dell" in result.lower():
            print("dell is in the top 10 products today!")
            exit(0)
    print("dell should pay more attention to it!")
