from lxml import etree


def get_if_ok(try_set: list, from_root: etree.ElementTree, condition_ok):
    for i in try_set:
        _ele = from_root.xpath(i)
        if condition_ok(_ele):
            return _ele
    return None