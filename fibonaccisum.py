first=0

sec=1

total=0

while first+sec<=1000:

    if (first+sec)%2==0:

        total += first+sec

    temp = first+sec

    first = sec

    sec = temp



print(total)