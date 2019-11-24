#!/bin/sh

exec 1>>`basename $0`.log
date_current=`date +%Y%m%d%H%M%S`
echo "系统时间为: ${date_current}"
