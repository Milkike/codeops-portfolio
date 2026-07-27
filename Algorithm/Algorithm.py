# Question 1
def getOnlyEvens(nums):
    result = []
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 == 0:
            result.append(nums[i])
    print(result)


# tests
getOnlyEvens([1, 2, 3, 6, 4, 8])
getOnlyEvens([0, 1, 2, 3, 4])


# Question 2
def reverseCompare(num):
    original = str(num)
    reverse = original[::-1]

    if int(original) > int(reverse):
        print("Ok")

  else:
         print("Not ok")


    
# Tests
reverseCompare(72)
reverseCompare(23)


# Question 3
def returnFactorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result


# Tests
print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))


# Question 4
def checkMeera(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] * 2 == arr[j]:
                print("I am NOT a Meera array")
                return

    print("I am a Meera array")


# Tests
checkMeera([10, 4, 0, 5])
checkMeera([7, 4, 9])
checkMeera([1, -6, 4, -3])


# Question 5
def isDual(arr):
    count = {}

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for value in count.values():
        if value != 2:
            return 0

    return 1


# Tests
print(isDual([1, 2, 1, 3, 3, 2]))
print(isDual([2, 5, 2, 5, 5]))
print(isDual([3, 1, 1, 2, 2]))


# Question 6
def digitalClock(seconds):
    seconds = seconds % 86400

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


# Tests
print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))