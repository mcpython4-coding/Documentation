***Backend.py - documentation - last updated on 9.2.2022 by uuk***
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


        function __init__(self, ip="127.0.0.1", port=8088)

            variable self.socket: typing.Optional[socket.socket]

            variable self.scheduled_packages

            variable self.data_stream

            variable self.connected

        function connect(self) -> bool

            variable self.socket

            variable self.connected

            variable shared.IS_NETWORKING

        function disconnect(self)

            variable self.connected

            variable shared.IS_NETWORKING

        function work(self)

            variable packages

                    variable d

    class ServerBackend
        
        Server network handler
        Contains threading code for each client


        function __init__(self, ip="0.0.0.0", port=8088)

            variable self.socket

            variable self.scheduled_packages_by_client

            variable self.data_by_client

            variable self.server_handler_thread

            variable self.pending_stops

            variable self.next_client_id

            variable self.threads

            variable self.pending_thread_stops

            variable self.handle_lock

        function disconnect_client(self, client_id: int)

        function disconnect_all(self)

            variable client_ids

        function get_package_streams(self)

        function connect(self)

        function enable_server(self)

            variable shared.IS_NETWORKING

        function inner_server_thread(self)

                variable client_id

                variable shared.NETWORK_MANAGER.client_profiles[client_id]

                variable self.data_by_client[client_id]

                variable self.client_locks[client_id]

                variable recv_thread

                variable send_thread

                variable self.threads[client_id]

        function single_client_thread_recv(self, conn, client_id: int)

        function single_client_thread_send(self, conn, client_id: int)

                    variable packages