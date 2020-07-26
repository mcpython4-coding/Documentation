***net.py - documentation - last updated on 20.7.2020 by uuk***
___

    class SimulatedResponse
        
        Simulated response


        function __init__(self, content, is_json, raw=None)

            variable self.content

            variable self.is_json

            variable self.status_code

            variable self.raw

        function json(self)

    variable SIMULATE

    function get_url(url, **kwargs)
        
        gets the content of an URL as an requests.get() or an an SimulatedResponse-instance
        :param url: the url to download from
        :param kwargs: kwargs to requests.get() with
        :return: the content
