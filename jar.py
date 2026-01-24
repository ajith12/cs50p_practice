class Jar:
    def __init__(self, capacity, size=0):
        self.size = size
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity<0:
            raise ValueError("Capacity cannot be less than 0")
        self._capacity = capacity

    def deposit(self):
        n = int(input("Number of cookies to deposit: "))
        if (n+self.size)>self.capacity:
            raise ValueError("Exceeds capacity")
        self.size = self.size+n

    def withdraw(self):
        n = int(input("Number of cookies to withdraw: "))
        if (self.size-n)<0:
            raise ValueError("Exceeds number of cookies in jar")
        self.size = self.size-n

    def __str__(self):
        return self.size*f"🍪"
    
def main():
    jar = Jar(10)
    jar.deposit()
    jar.withdraw()
    print(jar)

if __name__ =="__main__":
    main()