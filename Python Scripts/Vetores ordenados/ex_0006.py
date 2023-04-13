#Vou tentar escrever um vetor ordenado do zero
import numpy as np

class OrdenedArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lastPosition = -1
        self.values = np.empty(self.capacity, dtype= int)
    
    def add(self, value):
        if self.lastPosition == self.capacity -1:
            print('This array is full')
        else:
            if value > self.values[self.lastPosition]:
                self.values[self.lastPosition+1] = value
                self.lastPosition += 1
                return
            else:
                position = 0
                for i in range(self.lastPosition+1):
                    position = i
                    if self.values[i] > value:
                        break
                x = self.lastPosition
                while x >= position:
                    self.values[x+1] = self.values[x]
                    x -= 1
                self.values[position] = value
                self.lastPosition += 1
    
    def print(self):
        if self.lastPosition == -1:
            print('This array is empty')
        else:
            for x in range(self.lastPosition+1):
                print('[{} : {}] '.format(x, self.values[x]), end='')
            print('')

    def in_bissect(self, value):
        if self.lastPosition == -1:
            return -1
        else:
            higherLimit = self.lastPosition
            bottomLimit = 0

            while True:
                currentPosition = (int((bottomLimit + higherLimit) / 2))
                if self.values[currentPosition] == value:
                    return currentPosition
                elif bottomLimit > higherLimit:
                    return -1
                else:
                    if self.values[currentPosition] < value:
                        bottomLimit = currentPosition + 1
                    else:
                        higherLimit = currentPosition -1
        
    def delete(self, value):
        if self.lastPosition == -1:
            print('This array is empty')
        else:
            position = self.in_bissect(value)
            if position == -1:
                print('This value is not in the array')
            else:
                for position in range(self.lastPosition):
                    self.values[position] = self.values[position + 1]
                self.lastPosition -= 1




if __name__ == '__main__':
    vetor = OrdenedArray(5)
    vetor.add(5)
    vetor.add(300)
    vetor.add(98)
    vetor.add(76)
    vetor.add(2)
    vetor.print()
    vetor.delete(300)
    vetor.add(94)
    vetor.print()