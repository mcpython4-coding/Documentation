"""
This tool is about generating doc from the doc strings and extending it if needed
"""
import os
import sys
import datetime
import json
import time


local = os.path.dirname(os.path.dirname(__file__))
config_file = local+"/tools/config.json"

if os.path.exists(config_file):
    with open(config_file) as f:
        data = json.load(f)
else:
    data = {}

path = input("path to cloned core-repo: ") if "repo" not in data or data["repo"] is None else data["repo"]
user = input("user name: ") if "user" not in data or data["user"] is None else data["user"]

with open(config_file, mode="w") as f:
    json.dump({"repo": path, "user": user}, f)

now_raw = datetime.datetime.now()
now = "{}.{}.{}".format(now_raw.day, now_raw.month, now_raw.year)
if not os.path.isdir(path):
    print("invalid!")
    sys.exit(-1)


def generate_doc(raw_file, file, doc_file_loc):
    doc = """***{} - documentation - last updated on {} by {}***
___""".format(raw_file, now, user)
    with open(file) as f:
        lines = f.read().split("\n")
    in_doc = False
    doc_type = None
    handler_type = 0
    doc_string = ""
    in_function = False
    function_level = None
    in_init = False
    pre_level = None
    skip = 0
    for i, oline in enumerate(lines):
        if skip > 0:
            skip -= 1
            continue
        line = oline.lstrip()
        level = oline[:-len(line)].count("    ")
        if pre_level is not None and pre_level > level:
            in_init = False
        pre_level = level
        if in_function and level <= function_level: in_function = False
        if '"""' in line and line.count('"""') % 2 == 1:
            in_doc = not in_doc
            if in_doc:
                if handler_type == 0:
                    if line.startswith('"""mcpython'):
                        doc_type = 3
                    else:
                        doc_type = 0
                elif handler_type == 1:
                    doc_type = 1
                elif handler_type == 2:
                    doc_type = 2
            else:
                if doc_type in (0, 1, 2):
                    doc += "\n" + "    " * (level if doc_type == 0 else level + 1) + "{}\n".format(doc_string)
                doc_string = ""
                doc_type = 0
        elif in_doc:
            if line.replace('"""', "").strip() == "": continue
            doc_string += "\n" + "    " * (level+1) + line.replace('"""', "")
        elif in_doc:
            pass
        elif not in_function or in_init:
            s = line.split(" ")
            if s[0] == "class":
                handler_type = 1
                i2 = i - 1
                mod = ""
                while i2 >= 0:
                    l = lines[i2].strip()
                    if l.startswith("@"):
                        mod += l + " "
                    else:
                        break
                    i2 -= 1
                c = s[1].split("(")[0].split(":")[0]
                doc += "\n\n" + "    " * (level + 1) + mod + "class {}".format(c)
                if s[1].count("(") > 0:
                    doc += " extends " + line[line.index("(") + 1:line.index(")")].replace(",", ", ")
            elif s[0] == "def":
                in_function = True
                function_level = level
                handler_type = 2
                mod = ""
                i2 = i - 1
                while i2 >= 0:
                    l = lines[i2].strip()
                    if l.startswith("@"):
                        if l in ("@classmethod", "@staticmethod"):
                            mod += "    " * (level+1) + "static\n"
                        else:
                            mod += "    " * (level+1) + l + "\n"
                    else:
                        break
                    i2 -= 1
                if not line.endswith(":"):
                    head = line[line.index("def") + 4:]
                    i2 = i + 1
                    while i2 < len(lines):
                        cline = lines[i2].strip()
                        head += "\n" + cline
                        if cline.endswith(":") and (("):" in cline) or (") ->" in cline)):
                            break
                        i2 += 1
                    if head.count("\n") > 5:
                        print("skipping {} as function HEAD is to big".format(line))
                        continue
                    skip = i - i2
                else:
                    head = line[line.index("def") + 4:line.rindex(":")]
                if "__init__" in line:
                    in_init = True
                doc += "\n\n" + mod + "    " * (level + 1) + "function {}".format(
                    ("\n"+"    " * (level + 3)).join(head.split("\n")))
            elif len(s) > 1:
                if s[1] == "=" or (len(s) > 2 and s[2] == "=" and s[0].endswith(":")):
                    doc += "\n\n" + "    " * (level + 1) + "variable {}".format(s[0])
                    if s[0].endswith(":"):
                        doc += " " + s[1]
                    if "#" in line:
                        doc += " - {}".format(line[line.index("#") + 2:])
                    i2 = i - 1
                    sdoc = []
                    while i2 >= 0:
                        p = lines[i2].strip()
                        if p.startswith("#"):
                            sdoc.append(p[1:].strip())
                        else:
                            break
                        i2 -= 1
                    if len(sdoc) > 0:
                        sdoc.reverse()
                        doc += "\n" + "    " * (level + 2)
                        doc += ("\n" + "    " * (level + 2)).join(sdoc)
            elif line.startswith("# todo"):
                doc += "    " * (level + 1)+line[2:]
    flag = os.path.exists(doc_file_loc)
    if flag:
        with open(doc_file_loc) as f:
            d = f.read()
        if d.split("\n")[1:] == doc.split("\n")[1:]:
            return True
    with open(doc_file_loc, mode="w") as f:
        f.write(doc)
    print("generating doc for '{}'".format(file))
    if flag:
        print("please adapt file '{}' as it had content before!".format(doc_file_loc))
        # a = input("re-run generation? ").lower()
        # if a in ("y", "j", "1"): return False
    return True


def main():
    found_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            found_files.append((root, file))

    while len(found_files) > 0:
        root, file = found_files.pop(0)
        sub_root = root[len(path)+1:]
        if file.endswith(".py"):
            # a = input("generate doc for '{}'? ".format(file)).lower()
            # if a not in ("y", "j", "1"): continue
            real_file = os.path.join(root, file)
            doc_file = os.path.join(local, sub_root, file.split(".")[0]+".md")
            d = os.path.dirname(doc_file)
            if not os.path.isdir(d):
                os.makedirs(d)
            while not generate_doc(file, real_file, doc_file):
                time.sleep(0.2)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range((len(sys.argv)-1)//3):
            i += 1
            generate_doc(*sys.argv[i*3:(i+1)*3])
    else:
        main()

