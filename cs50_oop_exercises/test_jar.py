
import emoji


#Can add your own methods
class Jar:
    def __init__(self, capacity=12):
    #raise valueerror for capacity if not non-negative
        if capacity<0:
            raise ValueError("Capacity is negative")
        self._capacity=capacity
        self.size=0
        
    def __str__(self) -> str:
    #n cookie emojis to tell you number of cookies in the cookie jar  
        return f"the capacity is {self.capacity} and the number of cookies in the jar is "+emoji.emojize(":cookie:")*self.size

    def deposit(self,n):
    #add n cookies to cookie jar, if adding n goes over capacity then raise Valueerror
        if self.size+n>self.capacity:
            raise ValueError("Above capacity")
        self.size = self.size+n

    def withdraw(self,n):
    #remove n cookies from cookie jar. If n is more than number of cookies in cookie jar then raise valueerror
        if n>self.size:
            raise ValueError("Above number of cookies")
        self.size = self.size-n

    @property
    def capacity(self):
    #should return the cookie jar's capacity
        return self._capacity
    
    @property
    def size(self):
    #should return the number of cookies actually in the cookie jar, initially 0
        return self._size

    @size.setter
    def size(self,size):
        self._size = size


def main():
    jar = Jar(6)
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(1)
    print(jar)
    jar.withdraw(4)
    print(jar)


if __name__== "__main__":
    main()