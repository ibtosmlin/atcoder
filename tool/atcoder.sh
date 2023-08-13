#!/bin/bash

# working directory

url=${1}
arg=${2}
taskid=${url##*/}

cp=~/atcoder
ctool="${cp}/tool"
ctemplate="${ctool}/template.py"

cwd="${cp}/work"
cfname="${cwd}/${taskid}.py"
ctest="${cwd}/testlib"
ctaskwd="${ctest}/${taskid}"
ctaskfname="${ctest}/${taskid}/main.py"

cd ${cwd}

# argument 1
# example: https://atcoder.jp/contests/abc235/tasks/abc235_a
# argument 2
# example: 'd' or 't'


# echo $url
# echo $arg
# echo $taskid      -> abc235_a
# echo $filename    -> abc235_a.py

if [ $arg = 'd' ]; then
# download
#    x-www-browser $url
    echo "Downloading................"
    mkdir -p $ctaskwd
    cd $ctaskwd
    oj d $url
    cd $cp
    cp $ctemplate $cfname
    sed -i "1i # $url" $cfname
    code $cfname
    echo "${ctemplate} created in ${cfname}"


elif [ $arg = 't' ]; then
# test
    echo "Testing....................."
    cp $cfname $ctaskfname
    cd $ctaskwd
    # oj t -c 'python3 main.py' -S
    oj t -c 'pypy3 main.py' -S
    cd $cp


elif [ $arg = 'ss' ]; then
# submit
    echo "Submitting by Python3......."
    cp $cfname $ctaskfname
    cd $ctaskwd
    # echo y | oj s main.py
    oj s --language 5055 --no-guess main.py --yes
    cd $cp


elif [ $arg = 's' ]; then
# submit
    echo "Submitting by Pypy3........."
    fm="$cwd/$filename"
    to="$cp/$taskid/main.py"
    cp $cfname $ctaskfname
    cd $ctaskwd
    # echo y | oj s --guess-python-interpreter pypy main.py
    oj s --language 5078 --no-guess main.py --yes
    cd $cp


else
    echo '???'
fi
