from src.adapters.databases import Base
from sqlalchemy.orm import registry

metadata = Base.metadata
mapper_registry = registry()
