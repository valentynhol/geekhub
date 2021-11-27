"""
4. Написати функцію < prime_list >, 
яка прийматиме 2 аргументи - початок і кінець діапазона, 
і вертатиме список простих чисел всередині цього діапазона.
"""

def prime_list(start, end, *args):
    list_of_primes = []

    for number in range(start, end+1):
        if number > 1:
            prime = True
            
            for i in range(2, number//2+1):
                if (number % i) == 0:
                    prime = False
                    break

            if prime:
                list_of_primes += [number]

    return list_of_primes

start = (int(input('Введіть початкове число: ')))
end = (int(input('Введіть кінцеве число: ')))

print(prime_list(start, end))
