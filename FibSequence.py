def FibSequence(n):

    """
    This function intakes the nth term in the fibonachi sequence

    FibSequence will calculate each term in the sequence and dynamically store the results in a list

    Since the first two terms of the sequence are considered by default n should never be less than 3. Instead of n being the amount of terms after the initial
    two that I want to calculate Id rather have it be more acurate to where the term actually is in the sequence. So the number n should represent exactly where
    that term is in the sequence not where it is after 0 and 1

    I will use a dynamic algorithm that remembers each step of the sequence to save running time

    FIBONACHI SEQUENCE: 
    1. each term is the sum of the two previous terms
    2. the initial condition is that 0 and 1 are in the sequence at default meaning we start from the third term in the sequence
    """
    
    if(n < 3):
        print("The number you have entered is less than 3! Try again")
        return

    Sequence = [0, 1]
    x , y = 0, 1
    # x and y will hold the index of the two terms being added
    


    for i in range(n - 2):
        Sequence.append( Sequence[x] + Sequence[y])
        x += 1
        y += 1
        
    

    for i in range(n):
        print(Sequence[i])
    







def main():
    print("In the Fibonachi sequence each term is the sum of the previous two terms")
    print("The intial two terms in the sequence 0 and 1 are default")
    print("While selecting how many terms you generate please select a number greater than or equal to 3 to compensate for the first two terms")
    UserTerm = input("How many terms of the Fibonachi sequence would you like to calculate?: ")
    try:
        UserTerm = int(UserTerm)
        FibSequence(UserTerm)
    except ValueError:
        #triggers if value cannot be converterd to an integer
        print("Invalid input")


        
    

main()