***AbstractWorldGenerationModeConfigState.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class AbstractModeConfig
        
        Base class for a world generation mode config
        Serialize-able to save files


        static
        function deserialize(cls, data)

        function get_mode_instance(
                self,
                ) -> typing.Union[
                typing.Type[mcpython.server.worldgen.mode.IWorldGenConfig.IWorldGenConfig],
                mcpython.server.worldgen.mode.IWorldGenConfig.IWorldGenConfig,
                ]:
                """
                Helper function for creating an instance of a custom world gen config instance specific for this
                configuration.
                """
                raise NotImplementedError()
                
                def serialize(self):
            
            Helper function for creating an instance of a custom world gen config instance specific for this
            configuration.


        function serialize(self)

    class AbstractState extends mcpython.client.state.State.State,  ABC
        
        Base class for a configuration screen for a world generator mode
        todo: add sub-class with factory system
            -> data driven creation?


        function get_config_instance(self) -> AbstractModeConfig