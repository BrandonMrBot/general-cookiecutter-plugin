from {{ cookiecutter.plugin_for }}.models.meta import Base
from {{ cookiecutter.plugin_for }}.models import User

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    ForeignKey,
    INTEGER,
    Unicode,
)

from sqlalchemy.dialects.mysql import MEDIUMTEXT


class ExampleTable(Base):
    __tablename__ = "{{ cookiecutter.plugin_name }}_example"

    example_id = Column(Unicode(64), primary_key=True)
    example_name = Column(Unicode(120))
    example_desc = Column(MEDIUMTEXT(collation="utf8mb4_unicode_ci"))
