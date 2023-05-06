from pb_encoding import EncodeField, DecodeField, SupportedType


def func(type: SupportedType, value):
    b = bytearray()
    x = value
    EncodeField(type, b.__iadd__, x)
    y, _ = DecodeField(type, b, 0)
    print(type, b, x, y)
    return x == y


def test():
    assert func("int32", 65)
    assert not func("int32", 6500000000)
    assert func("uint32", 255)
    assert not func("uint32", 6500000000)
    assert func("sint32", -1)
    assert func("sint64", -1)
    assert func("fixed32", 1680000000)
    assert func("fixed64", 650000000000)
    assert func("sfixed32", -1680000000)
    assert func("sfixed64", -1680000000000)
    assert func("string", "s")
    assert func("string", "sssssssssss")
    assert func("bytes", b"sssssssssss")
