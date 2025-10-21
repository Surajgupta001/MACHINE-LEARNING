import logging

## Configuring logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('apps.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticLogger')

def add(a, b):
    logger.debug(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    logger.debug(f"Subtracting {b} - {a}")
    return a - b

def multiply(a, b):
    logger.debug(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    logger.debug(f"Dividing {a} / {b}")
    if b == 0:
        logger.error("Attempted to divide by zero")
        return None
    return a / b
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)