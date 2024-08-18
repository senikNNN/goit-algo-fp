def greedy_algorithm(items, budget):
    # Сортування страв за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_calories = 0
    total_cost = 0
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            total_cost += details['cost']
    
    return selected_items, total_calories, total_cost

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Обрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")
print(f"Загальна вартість: {total_cost}")

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    total_cost = budget - w
    
    return selected_items, total_calories, total_cost

# Приклад використання
selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
print(f"\nАлгоритм динамічного програмування:")
print(f"Обрані страви: {selected_items_dp}")
print(f"Загальна калорійність: {total_calories_dp}")
print(f"Загальна вартість: {total_cost_dp}")
