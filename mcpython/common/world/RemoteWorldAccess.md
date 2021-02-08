***RemoteWorldAccess.py - documentation - last updated on 8.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class RemoteWorldHelper
        
        Some really big, complex system for asynchronous world-access-able multiprocessing.
        Use RemoteWorldHelper.spawn_process(World) for creating a new process linke to the given world.
        You MUST call run_tasks() regular on your RemoteWorldHelperReference to process tasks to run on main!


        class RemoteWorldContext

            function __init__(
                    self, world: mcpython.common.world.AbstractInterface.IWorld, helper
                    ):

                variable self.world

                variable self.helper

            function get_world(self) -> mcpython.common.world.AbstractInterface.IWorld

            function get_helper(self) -> "RemoteWorldHelper"

        class RemoteWorldHelperReference

            function __init__(
                    self,
                    instance: "RemoteWorldHelper",
                    process: multiprocessing.Process,
                    world: mcpython.common.world.AbstractInterface.IWorld,
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
                cls, world: mcpython.common.world.AbstractInterface.IWorld
                ) -> "RemoteWorldHelper.RemoteWorldHelperReference":

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

    class RemoteWorld extends mcpython.common.world.AbstractInterface.IWorld

        function __init__(self, helper: RemoteWorldHelper)

            variable self.helper

            variable self.chunk_dimension_cache

            variable dim_id

            variable dim

            variable dim

            variable dim

            variable max_distance: int

    class RemoteDimension extends mcpython.common.world.AbstractInterface.IDimension

        function __init__(
                self, helper: RemoteWorldHelper, dimension_id: int, world: RemoteWorld
                ):

            variable self.helper

            variable self.dimension_id

            variable self.dimension_range

            variable self.dimension_name

            variable self.world

            variable self.chunk_cache

        function get_dimension_range(self) -> typing.Tuple[int, int]

        function get_id(self)

        function get_name(self) -> str

            variable cz: int

            variable generate: bool

            variable create: bool

            variable chunk

                variable position

            variable pos

    class RemoteChunk extends mcpython.common.world.AbstractInterface.IChunk

        function __init__(self, helper: RemoteWorldHelper, position, dimension: RemoteDimension)

            variable self.helper

            variable self.position

            variable self.dimension

            variable self.block_cache

        function get_dimension(self) -> "RemoteDimension"

        function get_position(self) -> typing.Tuple[int, int]

        function on_block_updated(
                self, position: typing.Tuple[float, float, float], itself=True
                ):

        function check_neighbors(self, position: typing.Tuple[int, int, int])

            variable immediate: bool

        function as_shareable(self) -> "RemoteChunk"

        function mark_dirty(self)