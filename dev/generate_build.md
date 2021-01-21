***generate_build.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    how to build an final version?
    1. create directory for storing the data
    2. collect the executable files
    3. collect the licences
    4. collect the changelog
    5. collecting generated sources [re-running the game]
    6. collect the assets
    7. exchange build information in globals.py from dev-environment to build
    8. zip-up the files into one directory
    9. remove documentation strings
    10. zip-up the undocumented code


    function collect_to_zip(source, file)

    function _copytree(
            entries,
            src,
            dst,
            symlinks,
            ignore,
            copy_function,
            ignore_dangling_symlinks,
            dirs_exist_ok=False,
            ):

            variable ignored_names

            variable ignored_names

        variable errors

        variable use_src_entry

            variable src_name

            variable dst_name

            variable src_obj

                variable is_symlink

                    variable l_stat
                        Special check for directory junctions, which appear as
                        symlinks but we want to recurse.

                        variable is_symlink

                    variable link_to

    function copytree(
            src,
            dst,
            symlinks=False,
            ignore=None,
            copy_function=shutil.copy2,
            ignore_dangling_symlinks=False,
            dirs_exist_ok=False,
            ):

            variable entries

    class BuildManager
        
        Main class for creating an build of mcpython-4


        function __init__(
                self,
                name: str,
                output_folder=None,
                version_id=None,
                external_library_paths=None,
                ):

            variable self.name

            variable self.local

                variable self.config

                variable self.output_folder

                variable self.output_folder

                variable self.output_folder

                variable self.version_id

                variable self.version_id

            variable self.config["version_id"]

            variable self.library_paths

            variable self.tmp_folder

        function generate(self)

        function collect_python_files(self)

        function collect_meta(self)

        function collect_assets(self)

        function apply_code_patches(self)

                variable d

                variable data

        function create_build(self, name: str)

        function strip_documentation(self)

                    variable result - here we store the context

                    variable in_multi_line_comment

                        variable line

                        variable multi_line_change

                        variable index

                        variable in_string
                            
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


                        variable string

                            variable string