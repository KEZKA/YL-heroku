import datetime
from sqlalchemy import orm, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from ..db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'))
    job = Column(String, nullable=True)
    work_size = Column(Integer, nullable=True, default=0)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime, default=datetime.datetime.now)
    is_finished = Column(Boolean, default=True)
    
    user = orm.relation('User')

    def __repr__(self):
        return f'<Job> {self.job}'
        