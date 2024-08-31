import time
from datetime import datetime, timedelta

def countdown_timer(seconds):
    end_time = datetime.now() + timedelta(seconds=seconds)
    
    while True:
        remaining_time = end_time - datetime.now()
        if remaining_time.total_seconds() <= 0:
            print("Time's up!")
            break
        
        # Print the remaining time in HH:MM:SS format
        time_left = str(remaining_time).split(".")[0]  # Remove microseconds
        print(f"Time remaining: {time_left}", end='\r')
        
        time.sleep(1)

# Example: Countdown from 10 seconds
countdown_timer(1234)

