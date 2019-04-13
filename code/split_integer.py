def splitInteger(num,parts):
    array = []
    for i in range(parts):
        if i < num % parts:
            value = num // parts + 1
        else:
            value = num // parts
        array.append(value)

    return sorted(array)

