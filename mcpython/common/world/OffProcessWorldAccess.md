***OffProcessWorldAccess.py - documentation - last updated on 6.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class OffProcessWorldHelper
        
        Some huge, complex system for asynchronous world-access-able multiprocessing.
        Use OffProcessWorldHelper.spawn_process(World) for creating a new process linke to the given world.
        You MUST call run_tasks() regular on your RemoteWorldHelperReference to process tasks to run on main!


        class OffProcessWorldContext

            function __init__(
                    self, world: mcpython.engine.world.AbstractInterface.IWorld, helper
                    ):

                variable self.world

                variable self.helper

            function get_world(self) -> mcpython.engine.world.AbstractInterface.IWorld

            function get_helper(self) -> "OffProcessWorldHelper"

        class OffProcessWorldHelperReference

            function __init__(
                    self,
                    instance: "OffProcessWorldHelper",
                    process: multiprocessing.Process,
                    world: mcpython.engine.world.AbstractInterface.IWorld,
                    ):

                variable self.instance

                variable self.process

                variable self.context

            function stop(self, immediate=True)

            function run_tasks(self)

            function run_on_process(self, func, *args, **kwargs)

            function get_worker_count(self)

        static
        function spawn_process(
                cls, world: mcpython.engine.world.AbstractInterface.IWorld
                ) -> "OffProcessWorldHelper.OffProcessWorldHelperReference":

            variable instance

            variable process

        static
        function run_task(cls, task, result_helper, context)

        static
        function run_task_async(cls, task, context)

                variable p

        static
        function decode_task(cls, task) -> typing.Tuple[typing.Callable, list, dict, typing.Any]

        static
        function encode_task(cls, func, args, kwargs, info) -> bytes

        function __init__(self)

            variable self.task_main_queue

            variable self.task_off_process_queue

            variable self.task_result_queue

            variable self.running

            variable self.inner_task_id

            variable self.worker_count

            variable self.pending_result_waits

        function get_worker_count(self) -> int

        function stop(self)

        function run(self)

            variable context

                    variable task

                    variable self.pending_result_waits[task_id]

            variable task_id

            variable result

        function run_on_main(self, func, *args, **kwargs)

        function run_on_process(self, func, *args, **kwargs)

    class OffProcessWorld extends mcpython.engine.world.AbstractInterface.IWorld

        function __init__(self, helper: OffProcessWorldHelper)

            variable self.helper

            variable self.chunk_dimension_cache

            variable dim_id

            variable dim

            variable dim

            variable dim

            variable max_distance: int

    class OffProcessDimension extends mcpython.engine.world.AbstractInterface.IDimension

        function __init__(
                self, helper: OffProcessWorldHelper, dimension_id: int, world: OffProcessWorld
                ):

            variable self.helper

            variable self.dimension_id

            variable self.dimension_range

            variable self.dimension_name

            variable self.world

            variable self.chunk_cache

        function get_world_height_range(self) -> typing.Tuple[int, int]

        function get_dimension_id(self)

        function get_name(self) -> str

            variable cz: int

            variable generate: bool

            variable create: bool

            variable chunk

                variable position

            variable pos

    class OffProcessChunk extends mcpython.engine.world.AbstractInterface.IChunk

        function __init__(
                self, helper: OffProcessWorldHelper, position, dimension: OffProcessDimension
                ):

            variable self.helper

            variable self.position

            variable self.dimension

            variable self.block_cache

        function get_dimension(self) -> "OffProcessDimension"

        function get_position(self) -> typing.Tuple[int, int]

        function on_block_updated(
                self, position: typing.Tuple[float, float, float], itself=True
                ):

        function check_neighbors(self, position: typing.Tuple[int, int, int])

            variable immediate: bool

        function as_shareable(self) -> "OffProcessChunk"

        function mark_dirty(self)