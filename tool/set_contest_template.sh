#設定ファイルから変数を取得
cp="`pwd`"
source ${cp}/tool/contest_id.txt

for task_id in {e..a}
do
    at ${con_root}/${con_id}/tasks/${con_id}_${task_id} template
done
