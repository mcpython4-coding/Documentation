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

                variable G.modloader.finished

            variable astate.parts[2].progress

            variable new_stage

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress_max

        function call_one(self, astate)

                variable self.active_mod_index

                variable self.active_event_name

                variable modinst: mod.Mod.Mod

                variable self.max_progress

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress

                variable self.active_event_name

            variable modname

            variable modinst: mod.Mod.Mod

                    variable self.active_mod_index

                    variable self.active_event_name

                    variable modinst: mod.Mod.Mod

                        variable self.max_progress

                        variable self.max_progress

                    variable astate.parts[2].progress_max

                    variable astate.parts[2].progress

                variable modinst: mod.Mod.Mod

                    variable self.max_progress

                    variable self.max_progress

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress

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

            variable self.finished

        function __call__(self, modname: str, eventname: str, info=None) -> ModLoaderAnnotation

        static function get_locations(cls) -> list

            variable modlocations

            variable locs

            variable i

                variable element

            variable i

                variable element

                    variable file

        function load_mod_jsons(self, modlocations: list)

                        variable self.active_directory

                        variable self.active_directory

                            variable data

                            variable data

                    variable self.active_directory

        function look_out(self)

            variable modlocations

            variable i

                variable element

                    variable name

        function check_for_update(self)

                    variable G.prebuilding
                        we have an mod which was previous loaded and not now or which was loaded before in another version

                    variable G.prebuilding
                        we have an mod which was loaded not previous but now

        function write_mod_info(self)

                variable m

        function load_mods_json(self, data: str, file: str)

        static function load_from_decoded_json(cls, data: dict, file: str)

        static function load_new_json(cls, data: dict, file: str)

            variable version

                variable loader

                        variable files

                    variable modname

                    variable loader

                        variable version

                        variable modinstance

                                variable t

        static function cast_dependency(cls, depend)

            variable c

        static function _load_from_old_json(data: dict, file: str)

                variable files

        function load_mods_toml(self, data: str, file)

            variable data

                variable version

                    variable mc_version

                    variable mc_version

                variable mc_version

                    variable dependname

        function add_to_add(self, mod)

            variable self.mods[mod.name]

            variable mod.path

        function check_mod_duplicates(self)

            variable errors

            variable modinfo

                    variable modinfo[mod.name]

        function check_dependency_errors(self, errors, modinfo)

        function sort_mods(self)

            variable self.modorder

        function process(self)

            variable start

            variable astate: state.StateModLoading.StateModLoading

            variable astate.parts[0].progress_max

            variable astate.parts[1].progress_max

                variable stage

        function update_pgb_text(self)

            variable stage

            variable astate: state.StateModLoading.StateModLoading

            variable modinst: mod.Mod.Mod

            variable astate.parts[2].text

            variable astate.parts[1].text

            variable astate.parts[1].progress

            variable index

            variable astate.parts[0].text

    variable G.modloader