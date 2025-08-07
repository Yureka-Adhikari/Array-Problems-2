def calculateprofit(arr, arr_size):
    
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
            
    return profit

prices = [690, 390, 725, 700, 390, 600, 280]

profit = calculateprofit(prices, len(prices))
print("Maximum profit is : ", profit)