***WorldGenerationHandler.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class WorldGenerationHandler
        
        Main handler instance for world generation
        Stored data for world generation and handles requests for generating chunks


        variable CHUNK_GENERATOR_VERSION

        function __init__(self)

            variable self.configs
                a config table: dimension name -> config list

            variable self.enable_generation
                if world gen should be enabled

            variable self.enable_auto_gen
                if chunks around the player should be generated when needed

            variable self.task_handler
                the general task handler instance

            variable self.feature_registry
                the feature registry, replacing old dict stored here
                has some fancier internals :-)

            variable self.chunk_maps

        function setup_chunk_maps(self, chunk: mcpython.engine.world.AbstractInterface.IChunk)

        function register_chunk_map(
                self,
                chunk_map: typing.Type[
                mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap
                ],
                ):

            variable self.chunk_maps[chunk_map.NAME]

            variable version

                variable name

                variable dim_data

            variable data

        function add_chunk_to_generation_list(
                self,
                chunk: mcpython.engine.world.AbstractInterface.IChunk,
                dimension=None,
                force_generate=False,
                immediate=False,
                ):
            
            Adds chunk schedule to the system
            Will set the loaded-flag of the chunk during the process
            Will schedule the internal inner_add_chunk function
            :param chunk: the chunk
            :param dimension: optional: if chunk is tuple, and another dimension than the active one should be used
            :param force_generate: if generation should take place also when auto-gen is disabled
            :param immediate: if inner_add_chunk should be called immediate or not [can help in cases where TaskHandler stops
                running tasks when in-generation progress]


                    variable chunk
                        todo: is there something better than this / remove this

                    variable chunk

            variable chunk.loaded

        function inner_add_chunk(self, chunk: mcpython.engine.world.AbstractInterface.IChunk)
            
            internal implementation of the chunk generation code
            :param chunk: the chunk to schedule


            variable config

            variable reference

                    variable config

                    variable config

        function setup_dimension(
                self, dimension: mcpython.engine.world.AbstractInterface.IDimension, config=None
                ):
            
            Sets up the layer configs for the given dimension
            :param dimension: the dimension to use
            :param config: optional additional dict specifying LayerConfig's


            variable config_name

                    variable layer_name

                    variable layer_config

                variable layer

                    variable layer_config

                    variable layer_config.dimension

                    variable layer_config

                variable layer_config.world_generator_config

                variable layer_config.layer

            variable dimension
            
            Generates the chunk in-place
            :param chunk: the chunk, as an instance, or a tuple
            :param dimension: if tuple, specifies the dimension. When still None, the active dimension is used
            todo: add flag to override any data, not only add additional if the chunk exists


                variable chunk

        function get_current_config(
                self, dimension: mcpython.engine.world.AbstractInterface.IDimension
                ):
            
            Helper method for getting the the world generation configuration for a given dimension
            :param dimension: the dimension instance
            todo: allow string and similar


            variable config_name

        function set_current_config(
                self, dimension: mcpython.engine.world.AbstractInterface.IDimension, config: str
                ):
            
            Writes a config name as the given into an dimension object
            :param dimension: the dimension
            :param config: the config name

            
            Internal helper for marking a chunk as finished. Will call the needed events.
            :param chunk: the chunk instance


            variable config_name

            variable config

        function register_layer(
                self, layer: typing.Type[mcpython.server.worldgen.layer.ILayer.ILayer]
                ):
            
            Registers a new layer object into the system
            :param layer: the layer instance
            todo: make more fancy


            variable self.layers[layer.NAME]

        function register_world_gen_config(self, instance)

        function unregister_world_gen_config(self, instance)

        function get_world_gen_config(self, dimension: str, name: str)

        function __call__(
                self,
                data: typing.Type[mcpython.server.worldgen.layer.ILayer.ILayer],
                ):

    variable shared.world_generation_handler