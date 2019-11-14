import random as rand;

while True:
    sectionInput = input("Enter section header or Q\q to quit: ")
    if sectionInput == 'q' or sectionInput == 'Q':
          quit()
    else:
        evenOrOdd, start, end, numProbs = input("Enter wether you want (e)ven or (o)dd or (b)oth types of problems, start of range, end of range, and amount you want to do, commas in between all inputs: ").strip(" ").split(",")
    
        start1 = int(start) #int start of range
        end1 = int(end) #int end of range
        numProbs1 = int(numProbs) #number of problems
        
        print(sectionInput)
        

        if evenOrOdd == 'e' or evenOrOdd == 'E' or evenOrOdd == 'even' or evenOrOdd == 'Even':
            for i in range(start1, end1 + 1): 
                if i % 2 == 0: #if i is divisible by 2,
                    pass
            print(sorted(rand.sample(range(start1,end1), numProbs1)), end=" ")
            print()
        elif evenOrOdd == 'o' or evenOrOdd == 'O' or evenOrOdd == 'odd' or evenOrOdd == 'Odd':
            for i in range(start1, end1 + 1):
                if i % 2 != 0: #if i is not divisible by 2,
                    pass
            print(sorted(rand.sample(range(start1,end1), numProbs1)), end=" ")
            print()
        elif evenOrOdd == 'b' or evenOrOdd == 'B' or evenOrOdd == 'both' or evenOrOdd == 'Both':
            for i in range(start1, end1 + 1):
                pass
            print(sorted(rand.sample(range(start1,end1), numProbs1)), end=" ")
            print()
