***StateWorldGeneration.py - documentation - last updated on 12.6.2020 by uuk***
___

    class StateWorldGeneration extends State.State

        variable NAME

        function __init__(self)

            variable self.status_table

        function get_parts(self) -> list

        function on_update(self, dt)

        function on_activate(self)

        function finish(self)

                variable chunk

                variable chunk.is_ready

                variable chunk.visible

            variable self

            variable playername

            variable G.world.active_player

            variable G.world.get_active_player().position

            variable G.world.config["enable_auto_gen"] - special.value.true*#"

            variable G.world.config["enable_world_barrier"]

            variable height

            variable blockchest

            variable blockchest.loot_table_link

            variable player
                set player position

            variable G.world.world_loaded

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        function calculate_percentage_of_progress(self)

        function on_draw_2d_post(self)

                variable status

                    variable factor

                    variable color

                    variable color

                    variable color

    variable worldgeneration

    function create()