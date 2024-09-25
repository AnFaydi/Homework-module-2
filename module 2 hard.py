for num in range(3,21):
    result = str()
    for div in range(3,21):
        if num%div == 0:
                for term in range(1,div):
                    if (div-term)!=term and term < div//2+1:
                        result += f"{term}{div-term}"
        else:
            continue
    print(result)

