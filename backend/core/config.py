from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "EthioVerify"
    DEBUG: bool = True

    UPLOAD_DIR: str = "temp_uploads"

    METADATA_WEIGHT: float = 0.15
    ELA_WEIGHT: float = 0.35
    OCR_WEIGHT: float = 0.15
    RULE_WEIGHT: float = 0.35

    model_config = {
        "env_file": ".env"
    }


settings = Settings()