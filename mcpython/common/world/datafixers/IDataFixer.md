***IDataFixer.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class IDataFixer extends mcpython.common.event.Registry.IRegistryContent

        variable FIXES_FROM

        variable FIXES_TO

        static
        function apply(cls, save_file, *args)

    class IStorageVersionFixer extends IDataFixer,  ABC
        
        Fixer for fixing an save from an old save format.
        Only implemented internally


        variable TYPE

        variable GROUP_FIXER_NAMES

    class IModVersionFixer extends IDataFixer,  ABC
        
        Fixer for another mod version. Can be used by mods to make old versions compatible.
        Used internally also for the core data.
        FIXES_FROM and FIXES_TO contain the mod versions.
        FIXES_FROM may be None if it should be applied when the mod gets added to the save file.
        FIXES_TO may be None if it is an cleanup-fixer


        variable TYPE

        variable MOD_NAME - the mod name to fix under

        variable GROUP_FIXER_NAMES

        variable PART_FIXER_NAMES

    class IGroupFixer extends IDataFixer,  ABC
        
        Fixer for an certain data group (e.g. the gamerule data or an chunk in the world).
        Mods can implement their own files in saves and use these to fix them


        variable TYPE

        variable PART_FIXER_NAMES

    class IPartFixer extends IDataFixer,  ABC
        
        Fixer for an part of an IGroupFixer. Certain files are able to contain data from different mods.
        Mods can register data fixers to fix their own data


        variable TYPE

        variable TARGET_SERIALIZER_NAME - the name of the fixer dedicated to these part

        static
        function apply(cls, save_file, *args, **kwargs)
            
            default implementation of the IPartFixer apply() calling apply_part_fixer(cls) on the SERIALIZER specified
            by TARGET_SERIALIZER_NAME
            Mods may want to override this method when doing other special stuff
