***ModLoadingPipe.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class LoadingStageManager
        
        System for handling the order of loading phases with dynamic dependency handling


        function __init__(self)

            variable self.stages

            variable self.order: typing.Optional[graphlib.TopologicalSorter]

            variable self.current_stage: typing.Optional[str]

            variable self.ready: typing.List[str] - todo: can we use queue?

        function get_new_ready(self)

        function get_stage(self) -> typing.Optional["LoadingStage"]

        function next_stage(self)

        function add_stage(self, stage: "LoadingStage")

        function update_order(self)

    class LoadingStage

        function __init__(self, name: str, user_facing_name: str, *dependencies: str)

            variable self.name

            variable self.user_facing_name

            variable self.events

            variable self.dependencies

            variable self.order: typing.Optional[graphlib.TopologicalSorter]

            variable self.dirty

            variable self.active_mod_index

            variable self.max_progress

            variable self.current_progress

            variable self.active_event

            variable self.event_scheduled: typing.List[str]

        function next_event(self)

        function finished(self)

        function add_event_stage(self, event_name: str, *inner_depends: str)

        function add_event_stage_dependency(self, event_name: str, *inner_depends: str)

        function add_dependency(self, stage_name: str)

        function update_order(self)

            variable self.order

        static
        function finish(cls, astate)
            
            Will finish up the system
            :param astate: the state to use


                    variable player

                    variable player.position

                    variable player.rotation

                variable shared.mod_loader.finished

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress_max

        function call_one(self, astate)
            
            Will call one event from the stack
            :param astate: the state to use


                variable self.active_mod_index

                variable mod_instance

                variable self.max_progress

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress

                variable self.active_mod_index

            variable modname

            variable mod_instance

                    variable self.active_mod_index

                    variable mod_instance

                        variable self.max_progress

                        variable self.max_progress

                    variable astate.parts[2].progress_max

                    variable astate.parts[2].progress

                variable mod_instance

                    variable self.max_progress

                    variable self.max_progress

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress

    variable manager

        variable stage