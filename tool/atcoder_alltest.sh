#!/bin/bash

#設定ファイルから変数を取得
source ~/atcoder/tool/contest_id.txt

NAME=$BASH_SOURCE[0]

at ${con_root}/${con_id}/tasks/${con_id}_a ${job_id} t
at ${con_root}/${con_id}/tasks/${con_id}_b ${job_id} t
at ${con_root}/${con_id}/tasks/${con_id}_c ${job_id} t
at ${con_root}/${con_id}/tasks/${con_id}_d ${job_id} t
