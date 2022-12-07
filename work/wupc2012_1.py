ma, da = map(int, input().split())
mb, db = map(int, input().split())
R = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
RR = [0]
for ri in R:
    RR.append(RR[-1] + ri)

mda = RR[ma] + da
mdb = RR[mb] + db
print(mdb-mda)
