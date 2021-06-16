import sys
import os
import logging
import logging.handlers

from mytrader import MyTrader
from PyQt5.QtWidgets import QApplication

def logger():

    if not os.path.exists('logs/'):
        os.makedirs('logs/')

    log = logging.getLogger('logger')
    log.setLevel(logging.INFO)

    log_fh = logging.handlers.TimedRotatingFileHandler(filename='logs/log.txt', when='midnight', encoding='utf-8', backupCount=120)
    log_fh.setLevel(logging.DEBUG)
    log_sh = logging.StreamHandler()
    log_sh.setLevel(logging.INFO)

    fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    log_fh.setFormatter(fmt)
    log_sh.setFormatter(fmt)

    log.addHandler(log_fh)
    log.addHandler(log_sh)
    
    pass

def main():
    logger()

    app = QApplication(sys.argv)

    trader = MyTrader()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
