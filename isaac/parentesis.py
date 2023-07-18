def is_valid(s):
    mapping = {'(':')', '{':'}','[':']',}
    closes = []
    for e in s:
        if mapping.get(e) is None:
            if len(closes) == 0:
                return False
            elif closes[-1] == e:
                closes.pop()
            else:
                return False
        elif mapping.get(e) is not None:
            closes.append(mapping.get(e))
    return True

print(is_valid('()[()({})[]]]'))
print(is_valid('()[()({})[][()]'))