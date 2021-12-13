***SaveFile.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    How to decide when an new version is needed?
    - you do better an new version in case of an update
    - you may use the old one if your data is still compatible or it is auto-fixing it OR you were on an unstable 
        feature-branch
    - you must increase the version number in case of any problems with loading new data arrays in compatible released 
        versions [e.g. an hotfix for an snapshot which changed some parts of the save]
    When to remove the data-fixers from an version?
    - the version is not played by anybody
    - two major updated were in between
    - the version was only short-living and is very outdated
    How to remove an version
    a) when the version is the last supported version of its kind, remove the DataFixer
    b) when the version is an minor between versions, remove the DataFixer and change the one before to skip the removed one
    c) when the version is an major version, remove all data-fixers up to the point
    History of save versions:
    - 1: introduced: 07.03.2020, outdated since: 10.03.2020, not loadable since: 12.12.2020
        - added save system
    - 2: introduced: 10.03.2020, outdated since: 13.03.2020, not loadable since: 12.12.2020
        - removed temperature maps from saves
        - optimized landmass map in saves
    - 3: introduced: 13.03.2020 [part of loot table update], outdated since: 31.03.2020, not loadable since: 12.12.2020
        - chest container stores now also the loot table link when set
    - 4: introduced: 31.03.2020, outdated since: -, not loadable since: 12.12.2020
        - block coordinates are stored now relative to chunk; decreases chunk size
    - 5: introduced: 17.03.2020 [part of entity update], outdated since: 11.06.2020, not loadable since: 12.12.2020
        - added entity serializer
    - 6: introduced: 11.06.2020, outdated since: 12.12.2020, not loadable since: 12.12.2020
        - re-write of data fixer system, old still fix-able
        - removed "version"-attribute out of region files and inventory files
        - data fixers are applied to the WHOLE world ON LOAD, not when needed
    - 7: introduced: 12.12.2020, outdated since: 21.05.2021, not loadable since: 21.05.2021
        - major code refactoring breaking nearly everything
        - player data reformat
    - 10: introduced: 21.05.2021, outdated since: 26.10.2021, not loadable since: 26.10.2021
        - improved block palette
        - improved entity storage
        - removed some sanity checks for backwards compatibility
    - 11: introduced: 26.10.2021, outdated since: -, not loadable since: -
        - chunk block data is now serialized via the network API, not the old storage API


    variable shared.STORAGE_VERSION
        the latest version, used for upgrading

    variable SAVE_DIRECTORY
        where the stuff should be saved

    class DataFixerNotFoundException extends Exception

    function register_storage_fixer(
            _, fixer: mcpython.common.world.datafixers.IDataFixer.IStorageVersionFixer
            ):

    function register_mod_fixer(
            _, fixer: mcpython.common.world.datafixers.IDataFixer.IModVersionFixer
            ):

    class SaveFile
        
        Interface to a stored file on the disk
        Used to load certain parts into the system & store them
        Contains the registries for data fixers


        variable storage_version_fixers

        variable mod_fixers

        variable storage_fixer_registry

        variable mod_fixer_registry

        variable group_fixer_registry

        variable part_fixer_registry

        function __init__(self, directory_name: str)
            
            Creates a new SaveFile object, normally not needed for the modder
            :param directory_name: the name of the directory


            variable self.directory

            variable self.version

            variable self.save_in_progress

        function region_iterator(self)
            
            Iterator iterating over ALL region files from a save file
            todo: can we cache this data somewhere?

            
            Async-loads all setup-data into the world using the default configuration for worlds


                    variable fixers

                        variable fixer
                            search for the one fixing to the nearest version to the searched for

                        variable fixer

                    variable self.version
            
            Save all base-data into the system
            :param _: used when used by special event triggers
            :param override: flag for saving the chunks


                variable self.save_in_progress
                    Make sure that nothing else is going on...

                variable shared.world_generation_handler.enable_generation

                    variable count

                variable shared.world_generation_handler.enable_generation
                    And open the system again

                variable self.save_in_progress
            
            Will apply a fixer to fix the storage version
            :param name: the name of the fixer to use
            :param args: the args to send
            :param kwargs: the kwargs to use
            :raises DataFixerNotFoundException: if the name is invalid


            variable fixer: mcpython.common.world.datafixers.IDataFixer.IStorageVersionFixer
            
            Will apply a group fixer to the system
            :param name: the name of the group fixer to use
            :param args: the args to use
            :param kwargs: the kwargs to use
            :raises DataFixerNotFoundException: if the name is invalid


            variable fixer: mcpython.common.world.datafixers.IDataFixer.IGroupFixer
            
            Will apply a part fixer to the system
            :param name: the name to use
            :param args: the args to send
            :param kwargs: the kwargs
            :raises DataFixerNotFoundException: if the name is invalid


            variable fixer: mcpython.common.world.datafixers.IDataFixer.IPartFixer
            
            Applies a mod fixer(list) to the system
            :param modname: the mod name
            :param source_version: where to start from
            :param args: args to call with
            :param kwargs: kwargs to call with
            :raises DataFixerNotFoundException: if the name is invalid


            variable instance

            variable fixers

                variable possible_fixers

                    variable fixer: mcpython.common.world.datafixers.IDataFixer.IModVersionFixer

                    variable fixer: mcpython.common.world.datafixers.IDataFixer.IModVersionFixer

                variable source_version

        static
        function _get_distance(cls, v, t)

        static
        function get_serializer_for(cls, part)
            
            Reads a part of the save-file
            :param part: the part to load
            :param kwargs: kwargs given to the loader
            :return: whatever the loader returns

            
            Similar to read(...), but the other way round.
            :param data: the data to store, optional, may be None
            :param part: the part to save
            :param kwargs: the kwargs to give the saver

            
            Access a saved json file
            :param file: the file to load
            :return: the data of the file or None if an error has occur


            variable file
            
            Access save a pickle file
            :param file: the file to load
            :return: the data of the file or None if an error has occurred


            variable file
            
            Access save a file in binary mode
            :param file: the file to load
            :return: the data of the file or None if an error has occurred


            variable file
            
            saves stuff with json into the system
            :param file: the file to save to
            :param data: the data to save


            variable file

            variable d

                variable data
            
            Saves stuff with pickle into the system
            :param file: the file to save to
            :param data: the data to save


            variable file

            variable d

                variable data
            
            saves bytes into the system
            :param file: the file to save to
            :param data: the data to save


            variable file

            variable d

        @deprecation.deprecated()
        function load_world(self)

        @deprecation.deprecated()
        function save_world(self, *_, override=False)

        @deprecation.deprecated()
        function apply_storage_fixer(self, name: str, *args, **kwargs)

        @deprecation.deprecated()
        function apply_group_fixer(self, name: str, *args, **kwargs)

        @deprecation.deprecated()
        function apply_part_fixer(self, name: str, *args, **kwargs)

        @deprecation.deprecated()
        function apply_mod_fixer(self, modname: str, source_version: tuple, *args, **kwargs)

        @deprecation.deprecated()
        function read(self, part, **kwargs)

        @deprecation.deprecated()
        function dump(self, data, part, **kwargs)

        @deprecation.deprecated()
        function access_file_json(self, file: str)

        @deprecation.deprecated()
        function access_file_pickle(self, file: str)

        @deprecation.deprecated()
        function access_raw(self, file: str)

        @deprecation.deprecated()
        function dump_file_json(self, file: str, data)

        @deprecation.deprecated()
        function dump_file_pickle(self, file: str, data)

        @deprecation.deprecated()
        function dump_raw(self, file: str, data: bytes)