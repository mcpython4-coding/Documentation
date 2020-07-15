***build.py - documentation - last updated on 15.7.2020 by uuk***
___

    variable local

    variable pre

            variable file

            variable localized

            variable target

            variable d

            variable root_l

                    variable file

                    variable localized

                    variable target

                    variable d

    variable name

    print("creating dev-version...")
    with zipfile.ZipFile(local+"/builds/"+name+"_dev.zip", mode="w") as instance:
        root_l = len(local + "/tmp/")
        for root, dirs, files in os.walk(local + "/tmp"):
            for f in files:
                file = os.path.join(root, f)
                local = file[root_l:]
                instance.write(file, local)
    print("filtering code...")  


        variable root_l

                variable file

                variable localized

            variable data

                    variable root_l

                            variable file

                            variable localized