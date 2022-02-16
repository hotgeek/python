
def smart_truncate(content, length=100):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1])

#print(smart_truncate("To Crop or not to crop", 21))


def carProblem(P, S):
    people = 0
    returnVal = 0

    for i in P:
        people = people + i

    peopleCount = people
    for i in S:   
        returnVal = returnVal + 1     
        seats = i

        remainingSeats = seats - peopleCount

        if(remainingSeats < 0) :
            peopleCount = peopleCount - (-remainingSeats)
            continue
        else:
            return returnVal

#print(carProblem([4,4,2,4], [5,5,2,5]))


def solution(A):
    # write your code in Python 3.6
    totalPollution = 0
    for pollutionAmt in A:
        totalPollution = totalPollution + pollutionAmt

    halfPollution = totalPollution / 2

    A.sort(reverse=True)


    numOfFilters = 0
    index = 0
    sumPollution = 0

    noOfFilters = 0

    for pollution in A:
        sumPollution = sumPollution +  pollution / 2
        index = index + 1
        if(sumPollution <= halfPollution):
            noOfFilters = index
            break
    
    return noOfFilters

    







