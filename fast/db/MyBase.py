from datetime import datetime

from sqlalchemy import create_engine, func, DateTime, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

engine = create_engine(r'sqlite:///test.db', echo=True, future=True)

class MyBase(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), comment = '记录生成时间')
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), onupdate=func.now(), comment = '记录更新时间')
