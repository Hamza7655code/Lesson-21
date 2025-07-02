start = int(input("Start: "))
end = int(input("End: "))

even_squares = [n*n for n in range(start, end+1) if (n*n) % 2 == 0]
odd_squares  = [n*n for n in range(start, end+1) if (n*n) % 2 != 0]

print("Even squares:", even_squares)
print("Odd  squares:", odd_squares)