class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = []
        for pos in range(1, n+1):
            if pos%15 == 0 :
                array.append("FizzBuzz")
            elif pos%3 == 0 :
                array.append("Fizz")
            elif pos%5 == 0 :
                array.append("Buzz")
            else:
                array.append(str(pos))
            
        return array