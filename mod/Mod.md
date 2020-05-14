***Mod.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ModDependency

        function __init__(self, name: str, version_min=None, version_max=None, versions=None)
            
            creates an new mod dependency instance. need to be assigned with another mod. if no version(s) is/are specified,
            all are allowed
            :param name: the name of the mod
            :param version_min: the minimum version to use, including
            :param version_max: the maximum version to use, including
            :param versions: set when an list of possible versions should be used. Can contain min-value and
                tuples of (min, max) [a whole range]


            variable self.name

            variable self.version_range

            variable self.versions

        static function convert_any_to_version_tuple(cls, a)

        function arrival(self) -> bool

        function __testfor(self, version, args: tuple) -> bool

        function get_version(self)

        function __str__(self)

    class Mod
        
        class for mods. for creating an new mod, create an instance of this


        function __init__(self, name: str, version: tuple)
            
            creates an new mod
            :param name: the name of the mod
            :param version: an tuple of CONSTANT length across ALL versions representing the version of the mod


        function mod_string(self)

        function add_load_default_resources(self)

        function add_dependency(self, depend)

        function add_not_load_dependency(self, depend)

        function add_not_compatible(self, depend)

        function add_load_before_if_arrival(self, depend)

        function add_load_after_if_arrival(self, depend)

        function add_load_only_when_arrival(self, depend)

        function add_load_only_when_not_arrival(self, depend)