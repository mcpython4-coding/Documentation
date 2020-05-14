***EventInfo.py - documentation - last updated on 14.5.2020 by uuk***
___

    class IEventInfo
        
        base class for every event info
        

        function equals(self, *args)

    class KeyPressEventInfo extends IEventInfo
        
        info for key press
        

        function __init__(self, symbol: int, modifer=[])
        function equals(self, symbol, modifiers)

    class MousePressEventInfo extends IEventInfo
        
        info for mouse press
        

        function __init__(self, mouse: int, modifier=[], area=None)
        function equals(self, x, y, button, modifiers)

    class CallbackHelper
        function __init__(self, function, args=[], kwargs={}, extra_arg_filter=None, enable_extra_args=True)
            
            creates an new object
            :param function: the function to call
            :param args: the args given
            :param kwargs: the kwargs given
            :param extra_arg_filter: an function(args, kwargs) -> args, kwargs which filters them
            :param enable_extra_args: weither args given by __call__ should be included
            

        function __call__(self, *args, **kwargs)