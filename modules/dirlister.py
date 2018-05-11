import cs

def run(**args):

    print("[*] In dirlister module.")
    files = cs.listdir(".")

    return str(files)

