from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert isinstance(
        read_brazilian_file("tests/mocks/brazilians_jobs.csv"), list
        )

    assert isinstance(
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0], dict
        )

    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0] == {
            'salary': '2000',
            'title': 'Maquinista',
            'type': 'trainee'
        }

    assert int(read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv")[0]["salary"]) == 2000

    assert read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv")[0]["title"] == 'Maquinista'

    assert read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv")[0]["type"] == 'trainee'
