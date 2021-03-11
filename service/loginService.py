from page.loginPage import loginPage
from time import sleep


"""登录"""
class loginService(loginPage):

    def login(self, username, password):
        # 判断当前浏览器是否为新打开，如是则在当前页面打开网址，否则新建标签页打开网址
        if self.driver.current_url != "data:,":
            self.driver.execute_script("window.open('" + self.base_url + "')")
            self.driver.switch_to.window(self.driver.window_handles[-1])
        else:
            self.open()
        self.click(*self.accept_btn)
        self.input(username, *self.username_input)
        self.input(password, *self.password_input)
        sleep(0.5)
        self.click(*self.login_button)
        sleep(1)

    def reset(self, ogPassword, newPassword, checkPassword):
        self.input(ogPassword, *self.ogPassword_in)
        self.input(newPassword, *self.newPassword_in)
        self.input(checkPassword, *self.checkPassword_in)
        self.click(*self.save_btn)
