def compare_versions(version_one, version_other):
    """Compare passed versions.

    :param version_one: (str)
    :param version_other: (str)
    :return: (int) 1 if `version_one` is greater than `version_other`
                   -1 if `version_other` is greater than `version_one`
                   0 if passed versions are equal.
    """
    ver_list_one = [int(v) for v in version_one.split(".")]
    ver_list_other = [int(v) for v in version_other.split(".")]

    for i in range(max(len(ver_list_one), len(ver_list_other))):
        unit_one = ver_list_one[i] if i < len(ver_list_one) else 0
        unit_other = ver_list_other[i] if i < len(ver_list_other) else 0
        if unit_one > unit_other:
            return 1
        elif unit_one < unit_other:
            return -1
    return 0
