import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'LookingGlass: Rubbish'
    except ZeroDivisionError:
        msg = 'Please do not divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
