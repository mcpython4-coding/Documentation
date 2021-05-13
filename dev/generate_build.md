***generate_build.py - documentation - last updated on 13.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable HOME

    class ProjectView
        
        Helper class for in-memory file manipulation


        function __init__(self)

            variable self.path_lookup

            variable self.path_cache

            variable self.modified_files

        function with_directory_source(
                self,
                directory: str,
                filter_files: typing.Callable[[str], bool] = lambda _: True,
                ):
            
            Adds the files from a directory to the project view
            :param directory: the directory to load from
            :param filter_files: a filter function; useful when only special files should be included


                    variable whole_file

                    variable f

                        variable self.path_lookup[f]

        function copy(self) -> "ProjectView"
            
            Copies the ProjectView class; Writing to the files not loaded into memory are still changed in the view


        function read(self, file: str, cache=False) -> bytes
            
            Reads a relative file
            :param file: the relative file
            :param cache: if the read data should be cached; useful when planning to access it multiple times in the near
                future
            :return: the data


                variable data

                variable self.path_cache[file]

        function write(self, file: str, data: bytes)
            
            Writes data into the local cache, overriding existing data, and overriding the original file data previously
                accessable via read()
            :param file: the file
            :param data: the data to write


        function dump_into_directory(
                self,
                directory: str,
                file_filter: typing.Callable[[str], bool] = lambda _: True,
                ):
            
            Writes all affected files into the given directory (all files accessed by with_directory_source
                and write()-en to)
            :param directory: the directory to write to
            :param file_filter: a filter for the files


        function dump_into_zipfile(
                self, file: str, file_filter: typing.Callable[[str], bool] = lambda _: True
                ):
            
            Writes all affected files into the given zipfile (all files accessed by with_directory_source
                and write()-en to)
            :param file: the file to write into
            :param file_filter: a filter for the files


        function filter_in_place(self, file_filter: typing.Callable[[str], bool])

        function merge(self, other: "ProjectView")

        function print_stats(self)

    class AbstractBuildStage extends ABC
        
        Base class for a stage in the build system


        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class AbstractProjectPreparation extends ABC
        
        Base class for a preparation stage; A stage affecting files, and not consuming a ProjectView.
        The ProjectView is created based on the results of this transformer


        function execute_in(self, directory: str, build_manager)

    class ProjectBuildManager
        
        The manager, storing how to build certain things


        function __init__(self)

            variable self.preparation_stages: typing.List[AbstractProjectPreparation]

            variable self.stages: typing.List[AbstractBuildStage]

            variable self.build_name

            variable self.version_id

        function add_preparation_stage(self, stage: AbstractProjectPreparation)
            
            Adds such preparation stage to the internal list
            :param stage: the stage


        function add_stage(self, stage: AbstractBuildStage)
            
            Adds a normal stage into the internal list
            :param stage: the stage to add


        function run(
                self,
                directory: str,
                build_output_dir: str,
                project_view_consumer: typing.Callable[[ProjectView], None] = None,
                ):
            
            Runs the build configuration onto the given directory and outputs the data at the given directory
            :param directory: the directory to use as a source
            :param build_output_dir: the directory to output to
            :param project_view_consumer: a consumer for the project view, for additonal changes


            variable view

    class BlackCodeFormattingPreparation extends AbstractProjectPreparation

        function execute_in(self, directory: str, build_manager)

    class ISortCodeFormattingPreperation extends AbstractProjectPreparation

        function execute_in(self, directory: str, build_manager)

    class UpdateLicenceHeadersPreparation extends AbstractProjectPreparation

        function execute_in(self, directory: str, build_manager)

    class PyMinifierTask extends AbstractBuildStage

        function __init__(self, special_config={})

            variable self.special_config

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class JsonMinifierTask extends AbstractBuildStage

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class BuildSplitStage extends AbstractBuildStage
        
        A stage for splitting the current build chain into a sub-chain not modifying the base chain


        function __init__(self, *parts: AbstractBuildStage, merge_back=False)

            variable self.parts

            variable self.merge_back

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class BuildSplitUsingManagerAndTMPCache extends AbstractBuildStage
        
        Similar to BuildSplitStage, but takes a whole ProjectBuildManager.
        Data is written to a temporary directory


        function __init__(self, manager: ProjectBuildManager, merge_back=False)

            variable self.manager

            variable self.merge_back

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class DumpTask extends AbstractBuildStage
        
        Task for dumping the whole file tree
        as_zip defines if the data should be written to a zip file or not
        file_filter is passed to the dump function


        function __init__(
                self,
                file_or_dir_name: str,
                as_zip=True,
                file_filter: typing.Callable[[str], bool] = lambda _: True,
                ):

            variable self.file_or_dir_name

            variable self.as_zip

            variable self.file_filter

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class FileFilterTask extends AbstractBuildStage
        
        Helper for filtering the project view by file name


        function __init__(self, file_filter: typing.Callable[[str], bool])

            variable self.file_filter

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class FileRenamerTask extends AbstractBuildStage
        
        Helper for renaming certain files in the tree


        function __init__(self, renamer: typing.Callable[[str], str])

            variable self.renamer

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

                        variable view.path_lookup[new_file]

    class FilePrefixRenamerTask extends FileRenamerTask

        function __init__(self, renames_from, renames_to)

            variable self.renames_from

            variable self.renames_to

        function rename(self, file: str) -> str

        function __repr__(self)

    class DocumentationStripper extends AbstractBuildStage

        static
        function transform_file(cls, file: str, view: ProjectView)

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
            i = 0
            while i < len(result):
                line = result[i]


            variable string

                variable string

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)

    class CustomCodePatcher extends AbstractBuildStage

        function execute_on(self, view: ProjectView, build_output_dir: str, build_manager)
    
        [
            sys.executable,
            home + "/__main__.py",
            "--data-gen",
            "--exit-after-data-gen",
            "--no-window",
        ],
        stdout=sys.stdout,


                    variable "IS_DEV

            variable data

    variable PY_FILE_FILTER

    variable CLIENT_FILE_STRIPPER

    variable DEFAULT_BUILD_INSTANCE

    function main(*argv)
        
        Launcher for the default build configuration for mcpython
        :param argv: argv, as passed to sys.argv
        First element may be build name, second may be output folder


                variable config

            variable output_folder

            variable output_folder

        variable version_id

        variable DEFAULT_BUILD_INSTANCE.build_name

        variable DEFAULT_BUILD_INSTANCE.version_id