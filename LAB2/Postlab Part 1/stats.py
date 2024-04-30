def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def mode(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_frequency = max(frequency.values())
    mode_list = [key for key, value in frequency.items() if value == max_frequency]
    return mode_list[0]

def mean(numbers):
    return sum(numbers) / len(numbers)
