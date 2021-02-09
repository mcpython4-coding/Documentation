***AbstractPackage.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractPackage extends ABC

        variable PACKAGE_ID - set only to an positive value if you know what you are doing!

        variable ASSIGNED_CHANNEL: str - the channel instance name to send over

        static
        function decode_package(cls, stream) -> "AbstractPackage"

        function __init__(self)

            variable self.package_number

            variable self.response_stack

        function respond(self, package: "AbstractPackage")

        function serialize(self) -> bytes