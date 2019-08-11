import threading
import time

# Constants section
THREAD_NUMBER = 10
OUTPUT_DELAY = 1
# -----------------

# Data section
STEP_COUNT = 0

# -----------------

def thread_step():
    """
    This function must be filled with the function that each thread should do per step
    It should return False when the thread should finish
    :return:
    """
    return True

def thread_flow():
    global STEP_COUNT

    while True:
        if thread_step():
            STEP_COUNT += 1
        else:
            break

def start():
    for i in range(THREAD_NUMBER):
        t = threading.Thread(target=thread_flow, daemon=True)
        t.start()

while True:
    print(f"{STEP_COUNT} steps", end="\r")
    time.sleep(OUTPUT_DELAY)