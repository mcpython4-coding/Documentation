***ModLoader.py - documentation - last updated on 14.5.2020 by uuk***
___

    class LoadingStage

        function __init__(self, name, *eventnames)

            variable self.name

            variable self.active_event_name

            variable self.active_mod_index

            variable self.eventnames

            variable self.running_event_names

            variable self.progress

            variable self.max_progress

        static function finish(cls, astate)

        function call_one(self, astate)

    class LoadingStages

        variable PREPARE

        variable ADD_LOADING_STAGES

        variable PREBUILD

        variable EXTRA_RESOURCE_LOCATIONS

        variable TAGS

        variable BLOCKS

        variable ITEMS

        variable LANGUAGE

        variable RECIPE

        variable INVENTORIES

        variable STATES

        variable COMMANDS

        variable LOOT_TABLES

        variable ENTITIES

        variable WORLDGEN

        variable BLOCKSTATE

        variable BLOCK_MODEL

        variable BAKE

        variable FILE_INTERFACE

        variable POST

    variable LOADING_ORDER

    class ModLoaderAnnotation

        function __init__(self, modname: str, eventname: str, info=None)

            variable self.modname

            variable self.eventname

            variable self.info

        function __call__(self, function)

    class ModLoader

        function __init__(self)

            variable self.found_mods

            variable self.mods

            variable self.modorder

            variable self.active_directory

            variable self.active_loading_stage

            variable self.lasttime_mods

            variable self.found_mod_instances

                    variable self.lasttime_mods

        function __call__(self, modname: str, eventname: str, info=None) -> ModLoaderAnnotation

        static function get_locations(cls) -> list

        function load_mod_jsons(self, modlocations: list)

        function look_out(self)

        function check_for_update(self)

        function write_mod_info(self)

        function load_mods_json(self, data: str, file: str)

        static function load_from_decoded_json(cls, data: dict, file: str)

        static function load_new_json(cls, data: dict, file: str)

        static function cast_dependency(cls, depend)

        static function _load_from_old_json(data: dict, file: str)

        function load_mods_toml(self, data: str, file)

        function add_to_add(self, mod)

        function check_mod_duplicates(self)

        function check_dependency_errors(self, errors, modinfo)

        function sort_mods(self)

            variable self.modorder

        function process(self)

        function update_pgb_text(self)

    variable G.modloader