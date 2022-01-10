***NetworkManager.py - documentation - last updated on 10.1.2022 by uuk***
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
        todo: move the mcpython specific methods to another util module


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

            variable self.playername2connectionID
            
            Creates a chunk request package to be sent to the server
            :param chunk: the chunk to get data for

            
            Helper function for displaying a message in a player chat
            :param player: the player name or the client id
            :param msg: the message itself
            :raises AssertionError: if the message is not a string


                variable player

        function reset_package_registry(self)
            
            Resets the internal package registry system to being empty
            Used only in unit tests to make sure that we are in a known state


        function get_dynamic_id_info(self) -> typing.Iterator[typing.Tuple[str, int]]
            
            Creates the dynamic id info data, storing the package ids set by the NetworkManager at runtime,
            so multiple sources are safe to register packages, without conflicts

            
            Helper function for writing the dynamic id info data created by get_dynamic_id_info()
            Will set the package ids as needed
            :param data: the data


            variable reassign

            variable assigned

                variable package_type

                variable package_id_here

                variable self.package_types[package_id]

                    variable self.general_package_handlers[

                variable previous

                variable package_class.PACKAGE_TYPE_ID

                variable self.package_types[package_class.PACKAGE_TYPE_ID]
            
            Disconnection helper, does send the disconnection package
            :param target: which one to disconnect, -1 to all directly connected (server: all, client: server)

            
            Sends a package to all clients in the network, excluding the given client id
            :param package: the package to send
            :param not_including: which client id to not include, or -1 if no one should be skipped
            :raises RuntimeError: if the package has no package ID, so no static id nor registered to a NetworkManager
                instance


            variable destination: int
            
            Sends the given package over the network to the target PC
            :param package: the package to send
            :param destination: the destination to send to, 0 is server, and clients are starting at 1
            :raises RuntimeError: if the package has no package ID, so no static id nor registered to a NetworkManager
                instance
            :raises ValueError: if the destination is 0, and we are on the server


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
            
            Registers a handler to be invoked when a certain package is received
            :param package_type: the package type to look for
            :param handler: the handler


        function register_answer_handler(
                self,
                previous_package: mcpython.engine.network.AbstractPackage.AbstractPackage,
                handler: typing.Callable[
                [mcpython.engine.network.AbstractPackage.AbstractPackage, int], None
                ],
                ):
            
            Registers a handler for when an answer is received for a given package
            :param previous_package: the package to wait for
            :param handler: the handler method


        function register_package_type(
                self,
                package_class: typing.Type[
                mcpython.engine.network.AbstractPackage.AbstractPackage
                ],
                ):
            
            Registers a certain package class to this network manager
            :param package_class: the class to register


                variable package_class.DYNAMIC_PACKAGE_ID

                variable package_class.PACKAGE_TYPE_ID

                variable other

                variable self.package_types[self.next_package_type_id]

            variable self.package_types[package_class.PACKAGE_TYPE_ID]

            variable self.name2package_type[package_class.PACKAGE_NAME]
            
            Util method invoked on the client to fetch data from the socket and handle it


            variable buffer

                    variable package

                variable package.sender_id

                        variable result

                        variable result
            
            Util method invoked on the server to fetch data from the socket and handle it


                variable buffer

                        variable package

                    variable package.sender_id

                            variable result

                            variable result

        function clean_network_graph(self)
            
            Cleans some internal stuff

            
            Encodes the given package to bytes
            :param destination: where to send to
            :param package: the package to encode
            :return: the bytes representing the package
            :raises RuntimeError: if the package has no package ID, so no static id nor registered to a NetworkManager
                instance


            variable buffer

            variable package.target_id

                variable package.package_id

            variable pbuf

            variable package_data

            variable compress_data

                variable package_data
            
            Reads a package from the network buffer instance
            :param buffer: the buffer to read from
            :param log_package_error: if to log errors with the package, or to silently ignore them
            :return: the package instance, or None if an error occurred


                    variable package_type

                    variable package_id

                    variable package_id

                    variable previous_ids

                    variable previous_ids

                variable package_compressed

                variable package_data

                    variable package_data

            variable buffer

            variable package

            variable package.package_id

            variable package.previous_packages

    variable shared.NETWORK_MANAGER