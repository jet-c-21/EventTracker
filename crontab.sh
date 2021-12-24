#!/bin/bash

# Ensure the env-vars are in the crontab env
echo "ENV-VARS :"
printenv
printenv >> /etc/environment

# Ensure the log file exists
mkdir -p /EventTracker/log
touch /EventTracker/log/crontab.log

# Ensure permission on the command
chmod a+x /EventTracker/crontab.sh

# Added a cronjob in a new crontab
echo "*/10 * * * * cd /EventTracker && /usr/local/bin/python main.py >> /EventTracker/log/crontab.log 2>&1" >/etc/crontab
#cd /EventTracker && /usr/local/bin/python main.py >> /EventTracker/log/crontab.log 2>&1
#echo "* * * * * cd /EventTracker && whoami >> /EventTracker/log/crontab.log 2>&1" >/etc/crontab
#echo "* * * * * which python && whoami" >/etc/crontab

# Registering the new crontab
crontab /etc/crontab

# Starting the cron
/usr/sbin/service cron start

# Displaying logs
# Useful when executing docker-compose logs mycron
tail -f /EventTracker/log/crontab.log
