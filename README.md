# Wingman

🚀 A Powerful Caching & Settings Management Library for Django

Wingman is a Django library designed to effortlessly manage and cache application settings. With a simple and 
elegant interface, you can store your configuration settings, cache them for performance, and retrieve them with 
ease—without worrying about stale data or unnecessary database queries.

Whether you're building a web app, an API, or anything in between, Wingman Settings is the perfect companion to handle 
your settings management needs!

---

## 📦 Installation

1. Install the package using pip:

```
pip install wingman
```

2. Add wingman_settings to your INSTALLED_APPS in settings.py:

```
INSTALLED_APPS = [
  'wingman',
]
```

3. Run migrations to create the necessary database table:

```
python manage.py migrate wingman
```

---

## 🛠 How It Works

Wingman provides a custom model WingmanSettings to store key-value pairs for your application settings. 
Additionally, the WingmanCacheManager manager allows caching of these settings, so you never need to hit the database 
unless necessary.

### Model: WingmanSettings
- name: A unique name for the setting (used as the key).
- value: The value of the setting, which can be any type.
- cache_expiry: Expiry time for the cached setting in seconds.
- description: Optional description for the setting.
- history: Automatically tracks changes to settings using simple_history.

### Manager: WingmanCacheManager

- **get_settings(name):** Retrieves a setting by its name, first checking the cache. If not found, it queries the database and caches the result for future use.
- **delete_settings(name):** Deletes the setting from the cache.

---

## 🔧 Usage

### Creating Settings

You can create settings like so:

```
from wingman.core.models import WingmanSettings

setting = WingmanSettings.objects.create(
    name='FEATURE_TOGGLE',
    value=True,
    cache_expiry=3600,  # Cache expiry time in seconds
    description='Enables the feature toggle for the new feature.'
)
```

### Retrieving Settings

Retrieve settings using the ```get_value`` method:

```
from wingman.core.models import WingmanSettings

# Get the value of a setting
setting_value = WingmanSettings.get_value('FEATURE_TOGGLE')
```

---

### 🔄 Version History

v1.0.0: Initial release. Includes WingmanSettings model with caching support via WingmanCacheManager.

### 📄 License

Wingman Settings is open-source and released under the MIT License.

### ✨ Why Wingman Settings?

- **Caching:** Automatically caches your settings for faster retrieval.
- **Simplicity:** A minimal, easy-to-use API that requires no boilerplate code.
- **Scalability:** Works seamlessly for large applications with many settings.
- **History Tracking:** Keep track of setting changes with simple_history.
- 