from behave.runner import Context
from selenium import webdriver
from features.poms.expense_page import ExpensePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("C:/Users/emuch/Git/chromedriver.exe")
    context.expense_page = ExpensePage(context.driver)


def after_all(context: Context):
    context.driver.quit()
