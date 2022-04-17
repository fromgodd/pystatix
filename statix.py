
def mean(array):
    try:
        sum = 0
        for v in array:
            sum += v
            pass
        return sum/len(array)
    except TypeError:
        print("Cannot calculate mean! Check if it has no string values")
    except:
        print("Error")

def median(array):
    try:
        sortedArray = sorted(array)
        lengthArray = len(array)
        index = (lengthArray - 1) // 2
        
        if (lengthArray % 2):
            return sortedArray[index]
        else:
            return (sortedArray[index] + sortedArray[index + 1])/2.0
    

    except:
        print("Error")

def lower_quartile(array):
    array.sort()
    arr_length = len(array)
    lq = (arr_length+1)/4
    lq_cnt = []
    lq_cnt.append(lq)
    return lq

a = [7,13,13,15,20,24,27]
print(lower_quartile(a))