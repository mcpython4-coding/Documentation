***WorldGenerationTaskArrays.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class WorldGenerationTaskHandler
        
        handler for generating tasks off-call
        todo: make task work more efficient!!!


        function __init__(self)

            variable self.chunks: typing.Set[mcpython.common.world.AbstractInterface.IChunk]

            variable self.data_maps - invoke, world_changes, shown_updates

        function get_total_task_stats(self) -> list
            
            will return the sum of all tasks of the whole system, in invoke, world_changes and shown_updates separated


        function get_task_count_for_chunk(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk
                ) -> int:
            
            gets the total count of tasks for an given chunk as an int
            :param chunk:
            :return:


            variable dim

            variable p

            variable count

        function schedule_invoke(
                self,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                method,
                *args,
                **kwargs
                ):
            
            schedules an callable-invoke for the future
            :param chunk: the chunk to link to
            :param method: the method to call
            :param args: the args to call with
            :param kwargs: the kwargs to call with


        function schedule_block_add(
                self,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                position: tuple,
                name: str,
                *args,
                on_add=None,
                **kwargs
                ):
            
            schedules an addition of an block
            :param chunk: the chunk the block is linked to
            :param position: the position of the block
            :param name: the name of the block
            :param args: the args to send to the add_block-method
            :param on_add: an callable called together with the block instance when the block is added
            :param kwargs: the kwargs send to the add_block-method


            variable kwargs["immediate"]

            variable self.data_maps[1].setdefault(chunk.get_dimension().get_id(),

        function schedule_block_remove(
                self,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                position: tuple,
                *args,
                on_remove=None,
                **kwargs
                ):
            
            schedules an removal of an block
            :param chunk: the chunk the block is linked to
            :param position: the position of the block
            :param args: the args to call the remove_block-function with
            :param on_remove: an callable to call when the block gets removed, with None as an parameter
            :param kwargs: the kwargs to call the remove_block-function with


            variable self.data_maps[1].setdefault(chunk.get_dimension().get_id(),

        function schedule_block_show(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk, position: tuple
                ):
            
            schedules an show of an block
            :param chunk: the chunk
            :param position: the position of the block


            variable self.data_maps[2].setdefault(chunk.get_dimension().get_id(),

        function schedule_block_hide(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk, position: tuple
                ):
            
            schedules an hide of an block
            :param chunk: the chunk
            :param position: the position of the block


            variable self.data_maps[2].setdefault(chunk.get_dimension().get_id(),

        function schedule_visual_update(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk, position: tuple
                ):
            
            schedules an visual update of an block (-> show/hide as needed)
            :param chunk: the chunk
            :param position: the position of the block


            variable self.data_maps[2].setdefault(chunk.get_dimension().get_id(),

        function process_one_task(self, chunk=None, log_msg=False) -> int
            
            processes one task from an semi-random chunk or an given one
            :param chunk: the chunk or None to select one
            :param log_msg: if messages for extra info should be logged


        function process_tasks(self, chunks=None, timer=None)
            
            process tasks
            :param chunks: if given, an iterable of chunks to generate
            :param timer: if given, an float in seconds to determine how far to generate


        function _process_0_array(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk
                ) -> bool:

                variable dim_map

                    variable m: list

                    variable data

        function _process_1_array(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk
                ) -> bool:

                variable dim_map

                    variable m: dict

                        variable block

        function _process_2_array(
                self, chunk: mcpython.common.world.AbstractInterface.IChunk
                ) -> bool:

                variable dim_map

                    variable m: dict

                    variable block

        function get_block(
                self, position: tuple, chunk: mcpython.common.world.AbstractInterface.IChunk
                ):
            
            gets an generated block from the array
            :param position: the position of the block
            :param chunk: if the chunk is known


            variable dimension

        function clear_chunk(self, chunk: mcpython.common.world.AbstractInterface.IChunk)
            
            will remove all scheduled tasks from an given chunk
            :param chunk: the chunk


        function clear(self)
            
            will remove all scheduled tasks [chunk-wise]


    class IWorldGenerationTaskHandlerReference

        function schedule_invoke(self, method, *args, **kwargs)

        function schedule_block_add(self, position, name, *args, on_add=None, **kwargs)

        function schedule_block_remove(self, position, *args, on_remove=None, **kwargs)

        function schedule_block_show(self, position)

        function schedule_block_hide(self, position)

        function schedule_visual_update(self, position)

        function get_block(self, position, chunk=None)

        function get_block_name(self, position, chunk=None)

        function fill_area(
                self,
                start: typing.Tuple[int, int, int],
                end: typing.Tuple[int, int, int],
                block,
                only_non_air=False,
                **kwargs
                ):

        function fill_area_inner_outer(
                self,
                start: typing.Tuple[int, int, int],
                end: typing.Tuple[int, int, int],
                inner_block,
                outer_block,
                only_non_air=False,
                inner_config=None,
                outer_config=None,
                ):

        function replace_air_and_liquid_downwards(self, block, x, y, z, delta, liquids)

        function get_biome_at(self, x, z) -> str

    class WorldGenerationTaskHandlerReference extends IWorldGenerationTaskHandlerReference
        
        reference class to an WorldGenerationTaskHandler for setting the chunk globally
        all scheduling functions are the same of WorldGenerationTaskHandler exept the chunk-parameter is missing.
        It is set on construction


        function __init__(
                self,
                handler: WorldGenerationTaskHandler,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                ):

            variable self.handler

            variable self.chunk

        function schedule_invoke(self, method, *args, **kwargs)

        function schedule_block_add(self, position, name, *args, on_add=None, **kwargs)

        function schedule_block_remove(self, position, *args, on_remove=None, **kwargs)

        function schedule_block_show(self, position)

        function schedule_block_hide(self, position)

        function schedule_visual_update(self, position)

        function get_block(self, position, chunk=None)

        function get_biome_at(self, x, z) -> str

    class OffProcessTaskHelper

        class OffProcessTaskHelperShared

            function __init__(
                    self, reference: "ProcessSeparatedWorldGenerationTaskHandlerReference"
                    ):

                variable self.running

                variable self.reference

                variable self.task_queue

                variable self.task_data_out

            function run(self)

        function __init__(self, chunk)

            variable self.chunk

            variable self.shared

            variable self.process

        function stop(self)

        function run_main(
                self,
                manager: "RemoteTaskHandlerManager",
                default: WorldGenerationTaskHandlerReference,
                ):

                    variable on_add

                    variable on_remove

                    variable position

        function run_layer_generation(self, layer, config)

    class RemoteTaskHandlerManager

        function __init__(self)

        function create(
                self,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                default: WorldGenerationTaskHandlerReference,
                ) -> typing.Tuple[
                "ProcessSeparatedWorldGenerationTaskHandlerReference", OffProcessTaskHelper
                ]:
                helper_instance = OffProcessTaskHelper(chunk)
                array_instance = ProcessSeparatedWorldGenerationTaskHandlerReference(
                helper_instance.shared, chunk.as_shareable()
                )
                helper_instance.reference = array_instance
                self.references.append((helper_instance, array_instance, default))
                return array_instance, helper_instance
                
                def tick(self):

            variable helper_instance

            variable array_instance

            variable helper_instance.reference

        function tick(self)

    class ProcessSeparatedWorldGenerationTaskHandlerReference extends  IWorldGenerationTaskHandlerReference 
        
        Reference class to an WorldGenerationTaskHandler for setting the chunk globally
        all scheduling functions are the same of WorldGenerationTaskHandler except the chunk-parameter is missing.
        It is set on construction
        WARNING: does need an assigned group of RemoteTaskHandlerReference and OffProcessTaskHelper to work correctly.
        Use RemoteTaskHandlerManager.create(<chunk>, <reference>) returning this object and an assigned OffProcessTaskHelper instance
        ready to go


        function __init__(
                self,
                shared_helper: OffProcessTaskHelper.OffProcessTaskHelperShared,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                ):

            variable self.shared_helper

            variable self.chunk

            variable self.tasks

        function schedule_invoke(self, method, *args, force_main=False, **kwargs)

        function schedule_block_add(self, position, name, *args, on_add=None, **kwargs)

        function schedule_block_remove(self, position, *args, on_remove=None, **kwargs)

        function schedule_block_show(self, position)

        function schedule_block_hide(self, position)

        function schedule_visual_update(self, position)

        function get_block(self, position: tuple, chunk=None)

        function execute_tasks(self)

        function get_biome_at(self, x, z) -> str