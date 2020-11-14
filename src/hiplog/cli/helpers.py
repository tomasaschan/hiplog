from zoneinfo import ZoneInfo


def datetime_with_zoneinfo(_ctx, _param, value):
    return value.replace(tzinfo=ZoneInfo("Europe/Stockholm"))


def parse_enum(cls):
    return lambda _ctx, _param, value: cls.parse(value)
