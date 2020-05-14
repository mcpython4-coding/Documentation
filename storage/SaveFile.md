***SaveFile.py - documentation - last updated on 14.5.2020 by uuk***
___

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
    - 5: introduced: 17.03.2020 [part of entity update], outdated since: -, not loadable since: -
        - added entity serializer
    
    planned:
    - 6: introduced: -, outdated since: -, not loadable since: -
        - changed how block-inventories are stored
        - optimisations to chunk-accessing
        - introduced datafixer system for mods; introduced block-fixers
        
        data structure changes:
            Region: add last_loaded-parameter
            Chunk: add unapplied_fixers-list for storing which fixers to apply when loaded
            General: add an list of data-fixers applied to the world in the time of live of the world
    


    variable LATEST_VERSION


    variable G.STORAGE_VERSION


    variable SAVE_DIRECTORY


    class SaveFile
        function __init__(self, directory_name)
        function load_world(self)

                    variable generaldatafixer


                    variable self.version

        function save_world(self, *_, override=False)
        function upgrade(self, part=None, version=None, to=None, **kwargs)
            
            upgrades the part of the SaveFile to the latest version supported
            :param part: the part to update, or None, if all should upgrade
            :param kwargs: kwargs given to the fixers
            :param version: which version to upgrade from
            :param to: to which version to upgrade to
            

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
            

        function access_file_json(self, file)
        function access_file_pickle(self, file)
        function access_raw(self, file)
        function dump_file_json(self, file, data)
        function dump_file_pickle(self, file, data)
        function dump_raw(self, file, data)