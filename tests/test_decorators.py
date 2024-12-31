from django.test import TestCase
from django.core.cache import cache
from core.models import WingmanSettings
from core.decorators import check_feature_flag
from unittest.mock import MagicMock


class CheckFeatureFlagTestCase(TestCase):
    def setUp(self):
        self.setting_name = "test_feature_flag"
        self.setting_value = True
        WingmanSettings.objects.create(
            name=self.setting_name,
            value=self.setting_value
        )

    def tearDown(self):
        cache.clear()

    def test_check_feature_flag_with_alt_value(self):
        """Test the decorator returns alt_value when the feature flag is enabled."""

        @check_feature_flag(flag_name=self.setting_name, alt_value="Feature Enabled")
        def test_function():
            return "Feature Disabled"

        result = test_function()
        self.assertEqual(result, "Feature Enabled")

    def test_check_feature_flag_with_alt_func(self):
        """Test the decorator calls alt_func when the feature flag is enabled."""
        alt_func_mock = MagicMock(return_value="Alternative Function Executed")

        @check_feature_flag(flag_name=self.setting_name, alt_func=alt_func_mock)
        def test_function():
            return "Feature Disabled"

        result = test_function()
        self.assertEqual(result, "Alternative Function Executed")
        alt_func_mock.assert_called_once()

    def test_check_feature_flag_executes_original_function(self):
        """Test the decorator executes the original function when the flag is disabled."""
        WingmanSettings.objects.filter(name=self.setting_name).update(value=False)

        @check_feature_flag(flag_name=self.setting_name)
        def test_function():
            return "Feature Disabled"

        result = test_function()
        self.assertEqual(result, "Feature Disabled")
