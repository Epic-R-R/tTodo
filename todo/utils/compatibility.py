import sys

def safe_print(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(
            s
            .replace('✓', '-') # change the checkmark symbol
            .encode('utf8')
            .decode(sys.stdout.encoding)
        )