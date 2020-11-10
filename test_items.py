import pytest
from selenium import webdriver
import time

def test_goods_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30) 
    button_add_to_basket = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button_add_to_basket, "No Button to add products to the cart!"

