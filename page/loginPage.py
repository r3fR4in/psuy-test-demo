from page.basePage import Page
from selenium.webdriver.common.by import By
from time import sleep

"""登录"""
class loginPage(Page):

    # 用户名输入框
    username_input = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[2]/form/label[1]/div/div/div/label/div/div[1]/div[2]/input')
    # 密码输入框
    password_input = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[2]/form/label[2]/div/div/div/label/div/div[1]/div[2]/input')
    # 登录按钮
    login_button = (By.XPATH, '//*[@id="q-app"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/img')
    # 接受按钮
    accept_btn = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/button[2]')
    # 旧密码
    ogPassword_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[1]/div[2]/div[1]/div[1]/input')
    # 新密码
    newPassword_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[2]/div[2]/div[1]/div[1]/input')
    # 确认新密码
    checkPassword_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[3]/div[2]/div[1]/div[1]/input')
    # 保存
    save_btn = (By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/button[2]')

