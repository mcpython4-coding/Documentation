***AbstractCapability.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractCapability
        
        Class representing a certain capability
        attach() returning the data to write into the buffer when the capability is first looked up
        rawRead() and rawWrite() for the described actions in saves
        copyOver() for transforming the data (written afterwards into cache if not None) and doing other stuff,
            may not be attach()-ed at the target
        prepareData() for returning a viewable form of the capability, when needed


        variable NAME

        variable ACCEPTED_CONTAINERS: typing.Set[str]

        variable SHOULD_BE_SAVED

        static
        function attach(cls, body: ICapabilityContainer)

        static
        function rawRead(cls, body: ICapabilityContainer, data) -> typing.Any

        static
        function rawWrite(cls, body: ICapabilityContainer, data) -> typing.Any

        static
        function copyOver(
                cls, source_body: ICapabilityContainer, target_body: ICapabilityContainer, data
                ):

        static
        function prepareData(cls, body: ICapabilityContainer, data)