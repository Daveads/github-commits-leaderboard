#!/usr/bin/env bash
# crontab auto run this file
# crontab command:
# 59 22 * * 0  /path/to/your_script.sh

cd /path/repo_path/
git pull

git add .
today=`date +"%Y-%m-%d"`
git commit -m "board update $today"
git push origin main
