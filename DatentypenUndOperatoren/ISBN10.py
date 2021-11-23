ISBN = 859373911

z1 = ISBN //10000000000 % 10
z2 = ISBN //1000000000 % 10
z3 = ISBN //100000000 % 10
z4 = ISBN //10000000 % 10
z5 = ISBN //1000000 % 10
z6 = ISBN //10000 % 10
z7 = ISBN //1000 % 10
z8 = ISBN // 100 % 10
z9 = ISBN // 10 % 10
z10 = ISBN // 1 % 10

summe = 1 * z1 + 2 * z10 + 3 * z3 + 4 * z4 + 5 * z5 + 6 * z6 + 7 * z7 + 8 * z8 + 9 * z9
Rest = summe % 11
print("Rest ist", Rest)
