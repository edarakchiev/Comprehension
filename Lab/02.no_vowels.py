text = input()

vowels = ['a', 'o', 'u', 'e', 'i']
vowels.extend([el.upper() for el in vowels])
result = [ch for ch in text if ch not in vowels]
print("". join(result))