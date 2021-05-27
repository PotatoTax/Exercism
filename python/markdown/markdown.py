import re


def parse_em_strong(line):
    m = re.match("(.*)__(.*)__(.*)", line)
    while m:
        line = f"{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}"
        m = re.match("(.*)__(.*)__(.*)", line)
    m = re.match("(.*)_(.*)_(.*)", line)
    while m:
        line = f"{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}"
        m = re.match("(.*)_(.*)_(.*)", line)
    return line


def parse(markdown):
    lines = markdown.split('\n')
    result = ""

    in_list = False

    for line in lines:
        if line.startswith("#"):
            count = 0
            while line.startswith("#"):
                count += 1
                line = line[1:]
            line = line.strip()
            line = f"<h{count}>{parse_em_strong(line)}</h{count}>"
        elif line.startswith("*"):
            if not in_list:
                in_list = True
                result += "<ul>"
            line = line[1:].strip()
            line = f"<li>{parse_em_strong(line)}</li>"
        elif in_list:
            in_list = False
            line = f"</ul><p>{parse_em_strong(line)}</p>"
        else:
            line = f"<p>{parse_em_strong(line)}</p>"

        result += line

    if in_list:
        result += "</ul>"

    return result
