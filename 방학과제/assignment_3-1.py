# Write your code here :-)
dollarToWon = 1272.1
dollarToEuro = 0.94

print("------------------------------")
print("  달러($)   원화(원)   유로(€)  ")
print("------------------------------")
for dollar in range(1, 11):
    print("  %3d      %6d     %.1f  " %(dollar * 10, int(dollar * 10 * dollarToWon), dollar * 10 * dollarToEuro))
print("------------------------------")
