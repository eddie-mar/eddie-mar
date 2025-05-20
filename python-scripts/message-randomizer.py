import argparse
import random
import string
import sys
import time

def main(args):
    message = args.m
    try_limit = int(args.tries)
    chars = string.ascii_letters + ' '

    for i in message:
        if i in string.punctuation:
            continue
        if i not in chars:
            print('Use letters only for message.')
            return

    final_message = ''
    idx = 0
    tries = 0

    while final_message != message:
        if message[idx] == ' ' or message[idx] in string.punctuation or tries >= try_limit:
            final_message += message[idx]
            char = ''
            idx += 1
            tries = 0
        else:
            tries += 1
            char = random.choice(chars)
            if char == message[idx]:
                final_message += char
                char = ''
                idx += 1
                tries = 0
        sys.stdout.write('\r' + final_message + char)
        #sys.stdout.flush()
        time.sleep(0.02)


    print('\n.')
    time.sleep(0.2)
    print('.')
    time.sleep(0.2)
    print('.')
    time.sleep(0.2)
    print('Message sent !')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Type your message')

    parser.add_argument('-m', help='Message to post', default='I love you Kayzee')
    parser.add_argument('-tries', help='Char tries', default=30)

    args = parser.parse_args()

    main(args)
