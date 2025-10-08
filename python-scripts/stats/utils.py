import sys
import time

DELAY = 0.02

def set_delay(new_delay):
    global DELAY
    DELAY = new_delay

def fancy_print(phrase, delay=None):
    if delay is None:
        delay = DELAY
    unf_msg = ''
    for char in phrase:
        unf_msg += char
        sys.stdout.write('\r' + unf_msg)
        time.sleep(delay)
    print('')
