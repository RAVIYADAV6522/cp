t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    answer = False

    new_a = 2 * b - c   # check if replacing a works
    if new_a // a > 0 and  new_a % a == 0 :
        answer = True

    if (a + c) % 2 == 0:   # check if replacing b works
        new_b = (a + c) // 2
        if new_b // b > 0 and new_b % b == 0 :
            answer = True

    new_c = 2 * b - a   # check if replacing c works
    if  new_c // c > 0 and  new_c % c == 0 :
        answer = True

    if answer:
        print("YES") 
    else:
        print("NO")
