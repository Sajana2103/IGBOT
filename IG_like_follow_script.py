from selenium import webdriver
from time import sleep,asctime
from numpy import random
from PIL import Image
import os


chrome_web = webdriver.Chrome('chromedriver.exe')

def sleep_time(low,high):
    sleep_for = random.randint(low,high)
    sleep(sleep_for)

def connect_web_chrome(chrome_web, link, username, password):
    chrome_web.get(link)
    sleep(2)
    user = chrome_web.find_element_by_name('username')
    user.send_keys(username)
    sleep(1)
    pw = chrome_web.find_element_by_name('password')
    pw.send_keys(password)
    sleep(1)
    get_image()
    login = chrome_web.find_element_by_class_name('y3zKF     ')
    login.click()

def get_image(): #image name
    current_time = asctime().replace(' ', '-')
    chrome_web.save_screenshot(f"./screens/{str(current_time.replace(':', '-'))}.png")

def image_process(): #saving the image
    cur_dir = os.getcwd()
    os.chdir('./screens')
    file_list = os.listdir()
    for i in file_list:
        new_name = i.lstrip('.png')
        img = Image.open(i)
        box = (55, 52, 800, 600)
        region = img.crop(box)
        os.chdir(cur_dir)
        region.save(f"CROP-{new_name}.png", 'PNG')
        new_file = f"CROP-{new_name}.png"
        print(new_file)
        sleep(2)
        os.chdir('./screens')


def print_this(this):
    print(str(this))
    print('that is true')

def not_now(element):
    not_now = chrome_web.find_element_by_class_name(element)
    not_now.click()
    sleep(3)


def search_bars(element1, element2, keyword):
    search_bar = chrome_web.find_element_by_class_name(element1)
    search_bar.send_keys(keyword)
    sleep(2)
    click_result = chrome_web.find_element_by_class_name(element2)
    click_result.click()
    sleep(3)


def click_post(cl):
    post = chrome_web.find_element_by_class_name(cl)
    sleep_time(1, 3)
    post.click()


def like_follow( like, follow, next):

    click_post('_bz0w')

    for i in enumerate(range(25)):
        sleep_time(2,7)
        get_image()
        sleep_time(1,2)
        web1 = chrome_web.find_elements_by_xpath("//*[name()='svg'][@class='_8-yf5 '][attribute::aria-label]")
        label = web1[5].get_attribute('aria-label')
        if label == 'Like':
            like_post = chrome_web.find_element_by_class_name(like)
            like_post.click()
            print('liked this post')
            sleep_time(2, 3)
        else:
            print('did not liked this post')
        follow_user = chrome_web.find_element_by_xpath(follow)
        if follow_user.text == 'Follow':
            follow_user.click()
            sleep_time(2, 4)
        next_post = chrome_web.find_element_by_class_name(next)
        next_post.click()
        sleep_time(2, 4)


connect_web_chrome(chrome_web, 'https://www.instagram.com/', '', '') #login

sleep(3)

not_now('y3zKF     ') #annoying notification

not_now('HoLwm ') #annoying notification

search_bars('x3qfX', 'z556c', '#artificialintelligence') #you can change the #hashtag


like_follow( 'fr66n', '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button',
             'coreSpriteRightPaginationArrow') #meat and potatoes, Liking and following if haven't already


