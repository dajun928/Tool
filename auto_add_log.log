#!/bin/sh
if [ $# -ne 1 ]
then
 echo "Usage:sh $0   YYYYMMDD "
  exit 1
fi
V_DT=$1
 
exec 1>>`basename $0`.log
date_current=`date +%Y%m%d`
echo "传入时间为: ${V_DT}"
echo "系统时间为: ${date_current}"
exit 0
