def vertical_txt(s):
    words = s.split()
    max_len = max(len(word) for word in words)
    
    result = []
    
    for i in range(max_len):
        row = []
        for word in words:
            if i < len(word):
                row.append(word[i])
            else:
                row.append(" ")
        result.append(row)
    
    print(result)
    
vertical_txt("Holy bananas")
vertical_txt("Hello fellas")
vertical_txt("Chocolate cake")
