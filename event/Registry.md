***Registry.py - documentation - last updated on 30.5.2020 by uuk***
___

    class IRegistryContent

        variable NAME

        variable TYPE

        variable INFO - can be used to display any special info in e.g. /registryinfo-command

        static
        function compressed_info(cls): return cls.NAME
                
                
                class Registry:
                def __init__(self, name: str, registry_type_names: list, injection_function=None,
                allow_argument_injection=False, class_based=True):

    class Registry

        function __init__(self, name: str, registry_type_names: list, injection_function=None,
                allow_argument_injection=False, class_based=True):

        function is_valid(self, obj: IRegistryContent)

        function register(self, obj: IRegistryContent, override_existing=True)

    class RegistryInjectionHolder

        function __init__(self, *args, **kwargs):   # todo: do something with the args and kwargs!
                self.args = args
                self.kwargs = kwargs
                self.injectable = None
                
                def __call__(self, obj):

            variable self.args

            variable self.kwargs

            variable self.injectable

        function __call__(self, obj)

    class RegistryHandler

        function __init__(self)

            variable self.registries

        function __call__(self, *args, **kwargs)

        function get_by_name(self, name: str) -> Registry

        function register(self, *args, **kwargs)

    variable G.registry