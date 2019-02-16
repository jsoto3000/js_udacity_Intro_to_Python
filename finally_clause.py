# why python needs finally clause

# code below will continue to run even when press ctrl-c

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except :
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

# code below will interrupt when press ctrl-c
# specifies which error to handle
# with tuple

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except (ValueError, KeyboardInterrupt):
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

# code below will interrupt when press ctrl-c
# specifies which error to handle
# with multiple except blocks

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except  KeyboardInterrupt:
        print('\nNo input taken!')
        break
    finally:
        print('\nAttempted Input\n')

