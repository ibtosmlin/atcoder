source ~/atcoder/tool/contest_id.txt

for task_id in {g..a}
do
    at ${con_root}/${con_id}/tasks/${con_id}_${task_id} template
done
