t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    continuous_three_empty_cells = False
    total_count_of_empty_cells = 0

    for i in range(n):
        if i + 2 < n and s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
            continuous_three_empty_cells = True
            break
        if s[i] == '.':
            total_count_of_empty_cells += 1

    if continuous_three_empty_cells:
        print(2)
    else:
        print(total_count_of_empty_cells)
