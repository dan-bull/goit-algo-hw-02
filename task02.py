from collections import deque

def check_for_palindrome(line):
    line = line.lower().replace(" ", "")

    d = deque(line)

    while len(d) > 1:
        first = d.popleft()
        last = d.pop()

        if first != last:
            return False
    
    return True

# Перевірка
test_words = check_for_palindrome(input("Enter the word to test for palindrome: "))
print(test_words)