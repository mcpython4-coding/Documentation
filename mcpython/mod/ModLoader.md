***ModLoader.py - documentation - last updated on 7.7.2020 by uuk***
___

    class LoadingStage
        
        class for any loading stage for the system


        function __init__(self, name, *eventnames)
            
            creates an new instance of LoadingStage
            :param name: the name of the stage
            :param eventnames: an list of events to call in this stage


            variable self.name

            variable self.active_event_name

            variable self.active_mod_index

            variable self.eventnames

            variable self.running_event_names

            variable self.progress

            variable self.max_progress

        static
        function finish(cls, astate)
            
            will finish up the system
            :param astate: the state to use


                variable G.modloader.finished

            variable astate.parts[2].progress

            variable new_stage

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress_max

        function call_one(self, astate)
            
            will call one event from the stack
            :param astate: the state to use


    class LoadingStages
        
        collection of all stages with their events


        variable PREPARE
            used to do the magic stuff to set up your system

        variable ADD_LOADING_STAGES
            this special phase is for adding new loading phases, if you want to

        variable EXTRA_RESOURCE_LOCATIONS
            if your mod has other resource locations...

        variable PREBUILD
            deprecated (but removal in future) system of preparing data, but storing them in an "cache"
            should be replaced by data gen and similar

        variable CONFIGS
            first: create ConfigFile objects, second: internally, third: do something with the data

        variable COMBINED_FACTORIES
            Stage collection for combined factories, last for building them

        variable BLOCKS
            blocks, items, inventories, ... all stuff to register

        variable ITEMS

        variable INVENTORIES

        variable COMMANDS

        variable ENTITIES

        variable DATA_GENERATION
            Optional stage for running the data generators. Only active in --data-gen mode

        variable LANGUAGE
            all the deserialization stuff, must be after data gen as data gen may want to inject some stuff

        variable TAGS

        variable RECIPE

        variable LOOT_TABLES

        variable MODEL_FACTORY
            so, all stuff around block models & states

        variable BLOCKSTATE

        variable BLOCK_MODEL

        variable BAKE

        variable WORLDGEN
            now, the world gen, depends on results of registry system and data deserialization

        variable FILE_INTERFACE
            How about storing stuff?

        variable STATES
            Display-ables. Depends on most of above, nothing depends on

        variable POST

    variable LOADING_ORDER: list
        the order of stages todo: make serialized from config file

    class ModLoaderAnnotation
        
        representation of an @G.modloader([...]) annotation
        todo: make use lambdas


        function __init__(self, modname: str, eventname: str, info=None)
            
            creates an new annotation
            :param modname: the name of the mod to annotate to
            :param eventname: the event name to subscribe to
            :param info: the info send to the event bus


            variable self.modname

            variable self.eventname

            variable self.info

        function __call__(self, function)
            
            subscribes an function to the event
            :param function: the function to use
            :return: the function annotated


    class ModLoader
        
        the mod loader class


        function __init__(self)
            
            creates an new modloader-instance


            variable self.found_mods

            variable self.mods

            variable self.modorder

            variable self.active_directory

            variable self.active_loading_stage

            variable self.lasttime_mods

            variable self.found_mod_instances

                    variable self.lasttime_mods

        function __call__(self, modname: str, eventname: str, info=None) -> ModLoaderAnnotation
            
            annotation to the event system
            :param modname: the mod name
            :param eventname: the event name
            :param info: the info
            :return: an ModLoaderAnnotation-instance for annotation


        static
        function get_locations(cls) -> list
            
            will return an list of mod locations found for loading


        function load_mod_jsons(self, modlocations: list)
            
            will load the mod description files for the given locations and parse their content
            :param modlocations: the locations found


        function look_out(self)
            
            will load all mods arrival


        function check_for_update(self)
            
            will check for changes between versions


        function write_mod_info(self)
            
            writes the data for the mod table into the file


        function load_mods_json(self, data: str, file: str)
            
            will parse the data to the correct system
            :param data: the data to load
            :param file: the file located under


        static
        function load_from_decoded_json(cls, data: dict, file: str)
            
            will parse the decoded json-data to the correct system
            :param data: the data of the mod
            :param file: the file allocated (used for warning messages)


        @deprecation.deprecated("dev1:2", "a1.2.0")
        static
        function load_new_json(cls, data: dict, file: str)

        static
        function load_json(cls, data: dict, file: str)
            
            load the stored json file
            :param data: the data to load
            :param file: the file to load, for debugging uses

                
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


        static
        function cast_dependency(cls, depend: dict)
            
            will cast an dict-structure to the depend
            :param depend: the depend dict
            :return: the parsed mod.Mod.ModDependency-object


        @deprecation.deprecated("dev1:2", "a1.3.0")
        static
        function _load_from_old_json(data: dict, file: str)

        function load_mods_toml(self, data: str, file)
            
            will load an toml-data-object
            :param data: the toml-representation
            :param file: the file for debugging reasons


        function add_to_add(self, modinstance: mcpython.mod.Mod.Mod)
            
            will add an mod-instance into the inner system
            :param modinstance: the mod instance to add


        function check_mod_duplicates(self)
            
            will check for mod duplicates
            :return an tuple of errors as string and collected mod-info's as dict
            todo: add config option for strategy: fail, load newest, load oldest, load all


        function check_dependency_errors(self, errors: list, modinfo: dict)
            
            will iterate through
            :param errors: the error list
            :param modinfo: the mod info dict
            :return: errors and modinfo-tuple


        function sort_mods(self)
            
            will create the modorder-list by sorting after dependencies


            variable self.modorder

        function process(self)
            
            will process some loading tasks


        function update_pgb_text(self)
            
            will update the text of the pgb's in mod loading


    variable G.modloader

    @G.modloader("minecraft", "special:exit")
    function exit()