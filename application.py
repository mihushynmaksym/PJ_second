from selenium import webdriver
__author__ = 'Max'


class Application:

    def __init__(self):
        self.app = webdriver.Chrome()

    def check_meta_one(self):
        wd = self.app
        area = wd.find_element_by_name('description')
        text = area.get_attribute('content')
        return(text)

    def check_meta_two(self):
        wd = self.app
        area = wd.find_element_by_xpath("//meta[@property='og:description']")
        text = area.get_attribute('content')
        return(text)

    def check_title(self):
        wd = self.app
        area = wd.find_element_by_tag_name("title")
        text = area.get_attribute("innerText")
        return (text)

    def check_h1_one(self):
        wd = self.app
        area = wd.find_element_by_xpath("//h1[@class='vcard-names']")
        text1 = area.find_element_by_xpath(".//span[@class='p-name vcard-fullname d-block']").text
        text2 = area.find_element_by_xpath(".//span[@class='p-nickname vcard-username d-block']").text
        return (text1, text2)

    def check_h1_two(self):
        wd = self.app
        area = wd.find_element_by_xpath("//h1[@class='alt-h0 text-white lh-condensed-ultra mb-3']")
        text = area.get_attribute("innerText")
        return(text)

    def go_to_page(self, url):
        wd = self.app
        wd.get(url)

    def destroy(self):
        wd = self.app
        wd.quit()