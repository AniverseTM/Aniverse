

def strip_to_len(string: str, length: int) -> str:
    string_len = len(string)
    if string_len <= length:
        return string
    else:
        diff = string_len - length
        diff += 3
        return string[:-diff] + "..."
