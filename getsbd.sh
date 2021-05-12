#!/bin/sh

fdm -v fetch
sudo /usr/bin/find "/home/root-gy/Mail/marlin" -type f -iname '*.sbd' -size 32c -exec /usr/bin/python3 "/home/root-gy/Mail/readmailsbd/unpack_weather.py" {} "/var/www/marlin" \; -exec /usr/bin/mv {} /home/root-gy/Mail/marlin-archive \;
#sudo /usr/bin/find '/home/root-gy/Mail/marlin' -type f -iname '*.sbd' -size 32c -exec /usr/bin/python3 '/home/root-gy/Mail/readmailsbd/unpack_weather.py' {} '/var/www/marlin' \; -delete
#sudo find marlin -type f -iname '*.sbd' -size 32c -exec /home/root-gy/Mail/readmailsbd/unpack_weather.py {} "/var/www/marlin" \;
#find ~/Mail/attachments -type f -iname '*.sbd' -size 32c -exec bin2csv {}>>$(date --iso-8601=minute).csv \; -delete 