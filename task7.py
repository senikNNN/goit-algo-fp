import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Підрахунок кількості випадінь кожної можливої суми
    sums_count = {sum_value: 0 for sum_value in range(2, 13)}
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1
    
    # Обчислення ймовірностей
    probabilities = {sum_value: count / num_rolls for sum_value, count in sums_count.items()}
    
    return sums_count, probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color='skyblue')
    plt.xticks(sums)
    plt.xlabel('Сума на двох кубиках')
    plt.ylabel('Імовірність')
    plt.title('Ймовірності сум на двох кубиках (Симуляція)')
    plt.show()

# Аналітичні значення ймовірностей
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

def compare_probabilities(simulated_probs, analytical_probs):
    print("Сума  | Симульована ймовірність | Аналітична ймовірність | Різниця")
    print("-----------------------------------------------------------")
    for sum_value in range(2, 13):
        sim_prob = simulated_probs[sum_value]
        ana_prob = analytical_probs[sum_value]
        difference = abs(sim_prob - ana_prob)
        print(f"{sum_value:4}  | {sim_prob:.4%}         | {ana_prob:.4%}        | {difference:.4%}")

# Виконання симуляції
num_rolls = 100000  # Наприклад, 100 тисяч кидків
sums_count, simulated_probabilities = simulate_dice_rolls(num_rolls)

# Порівняння результатів
compare_probabilities(simulated_probabilities, analytical_probabilities)

# Побудова графіка ймовірностей
plot_probabilities(simulated_probabilities)
