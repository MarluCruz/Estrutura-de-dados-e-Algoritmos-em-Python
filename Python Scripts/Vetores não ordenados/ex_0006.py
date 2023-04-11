# Vou tentar escrever um vetor do zero
import numpy as np

class Array:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.lastPosition = -1
        self.values = np.empty(self.capacity, dtype= int)
    
    def add(self, value):
        if self.lastPosition == self.capacity -1:
            print("The array is full!")
        else:
            self.lastPosition += +1
            self.values[self.lastPosition] = value
    
    def print(self):
        if self.lastPosition == -1:
            print('The array is empty!') 
        else:
            for x in range(self.lastPosition +1):
                print('[{} : {}] '.format(x, self.values[x]), end='')
            print('')
    
    def __str__(self):
        if self.lastPosition == -1:
            return 'The array is empty!'
        else:
            model = '[{} : {}] '
            arrayString = str()
            for x in range(self.lastPosition +1):
                arrayString += model.format(x, self.values[x])
            return arrayString
        
    def search(self, value):
        if self.lastPosition == -1:
            print('The array is empty!')
        else:
            for i in range(self.lastPosition + 1):
                if value == self.values[i]:
                    return i
            return -1
    
    def delete(self, value):
        if self.lastPosition == -1:
            print("The array is empty")
        else:
            position = self.search(value)
            if position == -1:
                print("This value is not in the array!")
            else:
                for i in range(position, self.lastPosition):
                    self.values[i] = self.values[i + 1]
                self.lastPosition -= 1
                
            #else:
                            

if __name__ == '__main__':
    array = Array(5)
    array.add(33)
    array.add(69)
    array.add(24)
    array.add(4)
    array.print()
    array.delete(69)
    print(array)
