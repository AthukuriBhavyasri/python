n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
text = input("Enter a word or phrase: ").replace(" ", "").lower()
if text == text[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
