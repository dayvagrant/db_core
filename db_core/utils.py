from db_core.env import _CONFIGS

class CONFIG:
    """Config extractor."""

    def __init__(self, dict_of_configs: dict = None):
        if dict_of_configs is None:
            from db_core.env import _CONFIGS
        else:
            _CONFIGS = dict_of_configs


    @classmethod
    def get(cls, *args) -> dict:
        """Method to extract target config."""
        current = _CONFIGS.copy()
        for key in args:
            current = current.get(key, None)
        if current is None:
            raise Exception (f"callable setting name {key} is missing in the options.")
        return current