from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,distinct
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('mysql+pymysql://onlineTest_zhiyi:NnNdHCbTY8sDS7Zi@111.230.27.166:3306/onlineTest_zhiyi?charset=utf8')

Session = sessionmaker(bind=engine)
Base = declarative_base()


session = Session()


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    type = Column(String(300))
    time = Column(String(300))
    context = Column(String(300))

    def __init__(self, id, title, type, time, context):
        self.id = id
        self.title = title
        self.type = type
        self.time = time
        self.context = context

    def __repr__(self):
        return "<news(id='%s', title='%s',type='%s',time='%s',context='%s')>" % (
            self.id, self.title, self.type,self.time,self.context)


if __name__ == '__main__':
    users=session.query(News).all()
    print(users)
