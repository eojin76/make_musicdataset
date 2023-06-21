import re


def get_milliseconds_array() -> list[int]:
    pattern = re.compile(r"\d+:\d+(:\d+)?")
    li = []
    while True:
        line = input()
        if line.lower() == "end":
            break
        match = pattern.search(line)
        if not match:
            continue
        x = match[0].split(":")
        if len(x) == 2:
            x.insert(0, "0")
        hour, minute, second = map(int, x)
        ms = ((hour * 60 + minute) * 60 + second) * 1000
        li.append(ms)
    return li
