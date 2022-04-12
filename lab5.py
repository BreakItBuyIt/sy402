import os
import hashlib
import datetime
import json

def hashf(f):
    x = ""
    with open(f, 'rb') as file:
        x = file.read()
    h = hashlib.new('sha256')
    h.update(x)
    return h.hexdigest()

def filesearch():
    nolist = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
    dict = {}
    changes = []
    for sys, dirs, files in os.walk("/"):
        for f in files:
            path = os.path.join(sys, f)
            if path in nolist:
                pass
            time = str(datetime.datetime.now())
            dict[path] = (hashf(path), time)
            print(path)
    update = json.dumps(dict)
    print("testing...")

    try: #creates log file if it doesn't exist
        a = open("log.txt", "x")
        a.write(update)
    except:
        pass



    f = open("log.txt")
    old = json.load(f)
    f.close()

    with open("log.txt", "w") as file1:
        file1.write(update)

    for key in old.keys():
        if key not in dict.keys():
            u = ""
            u += "File deleted: "
            u += key
            changes.append(u)
    for key in dict.keys():
        if key not in old.keys():
            u = ""
            u += "File created: "
            u += key
            changes.append(u)
        elif old[key][0] != dict[key][0]:
            print(old[key][1], dict[key][1])
            u = ""
            u += "File changed: "
            u += key
            changes.append(u)

    if len(changes) == 0:
        print("No changes detected!")
    else:
        for change in changes:
            print(change)



    return

filesearch()
