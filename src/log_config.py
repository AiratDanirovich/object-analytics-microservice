import logging

log_conf = logging.basicConfig(level=logging.INFO,
                               format="%(asctime)s : %(filename)s  %(levelname)s %(message)s ",
                               handlers=[
                                   logging.FileHandler("log.txt", mode='w'),
                                   logging.StreamHandler()
                               ],

                               )
