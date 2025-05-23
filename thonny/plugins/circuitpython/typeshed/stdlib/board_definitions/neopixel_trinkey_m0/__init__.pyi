# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for Adafruit NeoPixel Trinkey M0
 - port: atmel-samd
 - board_id: neopixel_trinkey_m0
 - NVM size: 256
 - Included modules: adafruit_pixelbuf, array, board, builtins, collections, digitalio, math, microcontroller, neopixel_write, nvm, os, rainbowio, random, storage, struct, supervisor, sys, time, touchio, usb_cdc, usb_hid, usb_midi
 - Frozen libraries: adafruit_hid, neopixel
"""

# Imports
import microcontroller


# Board Info:
board_id: str


# Pins:
TOUCH1: microcontroller.Pin  # PA03
NEOPIXEL: microcontroller.Pin  # PA05
TOUCH2: microcontroller.Pin  # PA07


# Members:

# Unmapped:
#   none
