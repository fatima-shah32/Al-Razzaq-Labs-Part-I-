import logging

# Task 1: Configure logging (console + file)
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Also enable console logging (optional but useful for labs)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

# Task 2: Log messages at different levels

logging.debug("This is a DEBUG message (used for debugging)")
logging.info("This is an INFO message (general information)")
logging.warning("This is a WARNING message (something unexpected)")
logging.error("This is an ERROR message (something went wrong)")
logging.critical("This is a CRITICAL message (serious failure)")
