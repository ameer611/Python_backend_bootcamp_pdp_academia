import contextlib
import time


# @contextlib.contextmanager
# def log(fileName, mode):
#     print(f"- context manager at {time.strftime('%X')}")
#     print('opened')
#     file = open(fileName, mode)
#     try:
#         yield file
#     finally:
#         print(f"- context manager at {time.strftime('%X')}")
#         print('closed')
#         file.close()

class log:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.opened_file = None

    def __enter__(self):
        print(f"- context manager opened at {time.strftime('%X')}")
        file = open(self.filename, self.mode)
        self.opened_file = file
        return file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"- context manager closed at {time.strftime('%X')}")
        self.opened_file.close()

with log('hello.txt', 'w') as file:
    print('hello')