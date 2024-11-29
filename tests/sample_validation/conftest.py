import pytest
from steps.sample_validations import sample_validator

@pytest.fixture(scope="module")
def sample():
    return sample_validator()