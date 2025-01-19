class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Stack to store indices of temperatures
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                sindex = stack.pop()  # Pop the index of the cooler temperature
                result[sindex] = i - sindex  # Calculate the difference in days until a warmer temperature
            stack.append(i)  # Add the current day to the stack
        
        return result