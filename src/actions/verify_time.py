import re


# Verify if time is formate H:M
def verify_time(time):
    return bool(re.match(r'^\d{1,2}:\d{2}$', time))
