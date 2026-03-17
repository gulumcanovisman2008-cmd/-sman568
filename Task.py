passwords = input().split(',')

result = []

for p in passwords:
    if 6 <= len(p) <= 12:
        lower = 0
        upper = 0
        digit = 0
        special = 0

        for c in p:
            if c >= 'a' and c <= 'z':
                lower = 1
            elif c >= 'A' and c <= 'Z':
                upper = 1
            elif c >= '0' and c <= '9':
                digit = 1
            elif c in "$#@":
                special = 1

        if lower and upper and digit and special:
            result.append(p)

print(','.join(result))
