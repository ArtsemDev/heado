from datetime import datetime

from sqlalchemy import Column, VARCHAR, TEXT, TIMESTAMP

from .database import Base


class Contact(Base):
    name = Column(VARCHAR(64), nullable=False)
    email = Column(VARCHAR(128), nullable=False)
    message = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())

    def __repr__(self):
        return self.email
