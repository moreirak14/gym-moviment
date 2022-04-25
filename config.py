from pathlib import Path

from dynaconf import Dynaconf

PATH_ROOT = Path(__file__).parent

settings = Dynaconf(
    environments=True,
    envvar_prefix="GYM_MOVEMENT",
    settings_files=["settings.toml", ".secret.toml"],
    includes=[f"{PATH_ROOT}/settings.toml", f"{PATH_ROOT}/.secret.toml"],
)


def database_uri():
    _database_uri = (
        f"{settings.database_dialect_driver}://"
        f"{settings.database_user}:{settings.database_password}@"
        f"{settings.database_host}:{settings.database_port}/"
        f"{settings.database_name}"
    )

    return _database_uri


settings.database_uri = database_uri()
