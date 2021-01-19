***AbstractPackage.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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