# -*-coding:utf-8-*-
import webbrowser
from utils.interpreters import basicInterpreter
from wox import Wox, WoxAPI


class Main(Wox):
    def query(self, key):
        return basicInterpreter.BasicInterpreter.interpret(key)

    def open_page(self, url):
        webbrowser.open(url)
        WoxAPI.change_query(url)
