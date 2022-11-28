import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from .factories import *
from django.test import LiveServerTestCase
from unittest import TestCase
import requests
from rest_framework.test import APIClient
from django.test.client import Client