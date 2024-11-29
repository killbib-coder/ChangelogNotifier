from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import json

Base = declarative_base()

with open('.config.json', 'r') as config_file:
    config_data = json.load(config_file)
db_name, db_user, db_password = config_data.get('database', {}).get('name'), config_data.get('database', {}).get('user'), config_data.get('database', {}).get('password')

db_url = f"postgresql://{db_user}:{db_password}@localhost/{db_name}"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

user_tools = Table(
    'user_tools', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('tool_id', Integer, ForeignKey('tools.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    followed_tools = relationship("Tool", secondary=user_tools, back_populates="followers")

class Tool(Base):
    __tablename__ = 'tools'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    url = Column(String(255), nullable=False)
    version_path = Column(String(255), nullable=False)
    link_path = Column(String(255), nullable=False)
    version = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    followers = relationship("User", secondary=user_tools, back_populates="followed_tools")


class DatabaseManager:
    def __init__(self, db_url=db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all_users(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            return [user for user in users]
        except Exception as e:
            print(f"[-] DatabaseManager - Error getting users: {e}")
        finally:
            session.close()

    def get_all_tools(self):
        session = self.Session()
        try:
            tools = session.query(Tool).all()
            return [tool for tool in tools]
        except Exception as e:
            print(f"[-] DatabaseManager - Error getting tools: {e}")
        finally:
            session.close()

    def get_all_user_tools(self):
        session = self.Session()
        try:
            user_tools_list = session.query(user_tools).all()
            return [ut for ut in user_tools_list]
        except Exception as e:
            print(f"[-] DatabaseManager - Error getting user_tools: {e}")
        finally:
            session.close()

    def get_tool_ids_by_user(self, user_id):
        session = self.Session()
        try:
            result = session.query(user_tools.c.tool_id).filter(user_tools.c.user_id == user_id).all()

            return [row[0] for row in result] if result else None
        except Exception as e:
            print(f"[-] DatabaseManager - Error getting tool ids for user_id {user_id}: {e}")
            return None
        finally:
            session.close()


    def get_tool_by_id(self, tool_id):
        session = self.Session()
        try:
            tool = session.query(Tool).filter(Tool.id == tool_id).first()
            return tool
        except Exception as e:
            print(f"[-] DatabaseManager - Error getting tool by id {tool_id}: {e}")
        finally:
            session.close()

    def update_tool(self, tool):
        session = self.Session()
        try:
            existing_tool = session.query(Tool).filter(Tool.id == tool.id).first()
            if not existing_tool:
                print(f"[-] DatabaseManager - No tool found with id {tool.id}")
                return False

            existing_tool.name = tool.name
            existing_tool.url = tool.url
            existing_tool.version_path = tool.version_path
            existing_tool.link_path = tool.link_path
            existing_tool.version = tool.version
            existing_tool.link = tool.link

            session.commit()
            print(f"[+] DatabaseManager - {tool.name} has been updated")
            return True
        except Exception as e:
            print(f"[-] DatabaseManager - Error updating tool with id {tool.id}: {e}")
            session.rollback()
            return False
        finally:
            session.close()
