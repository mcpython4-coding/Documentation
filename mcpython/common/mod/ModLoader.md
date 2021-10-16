***ModLoader.py - documentation - last updated on 16.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function cast_dependency(depend: dict)
        
        Will cast a dict-structure to the depend
        :param depend: the depend dict
        :return: the parsed mod.Mod.ModDependency-object


            variable config["version_min"]

            variable config["version_max"]

            variable config["versions"]

    function parse_provider_json(container: "ModContainer", data: dict)

    class ModContainer
        
        Class holding information about a mod file


        function __init__(self, path: str)

            variable self.path

            variable self.assigned_mod_loader: typing.Optional[AbstractModLoaderInstance]

                variable self.resource_access

                variable self.resource_access

                variable self.resource_access
                    In this case, it is a file, so we know what mod loader to use

                variable self.assigned_mod_loader

            variable self.loaded_mods

        function add_resources(self)

        function try_identify_mod_loader(self)
            
            Does some clever lookup for identifying the mod loader


                    variable self.assigned_mod_loader

        function load_meta_files(self)
            
            Looks out for some meta files


        function __repr__(self)

    class AbstractModLoaderInstance extends ABC

        static
        function match_container_loader(cls, container: ModContainer) -> bool

        function __init__(self, container: ModContainer)

            variable self.container

            variable self.parent

            variable self.raw_data

        function on_select(self)
            
            Informal method called sometime after construction


        function on_instance_bake(self, mod: mcpython.common.mod.Mod)

    class PyFileModLoader extends AbstractModLoaderInstance

    class DefaultModJsonBasedLoader extends AbstractModLoaderInstance

        static
        function match_container_loader(cls, container: ModContainer) -> bool

        function on_select(self)

            variable self.raw_data

        function load_from_data(self, data)

            variable version

                    variable modname

                    variable loader

                        variable version

                        variable instance

                                variable t

                        variable mod_loader

                        variable mod_loader.parent

    class TomlModLoader extends DefaultModJsonBasedLoader

        static
        function match_container_loader(cls, container: ModContainer) -> bool

        function on_select(self)

                variable data

            variable self.raw_data

        function load_from_data(self, data)

                        variable mod_loader

                        variable mod_loader.parent

                            variable self.container.assigned_mod_loader

                variable version

                    variable mc_version - todo: implement

                    variable mc_version

                variable mc_version

                    variable name

    class ModLoader
        
        The ModLoader class
        The mod loader is a system capable of loading code into the game, for actively modification
        the behaviour and the content of the game.
        WARNING: mods CAN damage your pc software-wise. They are small programs executed on your pc.
            Use only mods from sources you trust!
            DO  N E V E R  DOWNLOAD MODS FROM STRANGE SOURCES
            We, the developers of mcpython, give NOT WARRANTIES for things mods do, including, but not limited to,
            damage on the end user pc and/or direct or indirect stealing of valuable information about the user, including
            the download of programs to do so.


        variable KNOWN_MOD_LOADERS: typing.List[typing.Type[AbstractModLoaderInstance]]
            This stores a list of valid mod loader classes used during discovery

        function __init__(self)
            
            Creates a new mod-loader-instance
            WARNING: only ONE instance should be present, otherwise, bad things might happen


            variable self.found_mod_files: typing.Set[str]

            variable self.mod_containers: typing.List[ModContainer]

            variable self.located_mods: typing.List[mcpython.common.mod.Mod.Mod]
                the list of located mods

            variable self.mod_loading_order: typing.List[str]
                the order of mod loading, by mod name

            variable self.active_directory: typing.Optional[str]
                the directory currently loading from

            variable self.current_container: typing.Optional[ModContainer]

            variable self.active_loading_stage: int
                which stage we are in

            variable self.previous_mod_list
                used for detecting mod changes between versions

            variable self.located_mod_instances
                temporary list of mods, for setting stuff

                    variable self.previous_mod_list

            variable self.finished
                if mod loading has finished

            variable self.error_builder

        function __call__(
                self, modname: str, event_name: str, *args, **kwargs
                ) -> typing.Callable[[typing.Callable], typing.Callable]:
            
            Annotation to the event system
            :param modname: the mod name
            :param event_name: the event name
            :param info: the info, as shown by EventBus during errors
            :return: a callable, used for regisering
            Example:
            @shared.modloader("minecraft", "stage:mod:init")
            def test():
                print("Hello world!")


        function __getitem__(self, item: str)

        function __contains__(self, item: str)

        function __iter__(self)

        function look_for_mod_files(self)
            
            Scanner for mod files, parsing the parsed sys.argv stuff
            Stores the resuolt in the found_mod_files attribute of this


            variable folders

            variable files

        function parse_mod_files(self)

                variable self.current_container

                    variable self.current_container

        function check_errors(self)

        function load_missing_mods(self)

        function check_for_updates(self)
            
            Will check for changes between versions between this session and the one before
            In case of a change, rebuild mode is entered


                    variable shared.invalidate_cache

                    variable shared.invalidate_cache

        function write_mod_info(self)
            
            Writes the data for the mod table into the file


                variable m

        function add_to_add(self, instance: mcpython.common.mod.Mod.Mod)
            
            Will add a mod-instance into the inner system
            :param instance: the mod instance to add
            Use only when really needed. The system is designed for being data-driven, and things might go wrong
                when manually doing this


            variable self.mods[instance.name]

                variable instance.container

                variable instance.resource_access

                variable instance.path

        function check_mod_duplicates(self)
            
            Will check for mod duplicates
            :return an tuple of errors as string and collected mod-info's as dict
            todo: add config option for strategy: fail, load newest, load oldest, [load all}, load none


                    variable errors

                    variable mod_info[mod.name]

        function check_dependency_errors(self, errors: bool, mod_info: dict)
            
            Will iterate through all mods and check dependencies
            :param errors: if errors occurred
            :param mod_info: the mod info dict
            :return: errors and mod-info-tuple


        function sort_mods(self)
            
            Will create the mod-order-list by sorting after dependencies
            todo: use build-in library


            variable self.mod_loading_order

        function process(self)
            
            Will process some loading tasks scheduled
            Used internally during mod loading state
            If on client, the renderer is also updated


            variable start

            variable astate: mcpython.common.state.ModLoadingProgress.ModLoadingProgress

            variable astate.parts[0].progress_max

            variable astate.parts[1].progress_max

                variable stage

        function update_pgb_text(self)
            
            Will update the text of the pgb's in mod loading


            variable astate: mcpython.common.state.ModLoadingProgress.ModLoadingProgress

            variable instance: mcpython.common.mod.Mod.Mod

            variable astate.parts[2].text

            variable astate.parts[1].text

            variable astate.parts[1].progress

            variable astate.parts[0].text

    variable shared.mod_loader