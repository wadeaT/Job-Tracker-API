from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_username: str
    database_name: str

    model_config = SettingsConfigDict(env_file=".env")

    # should I add @computed_field ? what it is for? 
    @property
    def database_url(self)->str:
        return f"postgresql+psycopg://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}"
        
settings = Settings()