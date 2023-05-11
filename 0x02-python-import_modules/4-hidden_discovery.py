#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for word_name in sorted(dir(hidden_4)):
        if word_name[:2] != '__':
            print("{}".format(word_name))
