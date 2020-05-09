"""
This tool is about generating doc from the doc strings and extending it if needed
"""
import os
import sys
import datetime
import json


local = os.path.dirname(os.path.dirname(__file__))
config_file = local+"/tools/config.json"

if os.path.exists(config_file):
    with open(config_file) as f:
        data = json.load(f)
else:
    data = {}

path = input("path to cloned core-repo: ") if "repo" not in data and data["repo"] is not None else data["repo"]
user = input("user name: ") if "user" not in data and data["user"] is not None else data["user"]

with open(config_file, mode="w") as f:
    json.dump({"repo": path, "user": user}, f)

now_raw = datetime.datetime.now()
now = "{}.{}.{}".format(now_raw.day, now_raw.month, now_raw.year)
if not os.path.isdir(path):
    print("invalid!")
    sys.exit(-1)


for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
            a = input("generate doc for '{}'? ".format(file)).lower()
            if a not in ("y", "j", "1"): continue
            real_file = os.path.join(root, file)
            doc_file = os.path.join(local, file.split(".")[0]+".md")
            print("generating doc for '{}'".format(file))
            doc = """***{} - documentation - last updated on {} by {}***
___""".format(file, now, user)
            with open(real_file) as f:
                lines = f.read().split("\n")
            in_doc = False
            doc_type = None
            handler_type = 0
            doc_string = ""
            for i, oline in enumerate(lines):
                line = oline.strip()
                level = oline.count("    ")
                if in_doc:
                    doc_string += "\n"+"    "*level+line.replace('"""', "")
                if line.startswith('"""') or line.endswith('"""'):
                    in_doc = not in_doc
                    if in_doc:
                        if handler_type == 0:
                            doc_type = 0
                        elif handler_type == 1:
                            doc_type = 1
                        elif handler_type == 2:
                            doc_type = 2
                    else:
                        if doc_type in (0, 1, 2):
                            doc += "\n"+"    "*(level if doc_type == 0 else level+1)+"{}\n".format(doc_string)
                        doc_string = ""
                elif in_doc: pass
                else:
                    s = line.split(" ")
                    if s[0] == "class":
                        handler_type = 1
                        c = s[1].split("(")[0].split(":")[0]
                        doc += "\n"+"    "*(level+1)+"class {}".format(c)
                        if s[1].count("(") > 0:
                            doc += " extends "+line[line.index("(")+1:line.index(")")].replace(",", ", ")
                    elif s[0] == "def":
                        handler_type = 2
                        f = line[line.index("def")+4:line.index(")")+1]
                        doc += "\n"+"    "*(level+1)+"function {}".format(f)+"\n"
                    elif len(s) > 1:
                        if s[1] == "=" or (len(s) > 2 and s[2] == "=" and s[0].endswith(":")):
                            doc += "\n"+"    "*(level+1)+"variable {}".format(s[0])
                            if s[0].endswith(":"):
                                doc += " " + s[1]
                            if "#" in line:
                                doc += " - {}".format(line[line.index("#")+2:])
                            i2 = i
                            sdoc = [""]
                            while i2 > 0:
                                p = lines[i2-1].strip()
                                if p.startswith("#"):
                                    sdoc.append(p[1:])
                                else:
                                    break
                                i2 -= 1
                            if len(sdoc) > 1:
                                sdoc.reverse()
                                doc += ("\n"+"    "*(level+1)).join(sdoc)
                            doc += "\n"
            flag = os.path.exists(doc_file)
            with open(doc_file, mode="w") as f:
                f.write(doc)
            if flag:
                print("please adapt file {} as it had content before!".format(doc_file))
                input()

