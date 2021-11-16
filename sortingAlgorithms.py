def InsertionSort():
    #Given list for python
    unsortedNumbers = [1, 30, 23, 4, 6, 8]

    #variable declaration
    length = len(unsortedNumbers) #amount of items in list

    #Passing through the array
    for i in range(1, length):
        currentValue = unsortedNumbers[i]
        currentPosition = i

        #Assigning values
        while currentPosition > 0 and unsortedNumbers[currentPosition - 1] > currentValue:
            unsortedNumbers[currentPosition] = unsortedNumbers[currentPosition - 1]
            currentPosition = currentPosition - 1

        unsortedNumbers[currentPosition] = currentValue

    print("\n------")
    print("Sorting Successful")
    print(unsortedNumbers)

def bubbleSort():
    #Given list for sorting
    unsortedNumbers = [1, 30, 23, 4, 6, 8]

    #variable declaration
    length = len(unsortedNumbers) #amount of items in the list 
    currentIndex = 1
    currentPassthrough = 0
    tempNumber = 0 #variable created to temporarily hold item that will be swapped

    #Makes the nested while run until each item is sorted in the list
    while currentPassthrough < length:

        #Passing through the list once to get the highest unsorted number to the rightmost
        while currentIndex < length:
        
            if unsortedNumbers[currentIndex - 1] > unsortedNumbers[currentIndex]:
                tempNumber = unsortedNumbers[currentIndex - 1]
                unsortedNumbers[currentIndex - 1] = unsortedNumbers[currentIndex]
                unsortedNumbers[currentIndex] = tempNumber
            
                print(unsortedNumbers)
            currentIndex += 1

        currentIndex = 1
        currentPassthrough += 1
    
    print("\n\nList has been sorted")
    print(unsortedNumbers)
    print("\n\n")

def SelectionSort():
    #Given list for sorting
    unsortedNumbers = [12, 32, 34, 21, 56, 76]

    #amount of items in the list
    length = len(unsortedNumbers)

    #Go through the array
    for i in range(length):
        min = i
        #go through the unsorted portion of the array
        for j in range(i + 1, length):
            #Find the smallest number
            if unsortedNumbers[i] > unsortedNumbers[j]:
                i = j
        #swap numbers
        unsortedNumbers[i], unsortedNumbers[min] = unsortedNumbers[min], unsortedNumbers[i]
        print(unsortedNumbers)
            
    #Print sorted number list
    print("\n---------------------")
    print(unsortedNumbers)
    print("\n\n")



def SortingMethods():
    flag = True
    while flag == True:
        #Ask for choice the first time
        choice = int(input("1. Bubble Sort \n2. Selection Sort\n3. Insertion Sort\nPlease chose your sorting method: "))
        #Checks if choice is 1,2 or 3, if its not it reruns until valid number is given
        if choice < 1 or choice > 3:
            while choice < 1 or choice > 3:
                print("----------------------------------------------")
                print("Valid values are only 1,2 or 3, please try again")
                choice = int(input("1. Bubble Sort \n2. Selection Sort\n3. Insertion Sort\nPlease chose your sorting method: "))
        #Choice #1 Bubble Sort
        if choice == 1:
            bubbleSort()
        #Choice #2 = Selection Sort
        elif choice == 2:
                SelectionSort()
        elif choice == 3:
            InsertionSort()
        
        redo = int(input("Do you want to see another sorting method? 1/2: "))
        
        if redo < 1 or redo > 2:
            while redo < 1 or redo > 2:
                print("-----------------------")
                print("Valid values are only 1 or 2")
                redo = int(input("Do you want to see another sorting method? 1/2: "))
        if redo == 1:
            flag = True
        elif redo == 2:
            flag = False

SortingMethods()
    
