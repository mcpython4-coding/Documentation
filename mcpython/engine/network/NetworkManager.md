***NetworkManager.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NetworkManager
        
        THE network manager
        Abstracts packages away from the end user
        Destinations are no longer "addresses", they are ID's, where 0 is the server and players start at 1
        Data to transmit is now hold in "Packages", encoded in the following way:
            [3B-2Bi package type id][1Bi has id, 1Bi has answer id]
            [4B package id, if answering or answer is expected]
            [4B previous package id, if answer]
            [3B package size]
            [package data, encoded by the package]


        function __init__(self)

            variable self.next_package_type_id

            variable self.next_package_id

            variable self.client_id

            variable self.valid_package_ids
                Filled during handshake

        function send_package(
                self,
                package: mcpython.engine.network.AbstractPackage.AbstractPackage,
                destination: int = 0,
                ):

            variable encoded_head

                variable package.package_id

            variable package_id_data

            variable previous_package_id_data

            variable package_data

            variable package_size_data

            variable data

        function register_package_handler(
                self,
                package_type: typing.Type[
                mcpython.engine.network.AbstractPackage.AbstractPackage
                ],
                handler: typing.Callable[
                [mcpython.engine.network.AbstractPackage.AbstractPackage], None
                ],
                ):

        function register_answer_handler(
                self,
                previous_package: mcpython.engine.network.AbstractPackage.AbstractPackage,
                handler: typing.Callable[
                [mcpython.engine.network.AbstractPackage.AbstractPackage], None
                ],
                ):

        function register_package_type(
                self,
                t: typing.Type[mcpython.engine.network.AbstractPackage.AbstractPackage],
                ):

                variable t.DYNAMIC_PACKAGE_ID

                variable t.PACKAGE_TYPE_ID

                variable other

                variable self.package_types[self.next_package_type_id]

            variable self.package_types[t.PACKAGE_TYPE_ID]

        function clean_network_graph(self)

        function fetch_as_client(self)

                variable package

        function fetch_as_server(self)

                variable package

        function fetch_package_from_buffer(self, buffer)

                variable package_type

                variable has_package_id

                variable has_previous_package_id

                variable index

                    variable package_id

                    variable package_id

                    variable previous_id

                    variable previous_id

                variable package_size

                variable package_data

            variable package: mcpython.engine.network.AbstractPackage.AbstractPackage

            variable package.package_id

    variable shared.NETWORK_MANAGER