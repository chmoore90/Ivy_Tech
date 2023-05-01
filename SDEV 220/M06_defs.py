from datetime import datetime
import time
import random

def print_datetime(n):
    sleep_time = random.random()
    time.sleep(sleep_time)
    now = datetime.now()
    return f"Process {n}: {datetime.ctime(now)}"
