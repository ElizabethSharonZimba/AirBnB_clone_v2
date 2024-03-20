#!/usr/bin/python3
"""
This module manages the database connection and operations using SQLAlchemy.
"""

from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base

class DBStorage:
    """
    Manages the database connection and operations.
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """
        Initializes the DBStorage instance.
        """
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = f"mysql+mysqldb://{username}:{password}@{host}/{database_name}"
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects of a specified class from the database.
        """
        objs_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objs_list.extend(self.__session.query(subclass).all())
        obj_dict = {}
        for obj in objs_list:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """
        Adds a new object to the current session.
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
        Commits changes to the current session.
        """
        self.__session.commit()    

    def delete(self, obj=None):
        """
        Deletes an object from the current session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the database session.
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

