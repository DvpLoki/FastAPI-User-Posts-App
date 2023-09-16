from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import DateTime



class Base (DeclarativeBase):
    pass

class post(Base):
    __tablename__='posts'
    id:Mapped[int]=mapped_column(primary_key=True,nullable=False)
    user_id=mapped_column(ForeignKey("users.id",ondelete="cascade"),nullable=False)
    title:Mapped[str]=mapped_column(nullable=False)
    content:Mapped[str]=mapped_column(nullable=False)
    published:Mapped[bool]=mapped_column(server_default='True',nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=text('now()'))
    owner=relationship("user")

class user(Base):
    __tablename__='users'
    id:Mapped[int]=mapped_column(primary_key=True,nullable=False)
    email:Mapped[str]=mapped_column(unique=True,nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=text('now()'))


