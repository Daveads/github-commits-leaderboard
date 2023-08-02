#!/usr/bin/env bash
# crontab auto run this file
# crontab command:
# 59 11 * * * /path/to/your_script.sh //will be executed at 11:59 PM every Sunday. 
# Don't run ****

cd /home/ubuntu/git-commit-board
git pull

git add .