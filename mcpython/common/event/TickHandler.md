***TickHandler.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class TickHandler
        
        main handler for ticks


        function __init__(self)

            variable self.tick_array

            variable self.active_tick

            variable self.next_ticket_id

            variable self.results

            variable self.lost_time

            variable self.enable_tick_skipping

            variable self.instant_ticks

            variable self.enable_random_ticks

            variable self.execute_array
                an array of (function, args, kwargs) for functions which should be executed in near future

        function tick(self, dt)
            
            execute ticks
            :param dt: the time that came after the last event


        function schedule_once(self, function, *args, **kwargs)
            
            Will execute the function in near time. Helps when in an event and need to exchange stuff which might be
            affected when calling further down the event stack
            :param function: the function to call


        function bind(
                self, function, tick, is_delta=True, ticket_function=None, args=[], kwargs={}
                ):
            
            bind an function to an given tick
            :param function: the function to bind
            :param tick: the tick to add
            :param is_delta: if it is delta or not
            :param ticket_function: function which is called when the function is called with some informations
            :param args: the args to give
            :param kwargs: the kwargs to give


                variable self.tick_array[tick]

                variable ticket_id

                variable ticket_id

        function bind_redstone_tick(self, function, tick, *args, **kwargs)

        function send_random_ticks(self, *args, **kwargs)

            variable random_tick_speed

            variable r

                        variable x

                        variable z

                                variable position

                                variable instance

    variable handler