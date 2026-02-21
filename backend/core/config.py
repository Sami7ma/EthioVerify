from pydantic import BaseSettings

class Settings(BaseSettings):

    #application
    APP_NAME: str = "EthioVerify"
    DEBUG: bool = True
    
    #UPLOAD
    UPLOAD_DIR: str = "temp_uploads"

    #FRAUD SCORING WEIGHTS
    METADATA_WEIGHT: float = 0.15
    ELA_WEIGHT: float = 0.35
    OCR_WEIGHT: float = 0.15
    RULES_WEIGHT: float = 0.35

    class Config:
        env_file = ".env"
