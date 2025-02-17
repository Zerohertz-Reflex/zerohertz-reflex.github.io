from pydantic import BaseModel


class ThemeConfig(BaseModel):
    accent_color: str = "red"
    gray_color: str = "gray"
    radius: str = "large"
    scaling: str = "100%"


theme_config = ThemeConfig()
