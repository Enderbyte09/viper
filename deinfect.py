import os

for path, subdirs, files in os.walk("C:\\"):
    for name in files:
        if name.endswith(".py") or name.endswith(".pyw") and name != "virus.py":
            try:
                with open(os.path.join(path,name)) as f:
                    data = f.read()
                if data.startswith("###START###"):
                    print(f"Disinfected {os.path.join(path,name)}")
                    data = "\n".join(data.splitlines()[4:])
                with open(os.path.join(path,name),"w") as f:
                    f.write(data)
            except:
                pass
