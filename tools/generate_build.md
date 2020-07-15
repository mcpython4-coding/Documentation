***generate_build.py - documentation - last updated on 7.6.2020 by uuk***
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

        variable local_space

        variable now

                    variable t

                    variable m