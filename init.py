#!/usr/bin/env python3
# -*- coding:utf-8-*-

import tkinter.messagebox
from tkinter import Button, Label, Tk

from lib.functions import set_window_center
from lib.sqlite_helper import DBHelper
from main import App


class InitWindow(Tk):
    """Инициализировать окно или Окно инициализации"""

    def __init__(self):
        Tk.__init__(self)
        self.title("Данные инициализации")
        set_window_center(self, 300, 180)
        self.resizable(False, False)
        self.win_success = None # Окно сообщения об успешной инициализации
        self.init_page()

    def init_page(self):
        """Контроль нагрузки ??? (ориг. 加载控件)"""
        btn_1 = Button(self, text="Инициализировать базу данных", command=self.do_init_db)
        btn_1.pack(expand="yes", padx=10, pady=10, ipadx=5, ipady=5)

    def do_init_db(self):
        """Инициализация"""
        db_helper = DBHelper()
        db_helper.reset_database()
        db_helper.create_database()
        try:
            tmp = db_helper.insert_user("admin", "admin")  # Пользователь по умолчанию
            tmp2 = db_helper.insert_content_by_username(
                "admin",
                "Hello World !",
                "Адрес склада исходного кода ??? (ориг. 源码仓库地址)：https://github.com/doudoudzj/tkinter-app",
                "github",
            )
            tmp3 = db_helper.get_content_by_username("admin")
            print("Добавить пользователя admin:", tmp)
            print("Добавить контент ??? (ориг. 添加内容):", tmp2)
            print("Содержание запроса ??? (ориг. 查询内容):", tmp3)
            self.do_success()
            self.destroy()
        except KeyError:
            print(KeyError)
            self.do_failed()

    def do_failed(self):
        """Стоит ли повторить ??? (ориг. 是否重试)"""
        res = tkinter.messagebox.askretrycancel('Намекать ??? (ориг. 提示)', 'Ошибка инициализации, повторить попытку?', parent=self)
        if res is True:
            self.do_init_db()
        elif res is False:
            self.destroy()

    def do_success(self):
        """Всплывающее окно об успешной инициализации"""
        self.win_success = Tk()
        self.win_success.title("Инициализация прошла успешно")
        set_window_center(self.win_success, 250, 150)
        self.win_success.resizable(False, False)
        msg = Label(self.win_success, text="Инициализация прошла успешно")
        msg.pack(expand="yes", fill="both")

        btn = Button(self.win_success, text="Конечно ??? (ориг. 确定)", command=self.quit)
        btn.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)
        btn_open_app = Button(self.win_success, text="Стартовая программа ??? (ориг. 启动程序)", command=self.open_app)
        btn_open_app.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)

    def open_app(self):
        """Откройте приложение ??? (ориг. 打开应用程序)"""
        self.quit()
        self.win_success.destroy()
        self.win_success.quit()

        App()


if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()
