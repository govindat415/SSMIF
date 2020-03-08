def sum_ssmif(lst):

    ##initialized an array that will hold the sums of the sublists
    arrayOfSubListSums = []

    ##for loop with index to iterate through the nested list
    for i in range(len(lst)):
        ##checks if the index of the sublist is even
        if i%2 == 0:
            
            subList = lst[i] ##created subList to store the sublist to make it easier to use

            ##declared and initialized indexOfNine and indexOfSix to -1
            ##these two variables will hold the indexes of the nine and six if they exist or they will be -1            
            indexOfNine = -1 
            indexOfSix = -1

            ##declared and initialized sumOfSublist to 0
            sumOfSubList = 0

    
            try:
                ##tries to find the index of the first nine and set indexOfNine equal to the index
                indexOfNine = subList.index(9)
                try:

                    ##index of the first nine is found
                    ##try to find the index of the first six starting at the index of the first nine
                    indexOfSix = subList[indexOfNine:].index(6) + indexOfNine
                    
                except ValueError:
                    ##six is not found so keep indexOfSix as -1
                    indexOfSix = -1
            except ValueError:
                ##six is not found so keep indexOfNine as -1
                indexOfNine = -1                

            ##if indexOfNine and indexOfSix are greater than zero, the values in between will be doubled 
            if(indexOfNine >=0 and indexOfSix >= 0):
                ##iterate through the sublist
                for i in list(range(len(subList))):
                    if indexOfNine <= i <= indexOfSix:
                        ##if the index of the number in the sublist is between the indexOfNine and indexOfSix, add the number*2 to the sum 
                        sumOfSubList = sumOfSubList + subList[i]*2
                    else:
                        ##if the index of the number in the sublist is NOT between the indexOfNine and indexOfSix, add the number to the sum 
                        sumOfSubList = sumOfSubList + subList[i]

            ##if the indexOfNine and indexOfSix are not greater than 0, add the values normally
            else:
                ##iterates through the sublist and adds the numbers to the sum
                for i in list(range(len(subList))):
                        sumOfSubList = sumOfSubList + subList[i]
            ##add the sum of the sub list to th array of sums 
            arrayOfSubListSums.append(sumOfSubList)
        elif i%2 == 1:
            
            subList = lst[i] ##created subList to store the sublist to make it easier to use

            ##declared and initialized indexOfSeven and indexOfFour to -1
            ##these two variables will hold the indexes of the seven and fours if they exist or they will be -1 
            indexOfSeven = -1
            indexOfFour = -1

            ##declared and initialized sumOfSublist to 0
            sumOfSubList = 0
            
            try:
                ##tries to find the index of the first seven and set indexOfSeven equal to the index
                indexOfSeven = subList.index(7)
                try:
                    ##index of the first seven is found
                    ##try to find the index of the first fours starting at the index of the first seven
                    indexOfFour = subList[indexOfSeven:].index(4) + indexOfSeven
                except ValueError:
                    ##four is not found so keep indexOfFour as -1
                    indexOfFour = -1
            except ValueError:
                ##seven is not found so keep indexOfSeven as -1
                indexOfSeven = -1

            
            ##if indexOfSeven and indexOfFour are greater than zero, the values in between will be tripled 
            if(indexOfSeven >=0 and indexOfFour >= 0):
                ##iterate through the sublist
                for i in list(range(len(subList))):
                    if indexOfSeven <= i <= indexOfFour:
                        ##if the index of the number in the sublist is between the indexOfSeven and indexOfFour, add the number*3 to the sum 
                        sumOfSubList = sumOfSubList + subList[i]*3
                    else:
                        ##if the index of the number in the sublist is NOT between the indexOfSeven and indexOfFour, add the number to the sum 
                        sumOfSubList = sumOfSubList + subList[i]
            else:
                ##iterates through the sublist and adds the numbers to the sum
                for i in list(range(len(subList))):
                        sumOfSubList = sumOfSubList + subList[i]

            ##add the sum of the sub list to th array of sums 
            arrayOfSubListSums.append(sumOfSubList)


    ##Once the first for loop finishes, the array of sums will be populated with the sumss
    ##declared and initialized indexOfFour and indexOfFive to -1
    ##these two variables will hold the indexes of the four and five if they exist or they will be -1         
    indexOfFour = -1
    indexOfFive = -1
    
    try:
        ##tries to find the index of the first four and set indexOfFour equal to the index
        indexOfFour = arrayOfSubListSums.index(4)
        try:
            ##index of the first four is found
            ##try to find the index of the first five starting at the index of the first four
            indexOfFive = arrayOfSubListSums[indexOfFour:].index(5) + indexOfFour
        except ValueError:
            ##five is not found so keep indexOfFive as -1
            indexOfFive = -1
    except ValueError:
        ##four is not found so keep indexOfFour as -1
        indexOfFour = -1


    ##if indexOfSeven and indexOfFour are greater than zero, the values in between will be tripled 
    if(indexOfFour >= 0 and indexOfFive >= 0):
        ##iterate through the sublist
        for i in list(range(len(arrayOfSubListSums))):
            ##if the index of the number list of sums is NOT between the indexOfFour and indexOfFive, set the value to 0
            if indexOfFour <= i <= indexOfFive:
                arrayOfSubListSums[i] = 0


    ##return the sum of the arrayOfSubListSums
    return sum(arrayOfSubListSums)  
        
        
            

