#設定ファイルから変数を取得
cp="`pwd`"
source ${cp}/tool/contest_id.txt

for task_id in {a..e}
do
    echo "${con_root}/${con_id}/tasks/${con_id}_${task_id} ${job_id} testing..."
    at ${con_root}/${con_id}/tasks/${con_id}_${task_id} ${job_id} t
done
