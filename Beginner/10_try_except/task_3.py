n = []
dict_ = {}

try:
    # print(n[5])
    # print(dict_["salom"])
    print(n["salom"])
except (LookupError, TypeError) as e:
    print(f"You have {e.__class__.__name__}")