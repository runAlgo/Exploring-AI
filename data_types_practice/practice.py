# str: storing text
greeting = "Hello, Aitool!"
# print(greeting.upper()) # -> HELLO, AITOOL!

#int, float: numbers
age = 22
pi = 3.14159
area = pi * (5 ** 2) # circle area
# print(area)


# bool: flags
is_logged_in = True

# None: no value yet
user_avatar = None
# print(user_avatar)


## Collections ###
# list: shopping cart
cart = ["milk", "bread", "eggs"]
cart.append("butter")
# print(cart)



# touples: GPS coordinates (immutable)
home_location = (27.7172, 85.3240)
# print(home_location)

# range: batch processing 5 items
# for batch_id in range(5):
    # print(f"Processing bach {batch_id}")


# set: unique bashtags
hashtags = {"#AI", "#Python", "#AI"} # -> {"#AI", "#Python"}
# print(hashtags)


# dict: user profile
user = {"name": "Aitool", "country": "Nepal", "age": 22}
# print(user["country"]) # -> Nepal


###  Advanced / Specialized

from collections import defaultdict, Counter, deque, namedtuple

# defaultdict: count visitors by page
visitors = defaultdict(int)
visitors["/home"] += 1

# Counter: count words in text
text = "ai ai python data"
word_count = Counter(text.split()) # -> {'ai':2, 'python':1, 'data':1}
# print(word_count)


# deque: task queue
tasks = deque(["train_model", "serve_api"])
tasks.appendleft("download_data")
# print(tasks)


# namedtuple: representing a blog post
Post = namedtuple("Post", "title author")
p = Post("Learning Python", "Aitool")
# print(p)
# print(Post)



## Date, Time and Structured

from datetime import datetime, timedelta, date
from decimal import Decimal
from fractions import Fraction
import uuid

# datetime: logging
now = datetime.now()
# print(now.strftime("%y-%m-%d %H:%M"))


# timedelta: schedule task
tomorrow = now + timedelta(days=1)
# print(tomorrow)


# Decimal: money
price = Decimal("19.99")
tax = Decimal("1.25")
total = price + tax
# print(f"total price: {total}")


# Fraction: ratio (e.g., recipe)
ratio = Fraction(2, 3) # 2/3 cup sugar
# print(f"The ratio is: {ratio}")


# UUID: unique user id
user_id = uuid.uuid4()
# print(user_id)



##    Custom and Meta

from dataclasses import dataclass
from typing import List

@dataclass
class TodoItem:
    title: str
    done: bool = False

my_tasks: List[TodoItem] = [
    TodoItem("Study Python"),
    TodoItem("Build AI project", True)
]

# print(f"My Todo tasks: {my_tasks}")



##   File & I/O
from pathlib import Path

# Path: work with files
logs_dir = Path("logs")
# logs_dir.mkdir(exist_ok = True)
# (logs_dir / "app.log").write_text("App started")



### Concurrency / Async

import threading
import asyncio

# threading: background save
def save_file():
    print("Saving file in background...")
threading.Thread(target=save_file).start()

# asyncio: async web call simulation
async def fetch_data():
    await asyncio.sleep(1)
    return {"status": "ok"}

result = asyncio.run(fetch_data())
print(result)