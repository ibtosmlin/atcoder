#!/bin/bash
# フォルダのパスを指定
cp="`pwd`"
folder_path=${cp}/.work/
date >> ${folder_path}ZZ_backup.txt
ls ${folder_path}*.py -tlr >> ${folder_path}ZZ_backup.txt
rm ${folder_path}/*.py
rm ${folder_path}/testlib/* -r -f
