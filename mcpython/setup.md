***setup.py - documentation - last updated on 8.7.2020 by uuk***
___

    WARNING: the system is outdated and will likely be removed in the future
    what does this system do?
        as mentioned in #1 (may be closed when you read this), game loading takes / have taken for some reasons on some
            devices very long (in #1: 30 minutes).
        These file tries to fix this problem by adding an system which generates before the game is started by the user
            (or on his first start in an new downloaded folder) the things from different parts of the game which can be
            prepared before the game starts (texture atlases, file transformations, texture editing, ...) in an separated
            folder. Access to the prepared data is organized by index files.
        What happens if the user adds some data into the game?
            The system is not generating during runtime anymore. To update the data, run program with --invalidate-cache or import
            the __main__ file and the setup file and call the functions by hand
        What happens if an mod loader should be added?
            Have a look what is done to generate the vanilla things. Try to give the mod an interface for generating things.
            Rerun mod specified and vanilla-adapting tasks when the mod with the given version was run first. Afterwards,
            only access the prepared data. 


    class IPrepareAbleTask extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable USES_DIRECTORY

    variable taskregistry

    function add()

            static
            function dump_data(directory: str)

            variable USES_DIRECTORY

        @G.registry class TextureFactoryGenerate extends IPrepareAbleTask

            variable NAME

            static
            function dump_data(directory: str)

            variable USES_DIRECTORY

    function execute()

        variable G.invalidate_cacheing

        variable G.data_gen

            variable data

            variable G.invalidate_cacheing

            variable G.data_gen