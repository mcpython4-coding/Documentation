***SaveFile.py - documentation - last updated on 3.7.2020 by uuk***
___

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
    - 1: introduced: 07.03.2020, outdated since: 10.03.2020, not loadable since: -
        - added save system
    - 2: introduced: 10.03.2020, outdated since: 13.03.2020, not loadable since: -
        - removed temperature maps from saves
        - optimized landmass map in saves
    - 3: introduced: 13.03.2020 [part of loot table update], outdated since: 31.03.2020, not loadable since: -
        - chest container stores now also the loot table link when set
    - 4: introduced: 31.03.2020, outdated since: -, not loadable since: -
        - block coordinates are stored now relative to chunk; decreases chunk size
    - 5: introduced: 17.03.2020 [part of entity update], outdated since: 11.06.2020, not loadable since: -
        - added entity serializer
    - 6: introduced: 11.06.2020, outdated since: -, not loadable since: -
        - re-write of data fixer system, old still fix-able
        - removed "version"-attribute out of region files and inventory files
        - data fixers are applied to the WHOLE world ON LOAD, not when needed


    variable G.STORAGE_VERSION - the latest version, used for upgrading

    variable SAVE_DIRECTORY
        where the stuff should be saved

    class DataFixerNotFoundException extends Exception

    function register_storage_fixer(_, fixer: mcpython.storage.datafixers.IDataFixer.IStorageVersionFixer)

    function register_mod_fixer(_, fixer: mcpython.storage.datafixers.IDataFixer.IModVersionFixer)

    class SaveFile
        
        Interface to an stored file on the disk
        Used to load certain parts into the system & store them


        variable storage_version_fixers

        variable mod_fixers

        variable storage_fixer_registry

        variable mod_fixer_registry

        variable group_fixer_registry

        variable part_fixer_registry

        function __init__(self, directory_name: str)
            
            Creates an new SaveFile object
            :param directory_name: the name of the directory


            variable self.directory

            variable self.version

            variable self.save_in_progress

        function region_iterator(self)
            
            Iterator iterating over ALL region files from an save file


        function load_world(self)
            
            loads all setup-data into the world


        function save_world(self, *_, override=False)
            
            save all base-data into the system
            :param _: used when used by special event triggers
            :param override: flag for saving the chunks


        function apply_storage_fixer(self, name: str, *args, **kwargs)
            
            will apply an fixer to fix the storage version
            :param name: the name of the fixer to use
            :param args: the args to send
            :param kwargs: the kwargs to use
            :raises DataFixerNotFoundException: if the name is invalid


        function apply_group_fixer(self, name: str, *args, **kwargs)
            
            will apply an group fixer to the system
            :param name: the name of the group fixer to use
            :param args: the args to use
            :param kwargs: the kwargs to use
            :raises DataFixerNotFoundException: if the name is invalid


        function apply_part_fixer(self, name: str, *args, **kwargs)
            
            will apply an part fixer to the system
            :param name: the name to use
            :param args: the args to send
            :param kwargs: the kwargs
            :raises DataFixerNotFoundException: if the name is invalid


        function apply_mod_fixer(self, modname: str, source_version: tuple, *args, **kwargs)
            
            applies an mod fixer(list) to the system
            :param modname: the mod name
            :param source_version: where to start from
            :param args: args to call with
            :param kwargs: kwargs to call with
            :raises DataFixerNotFoundException: if the name is invalid


                    variable fixer: mcpython.storage.datafixers.IDataFixer.IModVersionFixer

                    variable fixer: mcpython.storage.datafixers.IDataFixer.IModVersionFixer

                variable source_version

        static
        function _get_distance(cls, v, t)

        static
        function get_serializer_for(cls, part)

        function read(self, part, **kwargs)
            
            reads an part of the save-file
            :param part: the part to load
            :param kwargs: kwargs given to the loader
            :return: whatever the loader returns


        function dump(self, data, part, **kwargs)
            
            similar to read(...), but the other way round.
            :param data: the data to store, optional, may be None
            :param part: the part to save
            :param kwargs: the kwargs to give the saver


        function access_file_json(self, file: str)
            
            access save an json file
            :param file: the file to load
            :return: the data of the file or None if an error has occur


        function access_file_pickle(self, file: str)
            
            access save an pickle file
            :param file: the file to load
            :return: the data of the file or None if an error has occur


        function access_raw(self, file: str)
            
            access save an file in binary mode
            :param file: the file to load
            :return: the data of the file or None if an error has occur


        function dump_file_json(self, file: str, data)
            
            saves stuff with json into the system
            :param file: the file to save to
            :param data: the data to save


        function dump_file_pickle(self, file: str, data)
            
            saves stuff with pickle into the system
            :param file: the file to save to
            :param data: the data to save


        function dump_raw(self, file: str, data: bytes)
            
            saves bytes into the system
            :param file: the file to save to
            :param data: the data to save


        @deprecation.deprecated("dev3-1", "a1.3.0")
        function upgrade(self, **kwargs)

    @G.modloader("minecraft", "stage:datafixer:general")
    function load_elements()