import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from clickchain_service import ClickChainService


class TestClickChainService:

    def setup_method(self):
        self.service = ClickChainService()

    def test_default_app_name(self):
        assert self.service.app_name == "ClickChain"

    def test_default_version(self):
        assert self.service.version == "1.0.0"

    def test_get_greeting_contains_name(self):
        greeting = self.service.get_greeting()
        assert "ClickChain" in greeting

    def test_get_greeting_contains_version(self):
        greeting = self.service.get_greeting()
        assert "1.0.0" in greeting

    def test_get_status(self):
        assert self.service.get_status() == "RUNNING"

    def test_custom_constructor(self):
        custom = ClickChainService("TestApp", "2.5.0")
        assert custom.app_name == "TestApp"
        assert custom.version == "2.5.0"
