import time

from numset import NumSet
import utils
# Statistics Calculator

# Global variables
DASH = '---------------------------------------------------'
OPTIONS = {
    1: 'mean',
    2: 'median',
    3: 'mode',
    4: 'population variance',
    5: 'population standard deviation',
    6: 'sample variance',
    7: 'sample standard deviation',
    8: 'sort list',
    9: 'mean absolute deviation',
    10: 'five-number summary',
    11: 'interquartile range and outlier detector',
    12: 'mean-based summary',
    13: 'median-based summary'
}
START_STRING = '''
STATISTICS CALCULATOR 
---------------------------------------------------
\t- 'start' to start solver
\t- 'help' for list of functions
\t- 'exit' to exit program
\t- 'delay' to adjust print delay settings
'''

# Functions
def start(instructions):
    num_list = []
    while True:
        input_nums = input('> ')
        try:
            input_nums = int(input_nums)
            num_list.append(input_nums)
            print('Added!')
            continue
        except ValueError:
            pass
            # if not int, try commands below

        if input_nums == 'b' and len(num_list) >= 1:
            num = num_list.pop()
            utils.fancy_print(f'Removed {num} from the list . . .')
        elif input_nums == 'b' and len(num_list) < 1:
            utils.fancy_print('Invalid command. List is empty.')
        elif input_nums == 'd':
            nums = ', '.join(map(str, num_list))
            msg = 'Numbers: ' + nums
            utils.fancy_print(msg)
        elif input_nums == 'r':
            num_list.clear()
            utils.fancy_print('List cleared . . .')
        elif input_nums == 'o':
            msg = 'Saving list of numbers . . .'
            nums = 'Numbers: ' + ', '.join(map(str, num_list))
            utils.fancy_print(msg)
            utils.fancy_print(nums)
            return num_list
        elif input_nums == 'x':
            return 'x'
        else:
            utils.fancy_print('Syntax error.')
            print(instructions)

def start_solving(NumSetObject):
    num_set = NumSetObject

    while True:
        print('')
        print(DASH)
        utils.fancy_print('Input Command')
        instructions = "\t'help' for list of functions\n\t'd' for list of numbers\n\t'x' to exit to main or restart session"
        print(instructions)
        command = input('> ')
        try:
            command = int(command)
        except ValueError:
            pass

        if command == 'help':
            for k, v in OPTIONS.items():
                msg = f'{k}: {v}'
                utils.fancy_print(msg)
            continue
        elif command == 'd':
            msg = 'Numbers: ' + ', '.join(map(str, num_set.nums))
            utils.fancy_print(msg)
            continue
        elif command == 'x':
            msg = 'Exiting session'
            utils.fancy_print(msg)
            for _ in range(3):
                time.sleep(0.2)
                print('.')
            break
        elif command == 1:
            num_set.mean()
        elif command == 2:
            num_set.median()
        elif command == 3:
            num_set.mode()
        elif command == 4:
            num_set.variance(ntype='population')
        elif command == 5:
            num_set.stddev(ntype='population')
        elif command == 6:
            num_set.variance(ntype='sample')
        elif command == 7:
            num_set.stddev(ntype='sample')
        elif command == 8:
            num_set.sort_nums()
        elif command == 9:
            num_set.mad()
        elif command == 10:
            num_set.five_num_summary()
        elif command == 11:
            num_set.iqr_outlier()
        elif command == 12:
            num_set.mean_based()
        elif command == 13:
            num_set.median_based()
        else:
            utils.fancy_print('Command unknown!')


def main():
    while True:
        print(START_STRING)

        enter = input('> ')

        if enter == 'start':
            print(DASH)
            utils.fancy_print('Give the list of numbers for the problem.')
            instructions = "Please only enter numbers or commands:\n\t'd' to display current numbers\n\t'b' to delete previous number inserted\n\t'r' to reset list\n\t'o' if done entering numbers\n\t'x' to exit to main\n"
            print(instructions)

            num_list = start(instructions)
            if num_list == 'x': continue

            numbers = NumSet(num_list)
            start_solving(numbers)

        elif enter == 'help':
            print(DASH)
            for k, v in OPTIONS.items():
                msg = f'{k}: {v}'
                utils.fancy_print(msg)

            print(DASH)
            continue

        elif enter == 'exit':
            msg = 'Exiting program'
            utils.fancy_print(msg)
            msg = '.'
            for _ in range(3):
                utils.fancy_print(msg, 0.5)

            break

        elif enter == 'delay':
            delay = input('WARNING: If ever delay is too long and you want to stop, press ctrl-C\nAdjust delay settings. Default = 0.02. No Delay = 0\ndelay = ')
            try:
                delay = float(delay)
            except ValueError:
                utils.fancy_print('Please input numbers only. If ever delay is too long and you want to stop, press ctrl-C')
                continue
            utils.set_delay(delay)

        else:
            utils.fancy_print('Syntax error!')
            continue

# Execute program
if __name__ == '__main__':
    main()