from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

#############################################################################
#------------------------------ UPDATE THESE -------------------------------#
BESTBUY_USERNAME = ""
BESTBUY_PASSWORD = "" # leave blank if you'd rather input inside browser
AUTO_CART_URL_LIST = [ # make sure you update this list
"https://www.bestbuy.ca/en-ca/product/invisibleshield-by-zagg-glass-elite-screen-protector-for-samsung-galaxy-s20-fe/14933491",
"https://www.bestbuy.ca/en-ca/product/2-packs-csmart-premium-tempered-glass-screen-protector-for-samsung-galaxy-s20-fe-5g-2020/15062927",
"https://www.bestbuy.ca/en-ca/product/topsave-case-friendly-flat-full-cover-protection-durable-tempered-glass-for-samsung-s20-fe-20/15078386",
"https://www.bestbuy.ca/en-ca/product/2x-pack-for-samsung-galaxy-a20-a30-anti-shatter-tempered-glass-guard-film-bubble-free-anti-scratch-screen-protector/15168465"
]
#---------------------------------------------------------------------------#


#----------------- THESE CONSTAINTS MIGHT REQUIRE UPDATING -----------------#
SIGN_IN_LINK = "https://www.bestbuy.ca/identity/en-ca/signin?tid=U6Pfv%252Bco%252Bk99SSh%252B9YwD4bJkl83zo4Lv5mJL7O4HlSqIPzZd3MkcUQTZ9goyvqTiQdNnHHVCFHjSLgB3xDRn7R10zE55s502gU3OU%252FhnbtgBJ8DbhfwU2q9M%252FeiieYVWc27oEPJYza3ANTyHay3QRlKsUFPJH3TcpdpjxzznG%252Bk9RvKgt20acEhALCpV2IWzQJg%252BmpakF3VpJV%252Fl4xsntqig2gJrauYvudMy4z24IBE4hSyqsLZiKtoi9Hy1ndSQalzclsxMfY6Jq2moGjyz9ZUDP0Y6kyBuyX1XtDNxl3MH75SIL%252FDtc4Rb0aT8d22Z"
CHROME_DRIVER_LOGGING = False # Change this to true if verbose logging is wanted
#---------------------------------------------------------------------------#


#-------------------- THESE CONSTAINTS MOST LIKELY WILL --------------------#
#-------------------------- NEVER REQUIRE UPDATING -------------------------#
ID_EMAIL_FIELD = 'username'
ID_PASSWORD_FIELD = 'password'
#---------------------------------------------------------------------------#
#############################################################################

def manual_pause(msg="Press enter to continue..\n"):
    input(msg)


def init_connection(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    if not CHROME_DRIVER_LOGGING:
        chrome_options.add_argument("--log-level=3")
        browser = webdriver.Chrome(chrome_options=chrome_options)
    else:
        browser = webdriver.Chrome()
    browser.get(url)
    return browser


def cond_sleep(sleep_time):
    if sleep_time > 0:
        sleep(sleep_time)


def add_to_cart(b, sleep_time=0):
    for url in AUTO_CART_URL_LIST:
        b.get(url)
        buyButton = b.find_element_by_class_name("addToCartButton")
        buyButton.click()
        cond_sleep(sleep_time)


def autofill_sign_in_data(b):
    email_field = b.find_element_by_id(ID_EMAIL_FIELD)
    email_field.send_keys(BESTBUY_USERNAME)
    password_field = b.find_element_by_id(ID_PASSWORD_FIELD)
    password_field.send_keys(BESTBUY_PASSWORD)


if __name__ == "__main__":
    print(("Welcome, to fill the cart you will first need to sign into the"
            "automated Chrome browser. (Look for chrome driver)"))
    print(("Make sure you fill in the urls you will like the script to add to"
            "your cart for first!!"))
    print("Total # of URLs to auto-add:", len(AUTO_CART_URL_LIST))

    b = init_connection(SIGN_IN_LINK)
    autofill_sign_in_data(b)
    print("")
    manual_pause("Press enter ONLY when you are done signing in")

    exit(0)
    
