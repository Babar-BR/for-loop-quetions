#Print all even numbers from 1 to 100.
for i in range(2,101,2):
    print(i)
#or you can write like this also
for i in range(1,101):
    if i%2==0:
        print(i)
for i in range(1,101):
    if not (i&1): # if last last value is 0 then even 0001
                    #                                 0010
                    #                                -------
                    #                                 0000
        print(i)

