import re

def read_template(filepath):
    """
    takes in a filepath as a string
    returns contents of the file as a string
    """
    with open(filepath) as f:
        contents = f.read()
    return contents


def parse_template(contents):
    stripped = re.findall('([^[}]+)(?:$|{)', contents)
    parts = re.findall('{(.*?)}', contents)
    txt = ' '.join(stripped)
    return txt.replace('  ', ' {}'), tuple(parts)


def merge(stripped, parts):
    return stripped.format(*parts)


def input_sequence():
    raw_text = read_template("assets/template.txt")
    stripped, parts = parse_template(raw_text)
    new_parts = []
    for word in parts:
        filler = input(f'Give me a {word} ')
        new_parts.append(filler)
    merged = merge(stripped, new_parts)
    print(merged)



if __name__ == '__main__':
    print('MadLib CLI edition')
    input_sequence()

