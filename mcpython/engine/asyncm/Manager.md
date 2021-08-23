***Manager.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class SpawnedProcessInfo

        function __init__(self, name: str)

            variable self.name

            variable self.main2off

            variable self.main2off_data

            variable self.off2main

            variable self.off2main_data

            variable self.sided_task_manager: typing.Optional[TaskManager]

            variable self.call_regular

        function spawn_main_task_manager(self)

        function spawn_off_task_manager(self)

        function off_work(self)

            variable manager

            variable manager.router

            variable self.sided_task_manager

    class TaskManager

        function __init__(
                self,
                info: "SpawnedProcessInfo",
                queue_in: multiprocessing.Queue,
                data_queue_in: multiprocessing.Queue,
                queue_out: multiprocessing.Queue,
                data_queue_out: multiprocessing.Queue,
                ):

            variable self.info

            variable self.queue_in

            variable self.data_queue_in

            variable self.queue_out

            variable self.data_queue_out

            variable self.next_id

            variable self.process: typing.Optional[multiprocessing.Process]

            variable self.is_on_main

            variable self.main_obj: typing.Optional["AsyncProcessManager"]

                variable result

                variable (

                    variable manager

                variable self.result_cache[task_id]
                    todo: clean up this somehow... (maybe weakref?)

                variable internal_id

                variable internal_id

            variable event

            variable self.waiting_awaits[internal_id]

        function invokeOnMainNoWait(self, function, *args, **kwargs)

                variable internal_id

                variable internal_id

            variable event

            variable self.waiting_awaits[internal_id]

        function invokeOnNoWait(self, process: str, function, *args, **kwargs)

        function __repr__(self)

    class AsyncProcessManager
        
        This is the class managing everything
        Call main() in order to get things going
        [The inter-process-com is not active before]
        Tasks may run before calling main()


        function __init__(self)

            variable self.spawned_processes: typing.List[SpawnedProcessInfo]

            variable self.callbacks

            variable self.running

        function add_regular_async_callback(
                self, callback: typing.Callable[[SpawnedProcessInfo], typing.Awaitable]
                ):

        function run_regular_on_process(self, process: str, task, *args, **kwargs)

        function add_process(self, name: str) -> SpawnedProcessInfo

            variable info

            variable self.lookup_processes[name]

            variable process

            variable info.sided_task_manager

            variable info.sided_task_manager.process

            variable info.sided_task_manager.router

            variable info.sided_task_manager.is_on_main

            variable info.sided_task_manager.main_obj

        function main(self)

            variable self.running

        function stop(self)