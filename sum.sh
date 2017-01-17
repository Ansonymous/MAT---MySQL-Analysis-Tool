#!/bin/bash

mysqlbinlog --base64-output=decode-rows -vv ~/Downloads/mysql-iso/logfile | awk \
'BEGIN {s_type=""; s_count=0;count=0;insert_count=0;update_count=0;delete_count=0;flag=0;} \
{if (match($0, /#16./)) {printf "\nTimestamp : " $1 " " $2 " \033[32mTable : " $(NF-4) "\033[0m"; flag=1} \
else if (match($0, /update./)) {printf "\nTimestamp : \033[33m" $1 " " $2 " " $3 " " $4 " " $(NF);count=count+1;update_count=update_count+1;s_type="UPDATE"; s_count=s_count+1;} \
else if (match($0, /insert./)) {printf "\nTimestamp : " $1 " " $2 " " $3 " " $4 " " $(NF);count=count+1;insert_count=insert_count+1;s_type="INSERT"; s_count=s_count+1;} \
else if (match($0, /delete./)) {printf "\nTimestamp : " $1 " " $2 " " $3 " " $4 " " $(NF);count=count+1;delete_count=delete_count+1;s_type="DELETE"; s_count=s_count+1;} \
else if (match($0, /(INSERT INTO .*..*)/)) {count=count+1;insert_count=insert_count+1;s_type="INSERT"; s_count=s_count+1;}  \
else if (match($0, /(UPDATE .*..*)/)) {count=count+1;update_count=update_count+1;s_type="UPDATE"; s_count=s_count+1;} \
else if (match($0, /(DELETE FROM .*..*)/)) {count=count+1;delete_count=delete_count+1;s_type="DELETE"; s_count=s_count+1;}  \
else if (match($0, /(insert into .*..*)/)) {count=count+1;insert_count=insert_count+1;s_type="INSERT"; s_count=s_count+1;}  \
else if (match($0, /(update .*..*)/)) {count=count+1;update_count=update_count+1;s_type="UPDATE"; s_count=s_count+1;} \
else if (match($0, /(delete from .*..*)/)) {count=count+1;delete_count=delete_count+1;s_type="DELETE"; s_count=s_count+1;}  \
else if (match($0, /^(# at) /) && flag==1 && s_count>0) {print "\n\033[31mQuery Type : "s_type " " s_count " row(s) affected\033[0m" ;s_type=""; s_count=0; }  \
else if (match($0, /^(COMMIT)/)) {print "\n\n\033[34mTransaction total : " count "\nInsert(s) : " insert_count " Update(s) : " update_count " Delete(s) : " \
delete_count "\n\033[0m"; \
count=0;insert_count=0;update_count=0; delete_count=0;s_type=""; s_count=0; flag=0} } '
