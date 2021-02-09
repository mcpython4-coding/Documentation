***ModLoader.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ModLoader
        
        The mod loader class


        function __init__(self)
            
            Creates an new mod-loader-instance
            WARNING: only ONE instance should be present.
            When creating a second instance, you should know what you are doing!


            variable self.located_mods: typing.List[mcpython.common.mod.Mod.Mod]

            variable self.mod_loading_order: typing.List[str]

            variable self.active_directory: typing.Optional[str]

            variable self.active_loading_stage: int

            variable self.previous_mods

            variable self.located_mod_instances

                    variable self.previous_mods

            variable self.finished

            variable self.reload_stages: typing.List[str]

            variable self.error_builder

        function register_reload_assigned_loading_stage(self, stage: str)
            
            Will register an loading stage as one to executed on every reload
            :param stage: the event name of the stage
            todo: remove -> resource pipe


        function execute_reload_stages(self)

        function __call__(
                self, modname: str, event_name: str, *args, **kwargs
                ) -> typing.Callable[[typing.Callable], typing.Callable]:
            
            Annotation to the event system
            :param modname: the mod name
            :param event_name: the event name
            :param info: the info
            :return: an ModLoaderAnnotation-instance for annotation


        function __getitem__(self, item: str)

        function __contains__(self, item)

        function __iter__(self)

        function get_locations(self) -> list
            
            Will return an list of mod locations found for loading
            todo: split up into smaller portions


                variable element

            variable i

                variable element

                    variable file

        function load_mod_json_from_locations(self, locations: typing.List[str])
            
            Will load the mod description files for the given locations and parse their content
            :param locations: the locations found


                        variable self.active_directory

                        variable self.active_directory

                            variable data

                            variable data

                            variable instance.package

                    variable self.active_directory

        function look_out(self, from_files=True)
            
            Will load all mods arrival


            variable i

                variable element

                    variable name

        function check_for_update(self)
            
            Will check for changes between versions between this session and the one before


                    variable shared.invalidate_cache

                    variable shared.invalidate_cache
                        we have an mod which was loaded not previous but now
                        todo: include version of the mod

        function write_mod_info(self)
            
            Writes the data for the mod table into the file


        function load_mods_json(self, data: str, file: str)
            
            Will parse the data to the correct system
            :param data: the data to load
            :param file: the file located under


        function load_from_decoded_json(self, data: dict, file: str)
            
            Will parse the decoded json-data to the correct system
            :param data: the data of the mod
            :param file: the file allocated (used for warning messages)
            todo: maybe a better format?

                
                example:
                {
                    "version": "1.2.0",
                    "entries": [
                        {
                            "name": "TestMod",
                            "version": "Some.Version",
                            "load_resources": true,
                            "load_files": ["some.package.to.load"]
                        }
                    ]
                }


                    variable modname

                    variable loader

                        variable version

                        variable instance

                                variable t

        static
        function cast_dependency(cls, depend: dict)
            
            will cast an dict-structure to the depend
            :param depend: the depend dict
            :return: the parsed mod.Mod.ModDependency-object


                variable config["version_min"]

                variable config["version_max"]

                variable config["versions"]

        function load_mods_toml(self, data: str, file: str)
            
            Will load a toml-data-object
            :param data: the toml-representation
            :param file: the file for debugging reasons


                variable version

                    variable mc_version - todo: implement

                    variable mc_version

                variable mc_version

                    variable name

        function add_to_add(self, instance: mcpython.common.mod.Mod.Mod)
            
            Will add a mod-instance into the inner system
            :param instance: the mod instance to add
            Use only when really needed. The system is designed for beeing data-driven!


            variable self.mods[instance.name]

                variable instance.path

        function check_mod_duplicates(self)
            
            Will check for mod duplicates
            :return an tuple of errors as string and collected mod-info's as dict
            todo: add config option for strategy: fail, load newest, load oldest, load all, load none


                    variable errors

                    variable mod_info[mod.name]

        function check_dependency_errors(self, errors: bool, mod_info: dict)
            
            Will iterate through all mods and check dependencies
            :param errors: if errors occured
            :param mod_info: the mod info dict
            :return: errors and mod-info-tuple


                        variable errors

        function sort_mods(self)
            
            Will create the mod-order-list by sorting after dependencies
            todo: use build-in library


            variable self.mod_loading_order

        function process(self)
            
            Will process some loading tasks scheduled
            Used internally during mod loading state
            If on client, the renderer is also updated


            variable start

            variable astate: mcpython.client.state.StateModLoading.StateModLoading

            variable astate.parts[0].progress_max

            variable astate.parts[1].progress_max

                variable stage

        function update_pgb_text(self)
            
            Will update the text of the pgb's in mod loading


            variable astate: mcpython.client.state.StateModLoading.StateModLoading

            variable instance: mcpython.common.mod.Mod.Mod

            variable astate.parts[2].text

            variable astate.parts[1].text

            variable astate.parts[1].progress

            variable astate.parts[0].text

    variable shared.mod_loader