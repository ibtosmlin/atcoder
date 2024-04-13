#!/bin/bash

# working directory

url=${1}
arg=${2}
taskid=${url##*/}

cp="`pwd`"
ctool="${cp}/tool"
cwd="${cp}/.work"

ctemplate="${ctool}/template.ts"
cfname="${cwd}/${taskid}.ts"
ctest="${cwd}/testlib"
ctaskwd="${ctest}/${taskid}"
ctaskfname="${ctest}/${taskid}/main.ts"
ctaskwdtest="${ctest}/${taskid}/test"

msg1="Downloading................"
msg2="Testing...................."
msg3="Submitting by TypeScript..."
msg4="SkipDownload..............."

function set_template(){            #
    if [ ! -f $2 ]; then
        cp $1 $2                    # テンプレのコピー
        sed -i "1i // $url" $2       # テンプレの一行目に問題urlを設定
        echo "${1} created in ${2}"
    else
        echo "${2} already exists."
    fi
    code $2                         # VSコードで表示
}

function download_testcase(){
    if [ ! -d $ctaskwdtest ]; then
        echo $msg1
        mkdir -p $ctaskwd
        cd $ctaskwd
        oj d $url
        cd $cp
    else
        echo $msg4
    fi
}


if [ $arg = 'd' ]; then
# download test data and set template
#    x-www-browser $url
    download_testcase
    set_template $ctemplate $cfname


elif [ $arg = 'template' ]; then
# set template
    set_template $ctemplate $cfname

elif [ $arg = 't' ]; then
# download test data and test
    download_testcase
# test
    echo $msg2
    cp $cfname $ctaskfname
    cd $ctaskwd
    tsc main.ts
    oj t -c 'node main.js' -D
    cd $cp


elif [ $arg = 's' ]; then
# submit
    echo $msg3
    cp $cfname $ctaskfname
    cd $ctaskwd
    oj s --language 5058 --no-guess main.ts --yes --open
    cd $cp


else
    echo '???'
fi
