***abstract.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractReloadListener extends ABC

        variable NAME

        variable DEPENDS_ON
            
            Invoked when it is time to load resources
            :param is_first_load: indicates if this is the first resource load or not


        static
        function on_unload(cls)
            
            Invoked before a reload, to delete all previous resources or do some fancy stuff with them


        static
        function on_bake(cls)
            
            Invoked after most of the stuff is loaded


    class AbstractFileWalkingReloadListener extends AbstractReloadListener,  ABC

        variable PATTERN: typing.Optional[re.Pattern]

        variable SPECIAL_WALK

        variable DIRECTORY

                variable entries

                variable entries

        static
        function load_file(cls, file: str, is_first_load=False)
            
            Similar to on_reload, but it invoked for each matching file
            :param file: the file to load
            :param is_first_load: same as in on_reload


    class AbstractFileWalkingReloadListenerInstanceBased extends AbstractReloadListener,  ABC

        function __init__(self)

            variable self.PATTERN: typing.Optional[re.Pattern]

            variable self.SPECIAL_WALK

            variable self.DIRECTORY

                variable entries

                variable entries
            
            Similar to on_reload, but it invoked for each matching file
            :param file: the file to load
            :param is_first_load: same as in on_reload


        function on_unload(self)

        function on_bake(self)