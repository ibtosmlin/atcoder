#!/bin/bash

#設定ファイルから変数を取得
cp="`pwd`"
source ${cp}/tool/contest_id.txt

# argment d or s or t
job_id=${2}
task_id=${1}

at ${con_root}/${con_id}/tasks/${con_id}_${task_id} ${job_id}
