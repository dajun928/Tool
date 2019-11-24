#!/bin/sh
if [ $# -ne 1 ]
then
 echo "Usage:sh $0   YYYYMMDD "
  exit 1
fi
V_DT=$1
 
date_current=`date +%Y%m%d`
echo "传入时间为: ${V_DT}"  >> $(basename $0).log
echo "系统时间为: ${date_current}" >> $(basename $0).log
echo "tee commant test" 2>&1|tee -a $(basename $0).log     
exit 0
