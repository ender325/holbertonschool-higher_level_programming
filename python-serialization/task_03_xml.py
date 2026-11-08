#!/usr/init/python3
#!/usr/bin/python3
"""A module to serialize and deserialize Python dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # Store the type as an attribute to help with deserialization casting
        child.set("type", type(value).__name__)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Read XML data from a file and return a reconstructed Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result_dict = {}

        for child in root:
            key = child.tag
            val_type = child.get("type")
            text = child.text

            # Type conversion based on stored type or inference
            if val_type == "int":
                result_dict[key] = int(text)
            elif val_type == "float":
                result_dict[key] = float(text)
            elif val_type == "bool":
                result_dict[key] = True if text == "True" else False
            elif val_type == "NoneType":
                result_dict[key] = None
            else:
                result_dict[key] = text

        return result_dict
    except Exception:
        return None
