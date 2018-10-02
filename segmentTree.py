
class SegmentTree:

    def __init__(self, inputList):
        self.inputList = inputList
        self.data = [0 for _ in inputList] + inputList
        self.n = len(inputList)
        for i in reversed(range(1, self.n)):
            self.data[i] = max(self.data[2*i], self.data[2*i+1])

    def update(self, index, value):
        index = index + self.n
        self.data[index] = value
        while index>1:
            index = index//2
            self.date[index] = max(self.data[2*index], self.data[2*index+1])

    def computeMax(self, left, right):
        left = left + self.n
        right = right + self.n
        maximum = self.data[left]
        while(left < right):
            if(left%2):
                maximum = max(maximum, self.data[left])
                left+=1
            if(right%2):
                right-=1
                maximum = max(maximum, self.data[right])
            left = left//2
            right = right//2
        return maximum

    def length(self):
        return len(self.inputList)


if __name__ == '__main__':
    count = 0
    list0 = [1,1,2,4,3,5,6,9,8]
    list1 = SegmentTree(list0)
    list1.computeMax(0,3) #2
    list1.computeMax(3,9) #9
    list1.update(3, 7)
    list1.computeMax(0,5) #7
