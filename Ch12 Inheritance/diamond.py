class A:
    def ping(self):
        print('A pings:', self)

class B(A):
    def pong(self):
        print('B pongs:', self)

class C(A):
    def pong(self):
        print('C PONGS:', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('After ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

d = D()
d.pong()
C.pong(d)

print(D.__mro__)
d.ping()
print('-'*50)
d.pingpong()
