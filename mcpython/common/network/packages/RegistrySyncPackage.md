***RegistrySyncPackage.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class RegistrySyncInitPackage extends AbstractPackage
        
        Sync init package send during the Server2ClientHandshake-handle
        Send client -> server


        variable PACKAGE_NAME

        function __init__(self)

            variable self.registries

        function setup(self)

        function read_from_buffer(self, buffer: ReadBuffer)

        function write_to_buffer(self, buffer: WriteBuffer)

        function handle_inner(self)

                variable registry

                variable package

    class RegistrySyncPackage extends AbstractPackage
        
        Package send server -> client as a response on the RegistrySyncInitPackage
        Send for each requested registry


        variable PACKAGE_NAME

        function __init__(self)

            variable self.content

            variable self.name

        function setup(self, name: str)

        function read_from_buffer(self, buffer: ReadBuffer)

        function write_to_buffer(self, buffer: WriteBuffer)

        function handle_inner(self)

    class RegistrySyncResultPackage extends AbstractPackage

        variable PACKAGE_NAME

        variable CAN_GET_ANSWER

        function __init__(self)

            variable self.name

            variable self.status

        function setup(self, name: str, status: bool)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

        function handle_inner(self)

                        function handle(*_)

                        variable package

            variable shared.NETWORK_MANAGER.client_profiles[self.sender_id]["registry_sync"][