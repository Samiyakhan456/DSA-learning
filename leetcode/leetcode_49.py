groups = {}
for word in str:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key]=[]
    
    groups[key].append(word)
return list(groups.values())
