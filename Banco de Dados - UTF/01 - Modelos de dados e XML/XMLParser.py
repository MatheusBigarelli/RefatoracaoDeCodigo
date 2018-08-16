class XMLParser:
    def __init__(self):
        pass

    def create_info_object_with_attributes(self, xml_element, keys):
        dictionary = self.create_dictionary(xml_element, keys)
        return dictionary

    def create_dictionary(self, xml_element, keys):
        dictionary = {}
        for key in keys:
            dictionary[key] = self.get_string_value_of_attribute(xml_element, key)
        return dictionary

    def get_string_value_of_attribute(self, xml_element, tag):
        return xml_element.getElementsByTagName(tag)[0].childNodes[0].data
