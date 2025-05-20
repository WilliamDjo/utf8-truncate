def truncate(s, n):
    if n >= len(s):
        return s

    while n > 0 and (s[n] & 0xC0) == 0x80:
        n -= 1

    return s[:n]


with open("cases", "rb") as fin, open("truncated_cases", "wb") as fout:
    for line in fin:
        if not line:
            continue
        truncate_len = line[0]
        utf8_data = line[1:-1]
        res = truncate(utf8_data, truncate_len)
        fout.write(res + b"\n")
