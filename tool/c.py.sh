#!/bin/bash

#設定ファイルから変数を取得
source ~/atcoder/tool/contest_id.txt

NAME=$BASH_SOURCE[0]
NAME=${NAME%.*}
NAME=${NAME%.*}
NAME=${NAME##*/}

# argment d or s or t
job_id=${1}


at ${con_root}/${con_id}/tasks/${con_id}_${NAME} ${job_id}
#echo ${con_root}/${con_id}/tasks/${con_id}_${NAME} ${job_id}
