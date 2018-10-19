# node class
class Node(object):
    password = ""
    count = -1
    next = None
    # Set up Password, count and next variables
    def __init__(self, password, count, next):
        self.password = password 
        self.count = count 
        self.next = next
# Create LL using hold array of passwords
def createLinkedList(hold):
    # Assert to avoid issues
    assert  len(hold) > 0
    #Base Case
    if len(hold) == 1:
        return Node(hold[0], +1, None)
    #Recursively Create List
    else:
        return Node(hold[0], +1, createLinkedList(hold[1:]))
# Remove duplicates from list
def removeDups(node):
    # Create two pointers 
    curr = sec = node
    while curr is not None:
        while sec.next is not None:
            # Compare pointer values delete dup and add to count
            if sec.next.password == curr.password:
                sec.next = sec.next.next
                curr.count += 1
            # Values are not the same
            else:
                sec = sec.next
        #Iterate over list
        curr = sec = curr.next
# use length of list for bubbleSort
def length(node):
    i = 0 
    if node is None:
        return i
    else:
        i += 1
        return i + length(node.next)
#Bubble sort (doesn't want to work for whatever reason)
def bubbleSort(node):
    num = length(node)
    if (num > 1):
        for i in range(num):
            curr = node
            sec = node.next
            for j in range(0, num-1):
                if curr.count < sec.count:
                    temp = curr
                    curr = sec
                    sec = temp
                curr = sec
                sec = sec.next
        return(sec)
# Get middle of list for merge sort
def getMid(node):
    if node is None:
        return node
    curr = node
    sec = node.next
    while sec is not None:
        sec = sec.next
        if sec is not None:
            curr = curr.next
            sec = sec.next
    return curr
# merge left and right from merge sort
def mergeMergeSort(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.count >= right.count:
        sort = left
        sort.next = mergeMergeSort(left.next, right)
    else:
        sort = right
        sort.next = mergeMergeSort(left, right.next)
    return sort
#Merge Sort
def mergeSort(node):
    if node is None or node.next is None:
        return node
    mid = getMid(node)
    midPlusOne = mid.next
    mid.next = None
    left = mergeSort(node)
    right = mergeSort(midPlusOne)
    sortedList = mergeMergeSort(left, right)
    return sortedList

#Open file
with open("test2.txt", "r") as ourFile:
    # Create array to store passwords after split
    hold = []
    # Go through each line of the file
    for line in ourFile:
        # split users and passwords
       passwords = line.split()
       # Store passwords
       hold.append(passwords[1])
# Create LL
node = createLinkedList(hold)
# Remove the duplicates
removeDups(node)
# node = bubbleSort(node)
tester1 = node
#for i in range(20):
    #print(tester1.password)
    #tester1 = tester1.next
node = mergeSort(node)
print("")
tester = node
#print 20 most used passwords 
for i in range(20):
    print(tester.password)
    tester = tester.next 
# Implement Dictionary 
dict = {}

for item in hold:
    if item in dict:
        dict[item] = dict[item] + 1
    else:
        dict[item] = 1   
