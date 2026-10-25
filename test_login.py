from playwright.sync_api import expect


def login(page, username, password):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)

    page.get_by_role("button", name="Login").click()
    
    
def test_successful_login(page):
    login(page, "standard_user", "secret_sauce")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    

def test_invalid_login(page):
    login(page, "standard_user", "wrong_password")

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_contain_text("Username and password do not match")
    

def test_add_item_to_cart(page):
    login(page,"standard_user", "secret_sauce")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    expect(cart_badge).to_have_text("1")
    

def test_remove_item_from_cart(page):
    login(page,"standard_user", "secret_sauce")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    expect(cart_badge).to_have_text("1")

    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    expect(cart_badge).not_to_be_visible()
    

def test_complete_checkout(page):
    login(page,"standard_user", "secret_sauce")
   
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    page.locator('[data-test="shopping-cart-link"]').click()

    page.get_by_role("button", name="Checkout").click()

    page.get_by_placeholder("First Name").fill("Test")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")

    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()

    checkout_message = page.locator('[data-test="complete-header"]')

    expect(checkout_message).to_have_text("Thank you for your order!")