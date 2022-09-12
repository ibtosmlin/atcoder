# DPライブラリー

配るDPよりは貰うDPの方が最適化されている

## EDPC

lib/lib/DP/dp_a.py
1. [A - Frog1](lib/lib/DP/dp_a.py)
    - 配るDP/貰うDP
/home/ibtosm/atcoder/lib/lib/DP/dp_i.py
1. [B - Frog2](./DP/dp_b.py)
    - 配るDP/貰うDP + 累積

1. [C - Vacation](./DP/dp_c.py)
    - 過去の履歴を捨てて、直近の情報のみ管理する

1. [D - Knapsack1](./DP/dp_d.py)
    - 重さ小さい + 値大きい
    - 重さを属性にして欲しい情報を管理する

1. [E - Knapsack2](./DP/dp_e.py)
    - 重さ大きい + 値小さい
    - 値を属性にして達成する条件を管理する
    - 最後に欲しい情報を集約する

1. [F - LCS](./DP/dp_f.py)
    - Longest Common Subsequence

1. [G - Longest Path](./DP/dp_g.py)
    - 木の上でDAGを構成する -> トポロジカルソート

1. [H - Grid1](./DP/dp_h.py)
1. [H - Grid1 (再帰版)](./DP/dp_h_rec.py)
    - 二次元グリッドでのdp
    - 上から順に記録していくパターン

1. [I - Coins](./DP/dp_i.py)
    - 確率計算

1. [J - Sushi](./DP/dp_j.py)
    - 期待値計算
    - 状態から遷移させる
    - 遷移は条件付き期待値となる

1. [K - Stones](./DP/dp_k.py)
    - 後退解析
    - Gameで手詰まりから戻る
    - 逆辺を張る感じ

1. [L - Deque](./DP/dp_l.py)
    - 区間DP
    - 区間が小さいものから記録していく

1. [M - Candies](./DP/dp_m.py)
    - 三重ループにおいて、累積和を使って計算量を抑える

1. [N - Slimes](./DP/dp_n.py)
    - 区間DP
    - 累積和を使って計算量を抑える

1. [O - Matching](./DP/dp_o.py)
    - bitDP
    - sに関係のあるiのみ見ているので、貰うdpだと遷移が少なくできる


1. [P Independent Set](./DP/dp_p.py)
1. [P Independent Set (再帰版)](./DP/dp_p_rec.py)
    - 木DP
    - 部分木に関する情報を集めて元の木に情報を集約
    - 葉からの帰りがけの処理

1. [Q - Flowers](./DP/dp_q.py)
    - 二重ループにおいて、セグメント木を使って計算量を圧縮

1. [R - Walk](./DP/dp_r.py)
    - 同じ状態遷移をｋ回（かなり大きい）も繰り返す
    - 木で隣接行列AでA^kを繰り返し二乗法で計算する

1. [S - Digit Sum](./DP/dp_s.py)
    - 桁DP

1. [T - Permutation](./DP/dp_t.py)
    - 配列の数え上げ
    - 直前の値とその残りとの関係をキーにする

1. [U - Grouping](./DP/dp_u.py)
    - bitDP
    - sごとにその部分集合を探索する

1. [V - Subtree](./DP/dp_v.py)
    - 全方位木DP

1. [W - Intervals](./DP/dp_w.py)
    - ??????????????

1. [X - Tower](./DP/dp_x.py)
    - ナップサック
    - 最適な順番があり、その順番を固定できる場合
    - 順番を見つけるのが難しい

1. [Y - Grid2](./DP/dp_y.py)
    - 二次元グリッドでのdp
    - 記録範囲が大きく、行ってはいけないマスが少ない
    - 行けないところを控除する方法
    - 初めて到達する場合からの場合分け
    - 行ってはいけないマスをソートする

1. [Z - Frog3](./DP/dp_z.py)
    - Convex Hull Trickを使ってdpの計算量を減らす
