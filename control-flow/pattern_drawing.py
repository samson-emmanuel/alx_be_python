size = int(input("Enter the size of the pattern: "))
rows = 0
while rows < size:
    columns = 0
    while columns < size:
        print("*", end=" ")
        columns += 1
    print()
    rows += 1