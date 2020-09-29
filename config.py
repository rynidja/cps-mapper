import logging as logger

# Logger config
logger.basicConfig(level=logger.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')


# Buttons to be mapped KeyCodes
# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
LBTN_KEY = 0x06  # Left mouse button mapper  # Mouse button5(xButton2)[Browser forward]
RBTN_KEY = 0x05  # Right mouse button mapper  # Mouse button4(xButton1)[Browser backward]


# Mouse buttons event values
LBTN_P = 0x2  # Left mouse button press event value
LBTN_R = 0x4  # Left mouse button release event value

RBTN_P = 0x8  # Right mouse button press event value
RBTN_R = 0x10  # Right mouse button release event value


# Default cps values
LCPS = 12  # Default left mouse button cps value
RCPS = 12  # Default right mouse button cps value


# Bool Stuff
RCLICKING = False
LCKICKING = False
