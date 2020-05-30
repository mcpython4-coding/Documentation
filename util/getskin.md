***getskin.py - documentation - last updated on 30.5.2020 by uuk***
___

    variable DEBUG

    variable SIMULATE

    variable userid_url

    variable userinfo_url

    class SimulatedResponse extends object

        function __init__(self, content, is_json, raw=None)

            variable self.content

            variable self.is_json

            variable self.status_code

            variable self.raw

        function json(self)

    function find_texture_info(properties)

    function get_url(url, **kwargs)

    function download_skin(username: str, store: str)

            variable r

        variable userid

        variable r

        variable userinfo

            variable texture_info

        variable skin_url

        variable r

        variable image

            variable new_image