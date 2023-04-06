# https://atcoder.jp/contests/abc296/tasks/abc296_b
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == '*':
            print(alp(j)+ str(8-i))
            exit()
