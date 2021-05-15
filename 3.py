
def CheckAandB(A,B)
    if A == B :
        print ("A contains all the elements of B")
    for item in range(0,len(A)):
        if A.index(item) == 1 and B.index == 1:

            print("A,B đều chứa các giá trị duy nhất")
        elif A.index(item) == 1 :

            print( " Chỉ có A chứa các giá trị duy nhất")
        elif B.index(item) == 1:
            print ("Chỉ có B chứa các giá trị duy nhất")   
        else:
            print("Không có tuple nào chứa các giá trị duy nhất")

