import sys
import time

print("executing ", end="")

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(0,20):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.15)
    sys.stdout.write('\b')
print('\n')