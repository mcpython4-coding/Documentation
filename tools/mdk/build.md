***build.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


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

        variable root_l

                variable file

                variable localized

    variable root_l

            variable file

                variable data

            variable result - here we store the context

            variable in_multi_line_comment

                variable line

                variable multi_line_change

                variable index

                variable in_string

                variable skip_entries
                
                            if in_multi_line_comment == 0:
                                in_multi_line_comment = 1
                                line = line[:index]
                                multi_line_change = True
                            elif in_multi_line_comment == 1:
                                in_multi_line_comment = 0
                                multi_line_change = True
                        elif in_string == 0:
                            in_string = 1
                        elif in_string == 1:
                            in_string = 0
                    elif e == "'" and not (i > 0 and line[i - 1] == "\\"):
                        if len(line) > i + 1 and line[i : i + 3] == "'''":
                            if in_multi_line_comment == 0:
                                in_multi_line_comment = 2
                                line = line[:index]
                                multi_line_change = True
                            elif in_multi_line_comment == 2:
                                in_multi_line_comment = 0
                                multi_line_change = True
                        elif in_string == 0:
                            in_string = 2
                        elif in_string == 2:
                            in_string = 0
                    elif e == "#" and in_string == 0 and index is None:
                        index = i
                        break
                if index is not None:
                    line = line[:index]
                if not (not multi_line_change and in_multi_line_comment != 0):
                    result.append(line)
            with open(file, mode="w") as f:
                i = 0
                while i < len(result):
                    line = result[i]


        variable root_l

                variable file

                variable localized

            variable data

                    variable root_l

                            variable file

                            variable localized