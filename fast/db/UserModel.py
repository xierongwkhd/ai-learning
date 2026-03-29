from os import name

from sqlalchemy import String, insert, select, text, update
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker

from fast.db.MyBase import MyBase, engine


class User(MyBase):

    __tablename__ = 'user_t'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with sessionmaker(engine).begin() as session:
        # user1 = User(name='张三')
        # session.add(user1)
        # insert_user = insert(User).values(name='李四')
        # session.execute(insert_user)
        # user1 = session.get(User, 1)
        # print(user1)
        stmt = select(User.name)
        result = session.scalars(stmt).all()
        print(result)
        # sql = text('select name from user_t')
        # result = session.execute(sql)
        # for row in result:
        #     print(row)

        # stmt = update(User).where(User.id == 1).values(name = '测试修改')
        # session.execute(stmt)
        # session.execute(update(User), [
        #     {'id':1, 'name': '张三'},
        #     {'id':2, 'name': '王五'}
        # ])
