from typing import List

import pytest

from main import main

test_filenames_exceptions: List[str] = [
    "test_files/test_file_1",
    "test_files/test_file_2",
    "test_files/test_file_3",
    "test_files/test_file_4",
]


@pytest.mark.parametrize("filename", test_filenames_exceptions)
def test_filesnames_exceptions(filename):
    with pytest.raises(FileNotFoundError) as execinfo:
        main(["a", "b", filename])

        assert execinfo.value == f"File {filename} is found"
