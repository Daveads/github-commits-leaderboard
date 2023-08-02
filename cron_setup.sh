#!/bin/bash

# Function to check if a cron job exists
cronjob_exists() {
    crontab -l | grep -Fxq "$1"
}

# Add git_pull.sh cron job if it doesn't exist
# 11:59 each day
if ! cronjob_exists "59 22 * * * /home/ubuntu/git-commit-board/git_pull.sh"; then
    (crontab -l ; echo "59 22 * * * /home/ubuntu/git-commit-board/git_pull.sh") | crontab -
    echo "Added git_pull.sh cron job."
else
    echo "git_pull.sh cron job already exists. Skipping."
fi

# Add cron.py cron job if it doesn't exist
if ! cronjob_exists "59 22 * * * /usr/bin/python3 /home/ubuntu/git-commit-board/cron.py"; then
    (crontab -l ; echo "59 22 * * * /usr/bin/python3 /home/ubuntu/git-commit-board/cron.py") | crontab -
    echo "Added cron.py cron job."
else
    echo "cron.py cron job already exists. Skipping."
fi
