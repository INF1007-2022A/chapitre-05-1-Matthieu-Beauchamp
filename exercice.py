#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return -number if number < 0 else number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = []
    for char in prefixes:
        noms.append(char + suffixe)

    return noms


def prime_integer_summation() -> int:
    nPrimes = 1
    primeSum = 2

    i = 3
    while nPrimes < 100:
        isPrime = True
        for k in range(3, int(i**0.5), 2):
            if (i / float(k)) == 0:
                isPrime = False
                break

        if isPrime:
            nPrimes += 1
            primeSum += i

        i += 2

    return primeSum


def factorial(number: int) -> int:
    fact = 1
    while number > 0:
        fact *= number
        number -= 1

    return fact


def use_continue() -> None:
    for i in range(11):
        if i == 5:
            continue

        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    verdicts = []

    for group in groups:
        nMembers = len(group)
        
        if nMembers < 3 or 10 < nMembers:
            verdicts.append(False)
            continue
        
        oneIsMinor = False
        oneIs25 = False
        oneIsOver70 = False
        oneIs50 = False
        for member in group:
            if member < 18:
                oneIsMinor = True
            elif member == 25:
                oneIs25 = True
                break
            elif member == 50:
                oneIs50 = True
            elif member > 70:
                oneIsOver70 = True

        if oneIs25:
            verdicts.append(True)
        elif oneIsMinor:
            verdicts.append(False)
        elif oneIs50 and oneIsOver70:
            verdicts.append(False)
        else:
            verdicts.append(True)
        
    return verdicts

def main() -> None:
    number = -4.325
    print(
        f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(
        f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [
            70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
