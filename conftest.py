
import os
import pathlib
import pytest



#Sending email
def pytest_sessionstart(session):
    session.results = dict()
    # creating report dir
    # native json and html format reports are created in reports dir
    reports_path = "reports"
    isReportDirExists= os.path.exists(reports_path)
    if not isReportDirExists:
        os.makedirs(reports_path)
        print("Created reports directory...")

    testdata_path = pathlib.Path("test_data")
    istestdataDirExists = testdata_path.exists()
    if not istestdataDirExists:
        testdata_path.mkdir(parents=True, exist_ok=True)
        print("Created test_data directory...")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


suite_names = set()





def pytest_sessionfinish(session, exitstatus):


    print("suite_names: {} ".format(suite_names))
    print('status code: {}'.format(exitstatus))

    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    total = passed_amount + failed_amount
    print('there are {} passed and {} failed tests'.format(passed_amount, failed_amount))


