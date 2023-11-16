# Precedência dos operadores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta1 = 1 + 1 ** 5 + 5     # 7
print(conta1)

conta2 = (1 + 1) ** (5 + 5) # 1024
print(conta2)