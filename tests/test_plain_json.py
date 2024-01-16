from gendiff.difference import generate_diff

file1 = './tests/fixtures/file1.json'
file2 = './tests/fixtures/file2.json'


def test_plain_json():
    sample = './tests/fixtures/plain_result.txt'

    with open(sample) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2) == sample_content
