def FromFormatToInt(date):
    result = date.split('/')

    if (int(result[1]) < 10):
        result[1] = '0' + result[1]

    if (int(result[2]) < 10):
        result[2] = '0' + result[2]
    
    return int(result[0] + result[1] + result[2])
