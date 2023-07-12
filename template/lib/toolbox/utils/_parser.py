'''
Not for import.
'''
__all__ = ['parse_unknown_args']

def parse_unknown_args(args: list[str], prefix: str = '-') -> dict:
    '''
    Parse unknown arguments `list` into `dict`. Basically, it's design to parse the return of `ArgumentParser.parse_known_args()`.

    For example, a `list` like::

        [
            "test",
            "--foo",
            "bar",
            "-buz",
            "1",
            "2",
            "3",
            "--sys",
            "xyz"
        ]

    Will be parsed into::

        {
            "unnamed": "test",
            "foo": "bar",
            "buz": [
                "1",
                "2",
                "3"
            ],
            "sys": "xyz"
        }

    :param list args: List of arguments.
    :param str prefix: The prefix of arguments.
    :return: Parsed arguments.
    :rtype: `dict`
    '''
    res = {}
    flag = 'unnamed'
    members = []
    for i in args:
        if i[0] == prefix:
            res[flag] = members if len(members) > 1 else ''.join(members)
            flag = i.lstrip(prefix)
            members = []
        else:
            members.append(i)
    res[flag] = members if len(members) > 1 else ''.join(members)
    if not res['unnamed']:
        del res['unnamed']
    return res