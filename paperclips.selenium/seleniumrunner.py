from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.decisionproblem.com/paperclips/index2.html")
make_clip = driver.find_element_by_id("btnMakePaperclip")
lower_price = driver.find_element_by_id("btnLowerPrice")
increase_price = driver.find_element_by_id("btnRaisePrice")


def keep_demand_at_hunderd_procent():
    for x in range(0, 5):
        lower_price.click()
    while True:
        try:
            clips_in_supply = int(driver.find_element_by_id("unsoldClips").text)
            demand = int(driver.find_element_by_id("demand").text)
            time.sleep(0.1)
            if clips_in_supply < 50:
                increase_price.click()
                print('too few clips increasing price')
                time.sleep(1)
            elif demand < 101 or clips_in_supply > 250:
                lower_price.click()
                print('lowered price: checked demand async')
                time.sleep(2)
            elif demand > 100 or clips_in_supply < 150:
                increase_price.click()
                print('increased price: checked demand async')
                time.sleep(2)
        except:
            continue


def make_clips():
    for x in range(0, 200):
        make_clip.click()
        time.sleep(0.001)
    return


def make_clippers():
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "btnMakeClipper"))
    )
    clipper_element = driver.find_element_by_id("btnMakeClipper")
    number_of_auto_clippers = 0
    while number_of_auto_clippers < 8:
        try:
            time.sleep(3)
            number_of_auto_clippers = int(driver.find_element_by_id("clipmakerLevel2").text)
            print(number_of_auto_clippers)
            funds = float(driver.find_element_by_id("funds").text.strip())
            needed_funds = float(driver.find_element_by_id("clipperCost").text.strip())
            if funds > needed_funds:
                print(funds)
                clipper_element.click()
        except:
            continue


def buy_wire():
    while True:
        time.sleep(2.5)
        try:
            wire = int(driver.find_element_by_id("wire").text)
            print(wire)
            wire_cost = int(driver.find_element_by_id("wireCost").text)
            print(wire_cost)
            wire_buy_button = driver.find_element_by_id("btnBuyWire")
            if wire_cost < 18 and wire < 250:
                print('buying cheap wire')
                wire_buy_button.click()
            if wire < 50:
                print('buying much needed wire')
                wire_buy_button.click()
        except:
            continue




if __name__ == "__main__":
    make_clips()

    executor = ProcessPoolExecutor(3)
    loop = asyncio.get_event_loop()
    demands = asyncio.ensure_future(loop.run_in_executor(executor, keep_demand_at_hunderd_procent))
    #clips = asyncio.ensure_future(loop.run_in_executor(executor, make_clips))
    clippers = asyncio.ensure_future(loop.run_in_executor(executor, make_clippers))
    wire = asyncio.ensure_future(loop.run_in_executor(executor, buy_wire))

    loop.run_forever()
    print('hello')



'''
keep_demand_at_hunderd_procent(driver, lower_price))


while demand < 90:
    LOWERPRICE.click()
    demand = int(driver.find_element_by_id("demand").text)
    
        funds = float(driver.find_element_by_id("funds").text.strip())
    print(funds)
    
        while funds < 5.00:
            make_clip.click()
            time.sleep(0.10)
            funds = float(driver.find_element_by_id("funds").text.strip())
            print(funds)
            
                def get_first_run():

        if funds > 5.00:
            make_clipper = driver.find_element_by_id("btnMakeClipper")
            make_clipper.click()
            time.sleep(2)

'''


