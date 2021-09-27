***Mod.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ModDependency
        
        Class for a dependency-like reference to a mod


        function __init__(self, name: str, version_min=None, version_max=None, versions=None)
            
            Creates a new mod dependency instance. Needs to be assigned to another mod. If no version is specified,
            all versions match this dependency.
            :param name: the name of the mod to depend on
            :param version_min: the minimum version to use, including
            :param version_max: the maximum version to use, including
            :param versions: set when an list of possible versions should be used. Can contain min-value and
                tuples of (min, max) [a whole range]


            variable self.name

            variable self.version_range

            variable self.versions

        static
        function convert_any_to_version_tuple(cls, a)

        function arrival(self) -> bool

        static
        function test_match(cls, version, args: tuple) -> bool
            
            Will test if the dependency is matching
            :param version: the version found
            :param args: optional args found


        function get_version(self)
            
            Getter for the real version of the mod specified by this


        function __str__(self)
            
            Returns a string representing this class


            variable cond

    class Mod
        
        Class for mods. For creating a new mod, create an instance of this or define an entry in the latest version in your
        mod.json file.
        Can be subclassed for custom mod specs


        function __init__(
                self,
                name: str,
                version: typing.Union[tuple, str, set, list],
                version_name: str = None,
                add_to_mod_loader=True,
                ):

            variable version_name: str
            
            Creates a new mod
            :param name: the name of the mod
            :param version: a tuple of CONSTANT length across ALL versions representing the version of the mod
            :param add_to_mod_loader: if to register to the mod loader


                    variable version

                    variable version

            variable self.name

            variable self.eventbus: mcpython.engine.event.EventBus.EventBus
                The mod event bus

            variable self.depend_info
                need, possible, not possible, before, after, only with, only without

            variable self.path - the path this mod is loaded from

            variable self.container - the mod loader container this is in

            variable self.version - the version of the mod, as an tuple

            variable self.version_name

            variable self.package - the package where the mod-file was found

            variable self.resource_access - where to load resources from

        function mod_string(self)
            
            Will transform the mod into a string for display purposes


        function __repr__(self)

        function add_load_default_resources(self, path_name=None)
            
            Adds the default resource locations for loading into the system
            :param path_name: optional: the namespace to load


        function add_dependency(self, depend: typing.Union[str, ModDependency])
            
            Will add a dependency into the system; The selected mod will be loaded before this one
            :param depend: the mod to depend on


        function add_not_load_dependency(self, depend: typing.Union[str, ModDependency])
            
            Will add a dependency without setting load_after for this mod
            :param depend: the mod to depend on


        function add_not_compatible(self, depend: typing.Union[str, ModDependency])
            
            Sets a mod for not loadable together with another one, meaning incompatibility, for example
            :param depend: the mod to not load with


        function add_load_before_if_arrival(self, depend: typing.Union[str, ModDependency])
            
            Will load these mod before the selected, but will not set the dependency
            :param depend: the mod to load before
            :return:


        function add_load_after_if_arrival(self, depend: typing.Union[str, ModDependency])
            
            Will load these mod after the selected, but will not set the dependency
            :param depend: the mod to load after
            :return:


        function add_load_only_when_arrival(self, depend: typing.Union[str, ModDependency])
            
            Will only load the mod if another one is arrival, but will not cause an dependency error when not arrival
            :param depend: the mod to check for


        function add_load_only_when_not_arrival(self, depend: typing.Union[str, ModDependency])
            
            Will only load the mod if another one is not arrival, but will not cause an dependency error when arrival,
            :param depend: the mod to check for


        function check_dependencies(self, mod_loader, mod_info)