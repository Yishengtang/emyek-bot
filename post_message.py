#!/usr/bin/env python3

import random
import sys
import time


def get_message():
    with open("quotes.txt") as f:
        choices = f.readlines()
    return random.choice(choices).strip()


def post(message):
    # TODO: write to Slack instead
    print(message)


if __name__ == "__main__":
    # First, only continue a quarter of the time.
    if random.random() > 0.25:
        sys.exit(0)

    # This script will run at the start of the workday. Sleep for a random
    # amount of time before posting the message during business hours.
    work_day_duration = 8 * 60 * 60
    sleep_amount = random.random() * work_day_duration
    time.sleep(sleep_amount)

    message = get_message()
    post(message)
