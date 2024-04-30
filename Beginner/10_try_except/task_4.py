import time
from datetime import datetime

try:
    while True:
        now = datetime.now()
        time.sleep(2)
        print(now.strftime("%X"))
except KeyboardInterrupt:
    print("stopped")

