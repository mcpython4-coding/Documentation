***NetworkManager.py - documentation - last updated on 16.9.2021 by uuk***
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
            [1B package compression enable]
            [3B package size]
            [package data, encoded by the package]


        function __init__(self)

            variable self.custom_package_handlers

            variable self.general_package_handlers

            variable self.next_package_type_id

            variable self.next_package_id

            variable self.client_id

            variable self.valid_client_ids

            variable self.valid_package_ids
                Filled during handshake

            variable self.client_profiles

        function reset_package_registry(self)

        function get_dynamic_id_info(self) -> typing.List[typing.Tuple[str, int]]

        function set_dynamic_id_info(self, data: typing.List[typing.Tuple[str, int]])

                variable package_type

                variable package_id_here

                variable self.package_types[package_id]

                    variable self.general_package_handlers[

        function disconnect(self, target=-1)

        function send_package_to_all(self, package, not_including=-1)

        function send_package(
                self,
                package: mcpython.engine.network.AbstractPackage.AbstractPackage,
                destination: int = 0,
                ):

            variable data

        function encode_package(self, destination, package) -> bytes

            variable compress_data

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
                [mcpython.engine.network.AbstractPackage.AbstractPackage, int], None
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

            variable self.name2package_type[t.PACKAGE_NAME]

        function clean_network_graph(self)

        function fetch_as_client(self)

            variable buffer

                    variable package

                variable package.sender_id

        function fetch_as_server(self)

                    variable package.sender_id

        function fetch_package_from_buffer(self, buffer)

                variable package_type

                variable has_package_id

                variable has_previous_package_id

                variable index

                    variable package_id

                    variable package_id

                    variable previous_id

                    variable previous_id

                variable package_compressed

                variable package_size

                variable package_data

                    variable package_data

            variable buffer

            variable package

            variable package.package_id

    variable shared.NETWORK_MANAGER

    function load_packages()