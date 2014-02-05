

'''
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


def to_english(number):
    '''Taken from http://zacharydenton.com/project-euler-solutions/17/'''	
    _ones = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            }

    _tens = {
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety'
            }
    if abs(number) >= 10000:
        return str(number)
    elif number == 0:
        return 'zero'
    else:
        output = ''

        if number < 0:
            output += 'negative '
            number = abs(number)

        if number >= 1000:
            output += _ones[number // 1000]
            if number % 1000 == 0:
                output += " thousand"
            else:
                output += " thousand "
            number %= 1000

        if number >= 100:
            output += _ones[number // 100]
            if number % 100 == 0:
                output += " hundred"
            else:
                output += " hundred and "
            number %= 100

        if number >= 20:
            output += _tens[number // 10]
            number %= 10
            if number % 10 in _ones:
                output += '-'

        if number in _ones:
            output += _ones[number]

        return output

def problem17():
    total = 0
    for i in range(1,1000+1):
        s = to_english(i).replace(' ','').replace('-','')
        total += len(s)
    return total

from cProfile import run
if __name__ == "__main__":
    print(problem17())
    run("problem17()")

