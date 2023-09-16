a = int(input())
lex = ['I', 'J', 'K', 'L', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(lex[a % 12], (a + 6) % 10, sep = "")