#!/bin/sh

fdm -v fetch
find ~/Mail/attachments -type f -iname '*.sbd*' -size 32c -exec bin2csv {}>>$(date --iso-8601=minute).csv \; -delete 
