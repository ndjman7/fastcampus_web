def longestSequence(A):

    def sequnce(A,start):
        min = 1
        result = [A[start]]
        for i in range(1, len(A)-start):
            if(min<len(result)):
                min = len(result)
            result = [A[start]]
            d=A[start]
            value = A[i]-A[start]
            for j in range(i,len(A)-start):
                if A[j]-d ==value:
                    result.append(A[j])
                    d = A[j]
        return min

    def check(A):
        min = 1
        for i in range(len(A)):
            result = sequnce(A, i)
            if(min<result):
                min=result
        return min
    print(check(A))

longestSequence([1,3,7,5])

