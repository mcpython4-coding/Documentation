***ModLoadingStages.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class LoadingStageManager
        
        System for handling the order of loading phases with dynamic dependency handling


        function __init__(self)

            variable self.stages

            variable self.order: typing.Optional[graphlib.TopologicalSorter]

            variable self.current_stage: typing.Optional[str]

            variable self.ready: typing.List[str]

        function get_new_ready(self)

        function get_stage(self) -> typing.Optional["LoadingStage"]

        function next_stage(self)

        function add_stage(self, stage: "LoadingStage")

        function update_order(self)

    class LoadingStage
        
        A single LoadingStage instance
        Used for holding information about the stage


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

            variable self.active_event

            variable self.active_mod_index

        function finished(self)

        function add_event_stage(self, event_name: str, *inner_depends: str)

        function add_event_stage_dependency(self, event_name: str, *inner_depends: str)

        function add_dependency(self, stage_name: str)

        function update_order(self)

            variable self.order
            
            Will finish up the system
            :param astate: the state to use


            variable astate.parts[2].progress

            variable new_stage: LoadingStage

                variable shared.mod_loader.finished

                variable astate.parts[2].progress_max

                variable astate.parts[2].progress_max

            variable self.active_mod_index

            variable mod_instance

            variable self.max_progress

            variable astate.parts[2].progress_max

            variable astate.parts[2].progress
            
            Will call one event from the stack
            :param astate: the state to use
            todo: split into smaller parts!


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