def assert_type(value, *expected_types):
    if not isinstance(value, expected_types):
        expected_names = ','.join(t.__name__ for t in expected_types)
        raise ValueError('{!r} must be one of {}'.format(value,
                                                         expected_names))
    return value

