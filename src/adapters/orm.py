from sqlalchemy.orm import registry

from src.adapters.databases import Base

metadata = Base.metadata
mapper_registry = registry()
