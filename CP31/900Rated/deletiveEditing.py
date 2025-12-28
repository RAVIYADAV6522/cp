t = int(input())
for _ in range(t):
    s = input().strip()
    t_str = input().strip()

    n, m = len(s), len(t_str)

    # frequency count for string t
    frequency_in_t = [0] * 26
    for ch in t_str:
        frequency_in_t[ord(ch) - ord('A')] += 1

    # traverse s from back and keep only required chars
    s_list = list(s)
    for i in range(n - 1, -1, -1):
        idx = ord(s_list[i]) - ord('A')
        if frequency_in_t[idx] > 0:
            frequency_in_t[idx] -= 1
        else:
            s_list[i] = '.'

    # construct final string without '.'
    final_string = "".join(ch for ch in s_list if ch != '.')

    if final_string == t_str:
        print("YES")
    else:
        print("NO")
