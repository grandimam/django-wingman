from django.test import TestCase
from unittest.mock import patch
from django.core.cache import cache
from wingman.models import WingmanSettings


class WingmanCacheManagerTestCase(TestCase):
    def setUp(self):
        self.setting_name = "test_setting"
        self.setting_value = True
        self.cache_expiry = 3600

        self.setting = WingmanSettings.objects.create(
            name=self.setting_name,
            value=self.setting_value,
            cache_expiry=self.cache_expiry,
            description="Test description"
        )

    def tearDown(self):
        cache.clear()

    def test_get_settings_caches_value(self):
        """Test that get_settings caches the setting value."""
        cache_key = WingmanSettings.objects.PREFIX.format(name=self.setting_name)

        self.assertIsNone(cache.get(cache_key))

        WingmanSettings.objects.get_settings(self.setting_name)

        cached_value = cache.get(cache_key)
        self.assertEqual(cached_value, self.setting_value)

    def test_get_settings_handles_missing_setting(self):
        """Test that get_settings logs an error if the setting is missing."""
        missing_name = "missing_setting"
        cache_key = WingmanSettings.objects.PREFIX.format(name=missing_name)

        with patch(".models.logger.error") as mock_logger:
            WingmanSettings.objects.get_settings(missing_name)

            mock_logger.assert_called_once_with(
                'Settings %s is not found: %s',
                missing_name,
                'WingmanSettings matching query does not exist.'
            )

        self.assertIsNone(cache.get(cache_key))

    def test_delete_settings_removes_cache(self):
        """Test that delete_settings removes the cached value."""
        cache_key = WingmanSettings.objects.PREFIX.format(name=self.setting_name)

        WingmanSettings.objects.get_settings(self.setting_name)
        self.assertIsNotNone(cache.get(cache_key))

        WingmanSettings.objects.delete_settings(self.setting_name)

        self.assertIsNone(cache.get(cache_key))

    def test_get_value_class_method(self):
        """Test that the get_value class method retrieves the correct value."""
        value = WingmanSettings.get_value(self.setting_name)
        self.assertEqual(value, self.setting_value)
