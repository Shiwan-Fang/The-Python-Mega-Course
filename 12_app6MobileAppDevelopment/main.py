from zoneinfo import available_timezones
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
import glob
import random
from datetime import datetime  # meand a detetime class of a datetime module
from pathlib import Path

Builder.load_file('12_app6MobileAppDevelopment//design.kv')


class LoginScreen(Screen):
    # the subclass of Screen
    # has to been the same name as the kv file
    # 这样才能将两个文件的内容连接起来
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        # self is refering to the class LoginScreen
        # manager is a property of screen, since the class LoginScreen is inherited from Screen(imported from kivy.uix.screenmanager)
        # current is the attribute of manager
        # 触发kv文件里的<RootWidge>t里的SignUpScreen，再触发kv文件里的<SignUpScreen>

    def login(self, uname, pword):
        with open("12_app6MobileAppDevelopment//users.json") as file:
            users = json.load(file)  # just give us a dictionary
            if uname in users and users[uname]['password'] == pword:
                self.manager.current = 'login_screen_success'
            else:
                self.ids.login_wrong.text = "Wrong username or password"
                # 让kv文件中<LoginScreen>里id是login_wrong的文本变成等号后的内容


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("12_app6MobileAppDevelopment//users.json") as file:
            users = json.load(file)

        users[uname] = {'username': uname, 'password': pword,
                        'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        # store the username and password in an empty json file

        with open("12_app6MobileAppDevelopment//users.json", 'w') as file:
            json.dump(users, file)  # 将上面这个users字典传到users.json文件里去
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        # 将切换下一个页面的方式改成从右边插入
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()  # 变成小写的字母
        available_feelings = glob.glob(
            "12_app6MobileAppDevelopment//quotes//*txt")  # 抓取这个文件夹里的所有txt格式的文件
        available_feelings = [
            Path(filename).stem for filename in available_feelings]  # 取文件名字中.txt之前的内容

        if feel in available_feelings:
            with open(f"12_app6MobileAppDevelopment//quotes//{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    # ButtonBehavior必须在前面，否则the order may hide it
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
