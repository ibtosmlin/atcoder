def i():return input()
n=i();r=0
for a in i().split():r=max(r+int(a),0)
print(r)