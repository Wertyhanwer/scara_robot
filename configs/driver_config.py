from pydantic import ConfigDict, PrivateAttr
from driver_config_data import HalDriverConfigData
from typing import Optional
import json


class HalDriverConfig(HalDriverConfigData):
    """Конфигурация HAL драйвера с автоматической валидацией и синхронизацией"""

    model_config = ConfigDict(
        validate_assignment=True,  # Валидация при изменении полей
    )

    # Приватные атрибуты (автоматически исключаются из сериализации)
    _config_path: str = PrivateAttr(default="configs_json/hal_driver_config.json")
    _initialized: bool = PrivateAttr(default=False)

    def model_post_init(self, __context):
        """Вызывается после инициализации модели"""
        self._initialized = True
        self.save_to_config()
        print(f"✓ Конфиг инициализирован и сохранён в {self._config_path}")

    def __setattr__(self, name: str, value):
        super().__setattr__(name, value)
        if hasattr(self, '_initialized') and self._initialized and not name.startswith('_'):
            self.save_to_config()
            print(f"✓ Поле '{name}' изменено на '{value}', конфиг обновлён")

    def save_to_config(self, path: Optional[str] = None):
        try:
            save_path = path or self._config_path

            config_data = self.model_dump()

            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"✗ Ошибка сохранения конфига: {e}")

    def update_from_dict(self, data: dict):
        """Обновление полей из словаря с валидацией"""
        for key, value in data.items():
            if key in self.model_fields:
                setattr(self, key, value)  # Валидация + автосохранение

