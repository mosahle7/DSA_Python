def sortInt(a1, a2):
    s1 = set(a1)
    s2 = set(a2)
    union_elements = sorted(s1 & s2)  # Union of s1 and s2
    return union_elements

# If sorted:

def sortInt(a1, a2):
    i, j = 0, 0
    result = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            i += 1
        elif a1[i] > a2[j]:
            j += 1
        else:
            if not result or result[-1] != a1[i]:  # Avoid duplicates
                result.append(a1[i])
            i += 1
            j += 1
    return result
