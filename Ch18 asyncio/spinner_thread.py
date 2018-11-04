import threading
import itertools
import time
import sys

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))

def slow_function(n_sec):
    time.sleep(n_sec)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('Spinning!', signal))
    print('spinner object:', spinner)
    spinner.start()
    # print('spinner object:', spinner)
    result = slow_function(1) # Wait/block for a few seconds
    signal.go = False
    spinner.join() # Wait/block until spinner thread stops
    # print('spinner object:', spinner)
    return result

def main():
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':
    main()
