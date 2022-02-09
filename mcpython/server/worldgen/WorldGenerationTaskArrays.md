***WorldGenerationTaskArrays.py - documentation - last updated on 9.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class WorldGenerationTaskHandler
        
        Handler for generating tasks in preparation for off-thread [like MC] & off-process generation
        [even more efficient when correctly implemented]
        todo: make task work more efficient, even without


        function __init__(self)

            variable self.chunks: weakref.WeakSet[IChunk]

            variable self.data_maps - invoke, world_changes, shown_updates

        function get_total_task_stats(self) -> list
            
            Will return the sum of all tasks of the whole system, in invoke, world_changes and shown_updates separated


        function get_task_count_for_chunk(
                self, chunk: IChunk
                ) -> int:
            
            Gets the total count of tasks for a given chunk as an int
            :param chunk: the chunk instance to get the task count for


            variable dim

            variable p

            variable count

        function schedule_invoke(
                self,
                chunk: IChunk,
                method: typing.Callable | typing.Awaitable,
                *args,
                **kwargs,
                ):
            
            Schedules a callable-invoke for the future or an 'await' on a coroutine
            :param chunk: the chunk to link to
            :param method: the method to call
            :param args: the args to call with
            :param kwargs: the kwargs to call with


        function schedule_block_add(
                self,
                chunk: IChunk,
                position: typing.Tuple[int, int, int],
                name: str,
                *args,
                on_add=None,
                **kwargs,
                ):
            
            Schedules an addition of a block
            :param chunk: the chunk the block is linked to
            :param position: the position of the block
            :param name: the name of the block
            :param args: the args to send to the add_block-method
            :param on_add: a callable called together with the block instance when the block is added
            :param kwargs: the kwargs send to the add_block-method


            variable kwargs["immediate"]

        function schedule_block_remove(
                self,
                chunk: IChunk,
                position: typing.Tuple[int, int, int],
                *args,
                on_remove=None,
                **kwargs,
                ):
            
            Schedules the removal of a block
            :param chunk: the chunk the block is linked to
            :param position: the position of the block
            :param args: the args to call the remove_block-function with
            :param on_remove: a callable to call when the block gets removed, with None as a parameter
            :param kwargs: the kwargs to call the remove_block-function with


        function schedule_block_show(
                self, chunk: IChunk, position: tuple
                ):
            
            Schedules a show of a block
            :param chunk: the chunk
            :param position: the position of the block


        function schedule_block_hide(
                self, chunk: IChunk, position: tuple
                ):
            
            Schedules hiding a block
            :param chunk: the chunk
            :param position: the position of the block


        function schedule_visual_update(
                self, chunk: IChunk, position: tuple
                ):
            
            Schedules a visual update of a block (-> show/hide as needed)
            :param chunk: the chunk
            :param position: the position of the block


        function process_one_task(self, chunk: IChunk = None, log_msg=False) -> int
            
            Processes one task from a semi-random chunk or a given one
            :param chunk: the chunk or None to select one
            :param log_msg: if messages for extra info should be logged
            :return: a return status for the task; 1 when no tasks are arrival, 2 or 3 otherwise 


            variable start

                variable chunk

                variable chunk.generated

                variable chunk.finished

                variable chunk.loaded
            
            Process tasks in chunks [default to all scheduled chunks] until more time than timer is left behind
                [Defaults to no limit]
            :param chunks: if given, an iterable of chunks to generate
            :param timer: if given, a float in seconds to determine how far to generate
            todo: add some better sorting function!


            variable start

                variable chunks
                    todo: optimize this!

                    variable start

            variable start

            variable flag

                variable flag

                variable chunk.generated

                variable chunk.finished

                variable chunk.loaded

            variable dimension

                variable dim_map

                variable dim_map

            variable m: list

            variable data

                variable dim_map

                    variable m: dict

                        variable block

                            variable result

                variable dim_map

                    variable m: dict

                    variable block

        function get_block(
                self, position: tuple, chunk: IChunk
                ):
            
            Gets an generated block from the array
            :param position: the position of the block
            :param chunk: if the chunk is known
            todo: make thread-safe


            variable dimension

        function clear_chunk(self, chunk: IChunk)
            
            Will remove all scheduled tasks from an given chunk
            :param chunk: the chunk


        function clear(self)
            
            Will remove all scheduled tasks [chunk-wise]


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
                **kwargs,
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
        all scheduling functions are the same of WorldGenerationTaskHandler except the chunk-parameter is missing.
        It is set on construction


        function __init__(
                self,
                handler: WorldGenerationTaskHandler,
                chunk: IChunk,
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

            variable self.shared - OffProcessTaskHelper.OffProcessTaskHelperShared()
                todo: implement

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
                chunk: IChunk,
                default: WorldGenerationTaskHandlerReference,
                ) -> typing.Tuple[
                "ProcessSeparatedWorldGenerationTaskHandlerReference", OffProcessTaskHelper
                ]:
                helper_instance = OffProcessTaskHelper(chunk)
                array_instance = ProcessSeparatedWorldGenerationTaskHandlerReference(
                helper_instance.shared, chunk
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
                chunk: IChunk,
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