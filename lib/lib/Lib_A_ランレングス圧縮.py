#name#
# ランレングス圧縮
#description#
# ランレングス圧縮
#body#
#####################################
from itertools import groupby
strings = "aabbbbbbbbbbbba"

ans = [(k, len(list(g))) for k,g in groupby(strings)]
print(ans)
#[('a', 2), ('b', 12), ('a', 1)]
#prefix#
# Lib_A_ランレングス圧縮_rle
#end#
