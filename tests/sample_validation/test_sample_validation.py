from pytest_bdd import scenario, given, then, parsers, when




featureFilePath = "../../features/sample.feature"


@scenario(featureFilePath, "Sample Test -01")
def test_sampletest_01():
    print("...the Sample Test -01 IS COMPLETED...")

@given("run the sample test 01")
def sample_test_runner_01(sample):
    result = sample.sample_validator_01()
    assert result,print("the assertion failed")
