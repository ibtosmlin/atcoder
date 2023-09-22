#!/bin/bash
# フォルダのパスを指定
folder_path=~/atcoder/work/
date >> ${folder_path}ZZ_backup.txt
ls ${folder_path}*.py -tlr >> ${folder_path}ZZ_backup.txt
rm ~/atcoder/work/*.py
rm ~/atcoder/work/testlib/* -r -f
