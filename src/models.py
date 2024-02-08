from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import enum
import datetime
from typing import Optional, Annotated

metadata_obj = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)


from database import Base


class WorkersOrm(Base):
    __tablename__ = "workers"
    id: Mapped[intpk]
    username: Mapped[str]


# class Workload(enum.Enum):
#     parttime = "parttime"
#     fulltime = "fulltime"
#
# class ResumesOrm(Base):
#     __tablename__ = "resumes"
#
#     id: Mapped[intpk]
#     title: Mapped[str]
#     compensation: Mapped[int | None]
#     workload: Mapped[Workload]
#     worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
#     created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"),
#                                                                 onupdate=datetime.datetime.utcnow)
    