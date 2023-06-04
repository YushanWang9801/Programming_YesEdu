
# '''
# n = int(input("Write an integer: "))
# if n > 0:
#     i, sum = 1, 0
#     while i <= n:
#         sum = sum +i
#         i += 1   # i++ or i = i+1
#     print("The number you enter is positive.")
#     print("The sum from 1 to n is : ", sum)
# elif n < 0:
#     # -1+-2+ -3 ..... + -n
#     i, sum = -1, 0
#     while i >=n:
#         sum = sum +i
#         i -= 1
#     print("The number you enter is negative.")
#     print("The sum from -1 to n is : ", sum)
# else:
#     print("You enter zero")
# '''
# n = int(input("Write an integer: "))
# if n > 0:
#     i, sum = 1, 0
#     for i in range(1, n):
#         sum = sum +i
#         # i += 1   # i++ or i = i+1
#     print("The number you enter is positive.")
#     print("The sum from 1 to n is : ", sum)
# elif n < 0:
#     # -1+-2+ -3 ..... + -n
#     i, sum = -1, 0
#     for i in range(-1, n, -1):
#         sum = sum +i
#         # i -= 1
#     print("The number you enter is negative.")
#     print("The sum from -1 to n is : ", sum)
# else:
#     print("You enter zero")




n = int(input("Write an integer: "))
print("The square of the number you enter is :" , n*n)