***Backend.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ClientBackend
        
        The backend of the client
        It wraps the socket in a set of helper functions


        function __init__(self, ip="localhost", port=8080)

            variable self.socket

            variable self.scheduled_packages

            variable self.data_stream

        function send_package(self, data: bytes)

        function connect(self)

        function work(self)

                variable d

    class ServerBackend
        
        Server network handler
        Contains threading code for each client


        function __init__(self, ip="0.0.0.0", port=8080)

            variable self.socket

            variable self.scheduled_packages

            variable self.data_by_client

            variable self.server_handler_thread

            variable self.pending_stops

        function send_package(self, data: bytes, client: int)

        function connect(self)

        function enable_server(self)

        function inner_server_thread(self)

                variable self.data_by_client[addr]

                variable thread

        function single_client_thread(self, conn, addr, client_id: int)