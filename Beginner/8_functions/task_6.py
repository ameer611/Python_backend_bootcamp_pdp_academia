def reverse_(name):
    if len(name) == 1:
        return name
    else:
        result = reverse_(name[1:]) + name[0]
        return result

print(reverse_('salom'))