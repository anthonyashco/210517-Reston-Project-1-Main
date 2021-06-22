from behave import given, when, then


@given("the user is on the login page")
def login_page(context):
    context.driver.get("http://localhost:8080")


@when("the user clicks the login button")
def click_login(context):
    context.expense_page.login_button().click()


@when("the user inputs their username")
def input(context):
    context.driver.implicitly_wait(1)
    context.expense_page.login_email().send_keys("employee@email.com")


@when("the user inputs their password")
def input(context):
    context.driver.implicitly_wait(1)
    context.expense_page.login_password().send_keys("employee@email.com")


@when("the user clicks submit")
def submit(context):
    context.driver.implicitly_wait(1)
    context.expense_page.submit_button().click()


@then("the user gets logged in")
def logged_in(context):
    pass
