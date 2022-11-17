# Allir hringir sem að við tveir spiluðum í móti sumarið 2022
Hakon = [79, 80, 75, 80, 72, 76, 80, 81, 71, 78, 80, 76, 74, 76, 77, 77]
Atli  = [82, 73, 90, 81, 79, 84, 76, 78, 91, 77, 79, 77, 79, 80]
def medal(arr):
    temp = 0
    for i in range (len(arr)):
        temp += arr[i]
    return temp/len(arr)
print("Meðal skor hjá Hákoni: ", medal(Hakon))
print("Meðal skor hjá Atla: %.1f" % medal(Atli))

## Meðal skor hjá Hákoni:  77.0
## Meðal skor hjá Atla:    80.4

# kenning afsönnuð.