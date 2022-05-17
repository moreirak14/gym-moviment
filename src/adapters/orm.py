from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import clear_mappers, registry, relationship

from src.adapters.databases import Base
from src.domain.lead.model import Lead
from src.domain.user.model import User

metadata = Base.metadata
mapper_registry = registry()

table_user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(60)),
    Column("hashed_password", String(255)),
)

table_lead = Table(
    "lead",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("owner_id", Integer, ForeignKey("user.id")),
    Column("first_name", String(60), nullable=False),
    Column("last_name", String(60), nullable=False),
    Column("email", String(60)),
    Column("email", String(15)),
)


def start_mappers():
    clear_mappers()

    mapper_registry.map_imperatively(User, table_user)
    mapper_registry.map_imperatively(
        Lead, table_lead, properties={"user": relationship(User)}
    )
