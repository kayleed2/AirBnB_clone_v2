#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from importlib_metadata import metadata
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.sql import text
import os


class DBStorage:
    """This class manages storage of hbnb models in SQL format"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates Instance into DBStorage"""
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                .format(dialect, driver, user, passwd, host,
                            db), pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            #We need to drop all tables, drop_all()?
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database session"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
        
        # if cls in the_class:
        #     objs.update({"{}.{}".format(cls.__name__, item.id): item
        #                  for item in self.__session.query(cls)})
        # elif cls is None:
        #     for (c) in the_class:
        #         objs.update({"{}.{}".format(c.__name__, item.id): item
        #                      for item in self.__session.query(c)})
        # return objs
        dictionary = {}
        if cls:
            # if type(cls) == str:
            #     cls = classes[cls]
            dic = self.__session.query(cls).all()
            for el in dic:
                key = el.__class__.__name__ + '.' + el.id
                dictionary[key] = el
        else:
            dic = self.__session.query(State).all()
            dic += self.__session.query(City).all()
            # dic += self.__session.query(Amenity).all()
            # dic += self.__session.query(Place).all()
            # dic += self.__session.query(Review).all()
            # dic += self.__session.query(User).all()
            for el in dic:
                key = el.__class__.__name__ + '.' + el.id
                dictionary[key] = el
            
            # for cls in classes.values():
            #     for i in self.__session.query(cls):
            #         dict[i.__class__.__name__ + '.' + i.id] = i
        return dictionary
    
    def new(self, obj):
        """add new object to DB"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to db session"""
        self.__session.commit()
        

    def delete(self, obj=None):
        """Delete object if exist"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
       """Creates all tables in database"""
       from models.base_model import BaseModel, Base
       from models.user import User
       from models.place import Place
       from models.state import State
       from models.city import City
       from models.amenity import Amenity
       from models.review import Review
       
       Base.metadata.create_all(self.__engine)
       Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
       self.__session = Session()


    def classes(self):
        """Defines classes"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                    }
        return classes
