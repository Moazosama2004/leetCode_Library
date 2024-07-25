class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        skip = False
        sum = 0

        for index in range(len(s)):
            if (index == len(s) - 1 and not skip) :
                sum += roman_numerals[s[index]]
                break
            if not skip:
                if s[index] == "I":
                    if s[index + 1] == "V":
                        sum += 4
                        skip = True
                    elif s[index + 1] == "X":
                        sum += 9
                        skip = True
                    else:
                        sum += roman_numerals[s[index]]
                elif s[index] == "X":
                    if s[index + 1] == "L":
                        sum += 40
                        skip = True
                    elif s[index + 1] == "C":
                        sum += 90
                        skip = True
                    else:
                        sum += roman_numerals[s[index]]
                elif s[index] == "C":
                    if s[index + 1] == "D":
                        sum += 400
                        skip = True
                    elif s[index + 1] == "M":
                        sum += 900
                        skip = True
                    else:
                        sum += roman_numerals[s[index]]
                else:
                    sum += roman_numerals[s[index]]
            else:
                skip = False
        return sum
