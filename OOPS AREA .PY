# OOPS:
class Circle:
    def _init_(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

r = float(input("Radius: "))
print("Area =", Circle(r).area())
