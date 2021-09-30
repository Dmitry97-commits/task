
from selenium import webdriver
from Pages import MainPage, Search

Number = 10
name_game_fallout = "Fallout"
name_game_witcher = "The Witcher"

driver = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')
driver.get("https://store.steampowered.com/")
Pager = MainPage(driver)
Pager.enter_name_game(name_game_fallout)
Searcher = Search(driver)
Searcher.do_click_sorted_by_price()
Searcher.do_click_button_price_desc()
Searcher.get_price_and_write_in_file(Number)
Searcher.check_sorted()
driver.quit()
# assert (len(Searcher.get_price_and_write_in_file(Number))) == 10