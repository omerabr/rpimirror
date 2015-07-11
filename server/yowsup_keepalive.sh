#!/bin/bash

VAL1=$(service whatsapp.sh status)
flag=`echo $VAL1|awk '{print match($0,"not running")}'`;
echo $flag
echo $VAL1
if [ $flag -gt 0 ];then
	VAL2=$(service whatsapp.sh start)
fi
