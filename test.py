from extract_data import extract_info

def test_extraction_OK():
    assert extract_info('.', 'SUV') is not None
    assert extract_info('.', 'HU') is not None
    assert extract_info('.', 'suv') is not None

def test_extraction_NON_OK():
    assert extract_info('.', 'toto') is None