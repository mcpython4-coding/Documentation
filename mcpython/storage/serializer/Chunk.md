***Chunk.py - documentation - last updated on 8.6.2020 by uuk***
___

    function chunk2region(cx, cz): return cx >> 5, cz >> 5
            
            
            @G.registry
            class Chunk(mcpython.storage.serializer.IDataSerializer.IDataSerializer):

    @G.registry class Chunk extends mcpython.storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function load(cls, savefile, dimension: int, chunk: tuple, immediate=False)

            variable G.worldgenerationhandler.enable_generation

            variable data

            variable chunk_instance.generated

            variable inv_file

                variable position

                variable d

                function add(blockinstance)

                variable flag

            variable positions

                variable biome_map

                    variable entity_instance

                variable entity_instance.rotation

                variable entity_instance.harts

            variable chunk_instance.loaded

            variable G.worldgenerationhandler.enable_generation

        static
        function save(cls, data, savefile, dimension: int, chunk: tuple, override=False)

                variable biome_map

                variable positions - an list of all (x, z) in the chunk, for sorting the arrays

                variable landmass_map

                variable cdata["maps"]["landmass_map"]

                variable cdata["maps"]["landmass_palette"]

                    variable mass

                        variable index

                        variable index

                variable biome_palette

                variable biomes

                        variable index

                        variable index

                variable cdata["maps"]["biome"]

                variable cdata["maps"]["biome_palette"]

                variable height_map

                variable cdata["maps"]["height"]

            variable data[chunk]

            variable G.worldgenerationhandler.enable_generation