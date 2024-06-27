class B:
    def __init__(self):
        self.rr = 1
        nonlocal u
        print(u)


class A:
    u = 3
    def __init__(self):
        self.v = 5
    cb = B()


ca = A()
print(ca.u, ca.v)
print(ca.cb.rr)