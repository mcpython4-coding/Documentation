***AbstractPackage.py - documentation - last updated on 19.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractPackage
        
        Base class for network packages
        A package may have a static or dynamic ID. Dynamic ids are given on the fly,
        static ones are checked at registration time.
        A package does not need to be arrival on both sides of a network. Each network manager holds
        a list of valid package id's, other ones will be ignored


        variable PACKAGE_NAME: typing.Optional[str]
            A unique package name, used during handshake for package type comparison
            Can include version of the package

        variable PACKAGE_TYPE_ID
            Set this to a meaningful int when needed

        variable DYNAMIC_PACKAGE_ID
            DO NOT TOUCH!

        variable CAN_GET_ANSWER

        function __init__(self)

            variable self.package_id - set during send process

            variable self.previous_packages - set only during receiving or calling answer()

        function send(self, destination=0)

        function on_answer_received(self, package)

        function encode(self) -> bytes

        static
        function from_data(cls, package_data: bytes)

        function answer(self, package: "AbstractPackage")

            variable package.previous_packages

        function handle_inner(self)