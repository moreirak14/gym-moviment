from typing import Dict


class BaseModelCustom:
    def update(self, data: Dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
