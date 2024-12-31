from django.test import TestCase
from unittest.mock import patch
from wingman.models import WingmanSettings
from django.core.cache import cache


class TestSignal(TestCase):
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

    @patch("wingman.models.WingmanSettings.objects.delete_settings")
    def test_invalidate_cache_on_post_save(self, mock_delete_settings):
        """Test that cache is invalidated on post_save signal."""
        self.setting.value = not self.setting_value
        self.setting.save()

        mock_delete_settings.assert_called_once_with(self.setting_name)

    @patch("wingman.models.WingmanSettings.objects.delete_settings")
    def test_invalidate_cache_on_post_delete(self, mock_delete_settings):
        """Test that cache is invalidated on post_delete signal."""
        self.setting.delete()

        mock_delete_settings.assert_called_once_with(self.setting_name)
