***generate_build.py - documentation - last updated on 26.7.2020 by uuk***
___

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

    function _copytree(entries, src, dst, symlinks, ignore, copy_function,
            ignore_dangling_symlinks, dirs_exist_ok=False):

        variable errors

        variable use_srcentry

            variable srcname

            variable dstname

            variable srcobj

                variable is_symlink

                    variable lstat
                        Special check for directory junctions, which appear as
                        symlinks but we want to recurse.

                        variable is_symlink

                    variable linkto

    function copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2,
            ignore_dangling_symlinks=False, dirs_exist_ok=False):

    variable local

    variable folder

    variable out

    function build()

                variable f

                variable t

                variable d

            variable d

            variable d

            variable d

        variable local_space

        variable now

        variable target_file

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
                            if len(line) > i + 1 and line[i:i + 3] == "'''":
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