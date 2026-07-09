from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Sequence, Optional, TypeVar, Generic, Self
import json
from pathlib import Path

T = TypeVar('T')

@dataclass
class User:
    id: int
    name: str
    login: str
    password: str = field(repr = False)
    email: Optional[str] = None
    address: Optional[str] = None

    def __lt__(self, other: Self) -> bool:
        return self.name < other.name
    
    
class IDataRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> Sequence[T]:
        ...
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        ...
    
    @abstractmethod
    def add(self, item: T) -> None:
        ...
    
    @abstractmethod
    def update(self, item: T) -> None:
        ...
    
    @abstractmethod
    def delete(self, item: T) -> None:
        ...


class IUserRepository(IDataRepository[User]):
    @abstractmethod
    def get_by_login(self, login: str) -> Optional[User]:
        ...
    

class DataRepository(Generic[T]):
    def __init__(self, file_path: str, cls_type: T) -> None:
        self.file_path = Path(file_path)
        self.cls_type = cls_type

        if not self.file_path.exists():
            self._save_all([])

        self.all_users = self.get_all()

    def get_all(self) -> Sequence[User]:
        with open(self.file_path, "r", encoding = "utf-8") as f:
            data = json.load(f)
        
        return [self.cls_type(**user) for user in data]

    def get_by_id(self, id: int) -> Optional[User]:
        all_users = self.get_all()

        for user in all_users:
            if user.id == id: return user
        return None

    def add(self, user: User) -> None:
        if self.get_by_id(user.id) is not None:
            raise ValueError('Item with this id is already exist')
        self.all_users.append(user)
        self._save_all(self.all_users)

    def update(self, user: User) -> None:
        user_index = self.all_users.index(user)
        self.all_users[user_index] = user
        self._save_all(self.all_users)

    def delete(self, user: User) -> None:
        self.all_users.remove(user)
        self._save_all(self.all_users)

    def _save_all(self, users: Sequence[T]) -> None:
        with open(self.file_path, "w", encoding = "utf-8") as f:
            json.dump([asdict(i) for i in users], f, indent = 2)

    
class UserRepository(DataRepository[User]):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path, User)
    
    def get_by_login(self, login: str) -> Optional[User]:
        users = self.get_all()
        for user in users:
            if user.login == login:
                return user
        return None


class IAuthService(ABC):    
    @abstractmethod
    def sign_in(self, user: User) -> None:
        pass
    
    @abstractmethod
    def sign_out(self, user: User) -> None:
        pass

    @property
    @abstractmethod
    def is_authorized(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def current_user(self) -> Optional[User]:
        pass


@dataclass
class Session:
    id: int


class SessionRepository(DataRepository[Session]):
    def __init__(self, file_path: str):
        super().__init__(file_path, Session)
    
    def get_session_by_user_id(self, user_id: int) -> Optional[Session]:
        for session in self.get_all():
            if session.id == user_id:
                return session
        return None


class AuthService(IAuthService):
    def __init__(self, auth_path: str, repo_path: str):
        self.session_repo = SessionRepository(auth_path)
        self.user_repo = UserRepository(repo_path)
    
    def sign_in(self, user: User) -> None:
        if self.is_authorized():
            print("Firstly sign out")
            return
        if self.user_repo.get_by_id(user.id) is None:
            print("That user doesn't exist")
            return
        self.session_repo.add(Session(user.id))
    
    def sign_out(self, user: User) -> None:
        session = self.session_repo.get_session_by_user_id(user.id)
        if not session:
            print(f"{user.name} is not sign in")
            return
        self.session_repo.delete(Session(user.id))
    
    def is_authorized(self) -> bool:
        return len(self.session_repo.get_all()) > 0
    
    def current_user(self) -> Optional[User]:
        sessions = self.session_repo.get_all()
        if not sessions:
            return None
        last_session = sessions[-1]
        return self.user_repo.get_by_id(last_session.id)
    

repo_path = "users.json"
auth_path = "user.json"

auth_service = AuthService(auth_path, repo_path)
repo = UserRepository(repo_path)

user1 = User(id = 1, name = "Angelika", login = "fanatka_Ishanova_ZXC", password = "dy/dx = f(x)", email = "deadInsideGirl@mail.ru")
user2 = User(id = 2, name = "Anton", login = "StarBoy", password = "1111111111111")
repo.add(user1)
repo.add(user2)
print("Все пользователи после добавления:")
print(repo.get_all())

user1.email = "NotdeadInsideGirl@mail.ru"
repo.update(user1)
print("\nПосле редактирования Angelika:")
print(repo.get_by_id(1))

auth_service.sign_in(user1)
print("\nis_autorized?:", auth_service.is_authorized())
print("Текущий пользователь:")
print(auth_service.current_user())

auth_service.sign_out(user1)

auth_service.sign_in(user2)
print("\nПосле авторизации Anton:")
print(auth_service.current_user())

auth_service2 = AuthService(auth_path, repo_path)
print("\nПосле перезапуска программы (автоавторизация):")
print(auth_service2.current_user())

#auth_service.sign_out(user2)
print("\nПосле выхода Anton:")
print(auth_service.current_user())

# auth_service2 = AuthService(auth_path, repo_path)
# print(auth_service2.current_user())