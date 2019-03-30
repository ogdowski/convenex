import xmltodict


class Reader:
    def __init__(self, format_type):
        self.format_type = format_type

    def read_file(self, path):
        with open(path, "r") as file:
            data = file.read()
            return self._parse_xml(data)

    def _parse_xml(self, xml_data):    
        json_data = xmltodict.parse(xml_data)
        return json_data
