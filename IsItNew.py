def start(name, line, verif):
    print("[" + name + "] - Date verification...")
    with open('DateCheck.txt', 'r') as file:
        data = file.readlines()

    if verif != " ".join(data[line].split()):
        print("[" + name + "] - (msg) Modification of the verification file...")
        data[line] = verif + "\n"
        with open('DateCheck.txt', 'w') as file:
            file.writelines(data)
        Output = True
    else:
        print("[" + name + "] - (msg) No new version")
        Output = False
    print("[" + name + "] - Verification complete")

    return Output
