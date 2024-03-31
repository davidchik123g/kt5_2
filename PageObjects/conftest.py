
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import logging


def get_logger(name, file_path):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(file_path, mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


@pytest.fixture(scope="function")
def logger(request):
    test_name = request.node.name
    log_dir = os.path.join(os.getcwd(), "opencart_logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"{test_name}.log")
    return get_logger(test_name, log_file_path)


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver

    def fin():
        driver.quit()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use: chrome or firefox")
