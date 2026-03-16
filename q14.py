#Print a pyramid (centered triangle) of stars with 5 rows.
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars  = "*" * (2 * i - 1)
    print(spaces + stars)
# k=1
# for i in range(6,0,-1):
#     print(" "*i,"*"*k)
#     k+=2