import logging

from PyQt5.QtCore import QObject
from PyQt5.QAxContainer import QAxWidget

class MyTrader(QObject):
    
    def __init__(self) -> None:
        self.log = logging.getLogger('logger')
        
        self.title()

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.OnEventConnect().connect(self.kiwoom_OnEventConnect)
        pass

    def title(self):
        self.log.info('Hello MyTrader!')
        pass

    def kiwoom_OnEventConnect(self, result):
        if result == 0:
            self.log.debug('Log-in succeed')
        else:
            self.log.error('falied to log in - %d', result)
        pass 