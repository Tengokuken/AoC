def captcha(str):
    points = 0
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            points += int(str[i])
    if str[-1] == str[0]:
        points += int(str[-1])
    return points

def captcha2(str):
    str1 = str[:len(str)//2]
    str2 = str[len(str)//2:]
    points = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            points += int(str1[i]) + int(str2[i])
    return points

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()[0]
    line = lines.strip()
    file.close()
    result = captcha(line)
    print(result)
    result = captcha2(line)
    print(result)

