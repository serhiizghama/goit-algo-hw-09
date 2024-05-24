import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount, coins=COINS):
    coin_count = {}
    for coin in coins:
        count, amount = divmod(amount, coin)
        if count > 0:
            coin_count[coin] = count
    return coin_count


def find_min_coins(amount, coins=COINS):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    coin_count = {}
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and dp[amount] == dp[amount - coin] + 1:
                amount -= coin
                if coin in coin_count:
                    coin_count[coin] += 1
                else:
                    coin_count[coin] = 1
                break
    return coin_count


# Вимірювання часу виконання
greedy_time = timeit.timeit(
    'find_coins_greedy(1000)', globals=globals(), number=100)
dp_time = timeit.timeit('find_min_coins(1000)', globals=globals(), number=100)

print(f"Час виконання жадібного алгоритму: {greedy_time} секунд")
print(f"Час виконання алгоритму динамічного програмування: {dp_time} секунд")