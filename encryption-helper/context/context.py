import logging


class Context:
    instance = None
    name = ''
    log_level = logging.INFO
    logger = None

    @staticmethod
    def getinstance():
        if Context.instance is None:
            Context()
        return Context.instance

    def __init__(self):
        if Context.instance is not None:
            raise Exception("This is a singleton class")
        else:
            Context.instance = self
        self.set_name('keypy')

    def set_name(self, name):
        self.name = name

    def set_log_level(self, log_level):
        if log_level is None or log_level.strip() == '':
            self.log_level = logging.INFO
            return

        if log_level == 'INFO':
            self.log_level = logging.INFO
        elif log_level == 'DEBUG':
            self.log_level = logging.DEBUG
        elif log_level == 'WARNING':
            self.log_level = logging.WARNING
        elif log_level == 'ERROR':
            self.log_level = logging.ERROR
        elif log_level == 'CRITICAL':
            self.log_level = logging.CRITICAL
        else:
            raise Exception('Invalid logging level defined')

    def init_logging(self):
        self.logger = logging.getLogger(self.name)
        console_handle = logging.StreamHandler()
        self.logger.setLevel(self.log_level)
        log_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        console_handle.setFormatter(log_format)
        if not self.logger.handlers:
            self.logger.addHandler(console_handle)

        self.logger.info('Logging initialized')

    def get_logger(self):
        if self.logger is None:
            self.init_logging()
        return self.logger
