from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from fast.db.MyBase import MyBase

class User(MyBase):

    __tablename__ = 'user_t'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)