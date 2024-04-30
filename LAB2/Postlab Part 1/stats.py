def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def mode(numbers):
    if not numbers:
        return 0
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
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9, 10]
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Mean:", mean(numbers))

if __name__ == "__main__":
    main()
