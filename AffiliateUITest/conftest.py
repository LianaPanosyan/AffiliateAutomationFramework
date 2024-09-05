import pytest
import logging
import datetime
import os
from selenium import webdriver
from Config.ConfigFileStaging import ConfigStaging
from Config.ConfigFileLive import ConfigLive


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests against: staging or live")


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    if env == "staging":
        return ConfigStaging
    elif env == "live":
        return ConfigLive
    else:
        raise ValueError(f"Unknown environment: {env}")


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def setup_logging(env):
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tests_log")
    os.makedirs(log_dir, exist_ok=True)
    log_file = f'UI_TestResultLog_{env}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    log_file_path = os.path.join(log_dir, log_file)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(log_file_path, mode='w'),
            logging.StreamHandler()
        ]
    )


def pytest_configure(config):
    env = config.getoption("--env")
    setup_logging(env)
    logging.info("=" * 60)
    logging.info(f"Starting new test run on environment: {env} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info("=" * 60)


def pytest_runtest_setup(item):
    logging.info(f"Starting test case: {item.name}")
