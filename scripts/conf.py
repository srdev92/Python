import xmltodict

class Conf:
    def __init__(self, url):
        self.url = url

    def params(self):
        with open(self.url) as f:
            xml_content = f.read()

        xml_dict = xmltodict.parse(xml_content)
        return xml_dict['Storage']
