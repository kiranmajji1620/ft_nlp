import logging


# Levels of severity
# Level     Function
# DEBUG     logging.debug() : Provides detailed information that's valuable to developer.
# INFO      logging.info()  : Provides general information about what's going on with the program
# WARNING   logging.warning() : Indicates that there's something you should look into
# ERROR     logging.error()   : Alerts you to an expected problem that's occured in program
# CRITICAL  logging.critical(): Tells you that a serious error has occurred and may have crashed the application
# Formatting, adding time, configuring severity of logs
def log_console():
    logging.basicConfig(format="{asctime} - {levelname} - {name} - {message}", style = "{", level="DEBUG")
    # Additional information, like the time of the log message becomes even more important when you want to keep a log of incidents over time or when you want to persist your logs in a external file.
    logging.basicConfig(level="DEBUG")


    # Once .basicConfig() is called, it can't be re configured.
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a Warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    # debug() and info() messages didn't get logged. Coz, by default, the logging module logs the messages with a severity level of warning or above. Can change this/

    # Setting the level
    # This should be set at the beginning of the code before logging anything.
    # logging.basicConfig(level=logging.DEBUG) 
    # logging.basicConfig(level=10)
    logging.debug("This debug will be logged now")

def log_file():
    logging.basicConfig(filename="app.log", encoding="utf-8", filemode="w", format="{asctime} - {levelname} - {message}", style = "{", datefmt="%Y-%m-%d %H:%M", level="DEBUG")
    logging.warning("save me!")
    bug = "LadyBug"
    logging.debug(f"This is a {bug}")
    logging.debug(f"This is the name of the file : {__name__}")
    # Logging Exceptions to capture stack traces
    try:
        donuts_per_guest = 89/0
    except ZeroDivisionError:
        # logging.error("Donut Calculation Error", exc_info=True)
        # Or simply say 
        logging.exception("Donut Calculation Error")
        # logging.exception comes with sensitivity of ERROR.
        # This should be called only during exception handling.
        # If you don't want the severity to be ERROR, then we can pass exc_info to be true to that log.

def custom_log():
    # Downside of working with root logger is that the configuration can be cumbersome as you're relying on a single basicConfig(). For bigger projects, you'll need more flexibility for your logging needs.
    jogger = logging.getLogger(__name__)
    # It is a good practice to put __name__ this way, loggers name is always the modules name.
    jogger.warning("This is a jogger warning")
    # custom loggers don't come with additional logging information. And also, we can't call basicConfig(). Instead we'll have to configure our custom logger using handlers and formatters. They give us more flexibility.
    # Handlers : When you want to configure your own loggers
    # Want to send messages to different locations
    kogger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("app.log", mode = "w", encoding="utf-8")
    kogger.addHandler(console_handler)
    kogger.addHandler(file_handler)
    print(kogger.handlers)
    kogger.warning("This is a kogger warning")

    # Handlers send your logs to the output destination we define.
    # With a formatter, we can control the output format by specifying a string format as we did in logging.basicConfig()
    formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")
    # .setFormatter is a method of handler.
    console_handler.setFormatter(formatter)
    kogger.warning("Stay Calm!")

if __name__ == "__main__":
    f = 11
    if f == 1:
        log_file()
    elif f == 2:
        log_console()
    else:
        custom_log()