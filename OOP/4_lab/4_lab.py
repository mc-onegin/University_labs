from typing import Any, TypeVar, Generic
from abc import ABC, abstractmethod
from dataclasses import dataclass

TEventArgs = TypeVar("TEventArgs")

class EventHandler(ABC, Generic[TEventArgs]):
    @abstractmethod
    def handle(self, sender: object, args: TEventArgs) -> None:
        ...

class EventArgs(ABC):
    ...

@dataclass
class PropertyChangedEventArgs(EventArgs):
    property_name: str

@dataclass
class PropertyChangingEventArgs(EventArgs):
    property_name: str
    old_value: Any
    new_value: Any
    can_change: bool = True

class Event(Generic[TEventArgs]):
    def __init__(self) -> None:
        self._handlers: list[EventHandler[TEventArgs]] = []

    def __iadd__(self, handler: EventHandler[TEventArgs]) -> 'Event[TEventArgs]':
        if handler not in self._handlers:
            self._handlers.append(handler)
        return self

    def __isub__(self, handler: EventHandler[TEventArgs]) -> 'Event[TEventArgs]':
        if handler in self._handlers:
            self._handlers.remove(handler)
        return self
    
    def invoke(self, sender: object, args: TEventArgs) -> None:
        for handler in self._handlers:
            handler.handle(sender, args)

    __call__ = invoke

class PrintHandler(EventHandler[PropertyChangedEventArgs]):
    def handle(self, sender: object, args: PropertyChangedEventArgs) -> None:
        print(f"[{sender}] changed {args.property_name}")


class ValidationHandler(EventHandler[PropertyChangingEventArgs]):
    def handle(self, sender: object, args: PropertyChangingEventArgs) -> None:
        args.can_change = not (args.new_value == "" or args.property_name.startswith("_"))


class ValidationHandler_2(EventHandler[PropertyChangingEventArgs]):
    def __init__(self, max_size: int, property_name: str) -> None:
        self.max_size = max_size
        self.property_name = property_name

    def handle(self, sender: object, args: PropertyChangingEventArgs) -> None:
        if not (isinstance(args.new_value, int) and self.property_name == 'size'):
            return
        if args.new_value >= self.max_size:
            return
        
        args.can_change = False
        print(f"{self.property_name} can't be higher than {self.max_size}")
            

class PropertyNotifierMixin:
    def __init__(self) -> None:
        self.property_changing = Event[PropertyChangingEventArgs]()
        self.property_changed = Event[PropertyChangedEventArgs]()

    def __setattr__(self, field_name: str, new_value: Any) -> None:
        if not hasattr(self, "property_changing"):
            super().__setattr__(field_name, new_value)
            return
            
        old_value = getattr(self, field_name, None)

        args_before = PropertyChangingEventArgs(field_name, old_value, new_value)
        self.property_changing(self, args_before)
        if not args_before.can_change:
            return

        super().__setattr__(field_name, new_value)

        args_after = PropertyChangedEventArgs(field_name)
        self.property_changed(self, args_after)


class Dog(PropertyNotifierMixin):
    def __init__(self, name: str, breed: str, sleep: bool) -> None:
        super().__init__()
        self.name = name
        self.breed = breed
        self._sleep = sleep


class turtle(PropertyNotifierMixin):
    def __init__(self, name: str, size: int, the_number_of_times_playing_curling_by_turtle: int) -> None:
        super().__init__()
        self.name = name
        self.size = size
        self._the_number_of_times_playing_curling_by_turtle = the_number_of_times_playing_curling_by_turtle



print_handler = PrintHandler()
valid1_handler = ValidationHandler()
valid2_handler = ValidationHandler_2(90, 'size')

d = Dog("Marussia", "sobaka", 1)

print("Testing Dog:")
d.property_changed += print_handler
d.property_changing += valid1_handler

d.breed = "sleep_dog"
d._sleep = 0

print("\nTesting turtle:")

t = turtle("Natashka", 100, 0)

t.property_changed += print_handler
t.property_changing += valid1_handler
t.property_changing += valid2_handler

t.name = "Pashka"
t.size = 85
t.property_changing -= valid2_handler
t._the_number_of_times_playing_curling_by_turtle = 1

#t.property_changed -= print_handler
t.property_changing -= valid1_handler

t._the_number_of_times_playing_curling_by_turtle = 1

class a():
    def __init__(self):
        self.x = 2
    def __getattr__(self, name):
        return f"Сработал __getattr__  {name}"

    def __getattribute__(self, name):
        print("сработал getattribute")
        return super().__getattribute__(name)
    
b = a()
# b.c = 1
# print(b.c)
# print(b.d)


print(b.x)
print(b.y)
