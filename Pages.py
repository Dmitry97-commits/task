from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class Base:
    def __init__(self,driver):
        self.driver = driver


class MainPage(Base):

    def enter_name_game(self,text):
         Steam_input_field = self.driver.find_element_by_id("store_nav_search_term")
         Steam_input_field.send_keys(text)
         Steam_input_field.send_keys(Keys.ENTER)

class Search(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.list_with_price = []

    def do_click_sorted_by_price(self):
        Sorted_by_price_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,"sort_by_trigger")))
        Sorted_by_price_field.click()

    def do_click_button_price_desc(self):
        Button_price_desc = self.driver.find_element_by_id("Price_DESC")
        Button_price_desc.click()
        time.sleep(5)

    def get_price_and_write_in_file(self,number):
        Prices_list = self.driver.find_elements_by_xpath(
            "//*[contains(@class, 'search_price ') and contains(@class, 'responsive_secondrow')]")

        for price in Prices_list:
            if not price.text or price.text.isalpha():
                    continue
            if len(price.text) >= 7:
                s1 = price.text.split('\n')[-1]
                self.list_with_price.append(float(s1.replace('$','')))

            else:
                self.list_with_price.append(float(price.text.replace('$','')))

            if len(self.list_with_price) == number:
                        break
        print(self.list_with_price)
        return (self.list_with_price)


    def check_sorted(self):
        list_sorted = all(self.list_with_price[i] <= self.list_with_price[i + 1] for i in range(len(self.list_with_price) - 1))
        if list_sorted:
            print('Отсортировано верно')
            return True , {'Отсортировано верно'}
        else:
            print('Отсортировано неверно')
            return False , {'Отсортировано неверно'}






        # print(list_with_price)
        # return list_with_price
        # if list_with_price != list_with_price.sort():
        #     print("Отсортиравано верно")
        #     print(list_with_price)
        #     print(list_with_price.sort())
        # else:
        #     print('Отсортировано не верно')
        #     print(list_with_price)
        #     print(list_with_price.sort())



