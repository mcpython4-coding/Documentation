***HandShakePackage.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Client2ServerHandshake extends AbstractPackage
        
        Package to be send from the client to the server on connection


        variable CAN_GET_ANSWER

        variable PACKAGE_TYPE_ID

        variable PACKAGE_NAME

        function __init__(self)

            variable self.game_version

            variable self.player_name

        function setup(self, player_name: str)

        function read_from_buffer(self, buffer: ReadBuffer)

        function write_to_buffer(self, buffer: WriteBuffer)

        function handle_inner(self)

            variable shared.NETWORK_MANAGER.client_profiles.setdefault(self.sender_id,

            variable shared.NETWORK_MANAGER.playername2connectionID[

    class Server2ClientHandshake extends AbstractPackage
        
        The package send from the server back to the client
        Contains some meta information


        variable PACKAGE_TYPE_ID

        variable PACKAGE_NAME

        function __init__(self)

            variable self.accept_connection

            variable self.deny_reason

        function setup_deny(self, reason: str)

        function setup_accept(self)

            variable self.mod_list

        function read_from_buffer(self, buffer: ReadBuffer)

                variable self.deny_reason

            variable self.mod_list

        function write_to_buffer(self, buffer: WriteBuffer)

        function handle_inner(self)

            variable miss_matches