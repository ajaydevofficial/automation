from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from utils import read_csv_to_json
from selenium.webdriver.common.keys import Keys


def url_checker():

    # You can mofity this to support a web url as well
    filepath = 'urls.csv'
    key = "Url"
    urls = read_csv_to_json(filepath)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    while True:
        for entry in urls:
            url = entry["Url"]
            phone_number_query = url.split('?')[1].split('=')[1]

            driver.get(url)
            phone_element = driver.find_element_by_id('phone')
            number_in_input = phone_element.get_attribute("value")
            
            print('Query: {}, Value: {}'.format(phone_number_query, number_in_input))
            if not number_in_input == phone_number_query:
                raise Exception("Bug! Numbers not matching")

            buttons = driver.find_elements_by_tag_name('button')
            if len(buttons) == 0:
                raise Exception("Error! No button found in page")
            
            submit_button = buttons[0]
            submit_button.click()

            print('No bug: Submitted form! Iteration ends successfully')



if __name__ == '__main__':

    url_checker()