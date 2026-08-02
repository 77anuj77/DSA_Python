'''
choose fordt three then 
arr= [1,2,3,4,5]
left total
right total
current_total=current_total-left_total+right_total
return '''
def best_chocolates(prices, window_size):

    current_total = sum(prices[0:window_size])
    best_total = current_total

    print(f"Window : {prices[0:window_size]} = {current_total}")

    for i in range(window_size, len(prices)):

        left_total = prices[i - window_size]
        right_total = prices[i]

        current_total = current_total - left_total + right_total

        window = prices[i - window_size + 1 : i + 1]
        print(f"Window: {window} = {current_total}")

        if current_total > best_total:
            best_total = current_total

    return best_total


prices = [2, 3, 4, 3, 4, 7, 9]
answer = best_chocolates(prices, 3)
print("Best total:", answer)