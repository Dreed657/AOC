f = open('advent/day1/input', 'r')
lines = f.readlines();

strToDigit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0

for calibraiton in lines:
    clean = calibraiton.rstrip('\n')
    
    chars = list(clean)
    
    digits = list()
    
    for idx, char in enumerate(chars):
        if char.isdigit():
            digits.append(char)
        elif numbers.__contains__(clean[idx:idx+3]):
            digits.append(strToDigit[clean[idx:idx+3]])
        elif numbers.__contains__(clean[idx:idx+4]):
            digits.append(strToDigit[clean[idx:idx+4]])
        elif numbers.__contains__(clean[idx:idx+5]):
            digits.append(strToDigit[clean[idx:idx+5]])
            
    print(digits)
    num = int(digits[0] + digits[-1])
    
    total += num
  
print(total);
