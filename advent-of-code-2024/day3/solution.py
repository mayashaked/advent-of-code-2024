import re
import ast

def part1():

    result = 0
    full_text = ''
    with open('input.txt', 'r') as file:
        for line in file:
            full_text += line

    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, full_text)
    for match in matches:
        string_tuple = match[3:]
        try: # this is pretty lazy, but regex are hard!!
            num1, num2 = ast.literal_eval(string_tuple)
            if num1 < 1000 and num2 < 1000:
                result += num1 * num2
        except:
            None

    print(result)
    return(result)

def part2():

    result = 0
    full_text = ''
    with open('input.txt', 'r') as file:
        for line in file:
            full_text += line

    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, full_text)
    do = True
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif match not in ("do()", "don't()") and do:
            string_tuple = match[3:]
            try:
                num1, num2 = ast.literal_eval(string_tuple)
                if num1 < 1000 and num2 < 1000:
                    result += num1 * num2
            except:
                None

    print(result)
    return(result)


if __name__ == "__main__":
    part1()
    part2()
