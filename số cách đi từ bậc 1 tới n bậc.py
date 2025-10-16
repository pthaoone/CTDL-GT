n = int(input("Nhập số bậc thang n: "))
if n <= 0:
    print("Số bậc phải lớn hơn 0")
elif n == 1:
    print("Có 1 cách để leo 1 bậc thang.")
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    #số cách leo cho từng bậc
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(f"Có {dp[n]} cách để leo lên bậc {n}.")
