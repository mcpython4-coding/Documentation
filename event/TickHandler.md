***TickHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class TickHandler
        
        main handler for ticks
        

        function __init__(self)
        function tick(self, dt)
            
            execute ticks
            :param dt: the time that came after the last event
            

        function schedule_once(self, function, *args, **kwargs)
            
            Will execute the function in near time. Helps when in an event and need to exchange stuff which might be
            affected when calling further down the event stack
            :param function: the function to call
            

        function bind(self, function, tick, isdelta=True, ticketfunction=None, args=[], kwargs={})
            
            bind an function to an given tick
            :param function: the function to bind
            :param tick: the tick to add
            :param isdelta: if it is delta or not
            :param ticketfunction: function which is called when the function is called with some informations
            :param args: the args to give
            :param kwargs: the kwargs to give
            

        function bind_redstone_tick(self, function, tick, *args, **kwargs)
        function send_random_ticks(self, *args, **kwargs)

    variable handler
