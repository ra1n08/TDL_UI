"""
@File    :  test.py
@Date    :  2022/03/28
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
"""
import sys
import aigpy
import _thread
import importlib

from tidal_dl.events import *
from tidal_dl.settings import *
from tidal_dl.printf import *
from tidal_dl.enums import *

def enableWebGui():
    try:
        importlib.import_module('nicegui')
        return True
    except Exception as e:
        return False
if not enableWebGui():
    def startWebGui():
        Printf.err("Something went wrong. Try install nicegui library to fix it, Type: `pip3 install nicegui`")
else:
    from nicegui import ui, app
    from nicegui.events import ValueChangeEventArguments

    class 