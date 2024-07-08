from models import Address, session, User

#Creating Users
user1 = User(name="John Doe", age=52)
user2 = User(name="Jane Smith", age=34)

#Creating addresses 
address1 = Address(city="New York", state="NY", zip_code="10001")
address2 = Address(city="Los Angeles", state="CA", zip_code="90001")
address3 = Address(city="Chicago", state="IL", zip_code="60601")

#Associating addresses with users
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

# Adding users and addresses to the session and comitting changes to the database 
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses = }")
print(f"{user2.addresses = }")
print(f"{address1.user = }")



""""

from sqlalchemy.orm import sessionmaker
from models import User, engine
import random
from sqlalchemy import  func

Session = sessionmaker(bind=engine)
session = Session()

""
only_iron_man = True
group_by_age = True

users = session.query(User)

if only_iron_man:
    users = users.filter(User.name == "Iron Man")

if group_by_age:
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f"User age: {user.age}, name: {user.name}")

""
SQL 
SELECT *
FROM users
WHERE name = "Iron Man"
GROUP BY age;
""
# Chaining
users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all() 
)

for age, count in users_tuple:
    print(f"Age: {age} - {count} users")

""
at SQL 
SELECT age, COUNT(id)
FROM users
WHERE age > 24 AND age < 50
GROUP BY age
ORDER BY "age";

# group users by age
users = session.query(User.name, func.count(User.id)).group_by(User.name).all()

print(users)

""
users = (
    session.query(User).where(
        or_(
            not_(User.name == "Iron Man"),
            and_(
                User.age > 35,
                User.age < 60
            )
        )
    )
).all()

for user in users:
    print(f"{user.age} - {user.name}")

""
users = session.query(User).where(User.name == "Iron Man").all()

for user in users:
    print(f"{user.age} - {user.name}")

""
users = session.query(User).where((User.age >= 30) & (User.name == "Iron Man") & (User.id > 4)).all()

for user in users:
    print(f"{user.age} - {user.name}")


""
users = session.query(User).where((User.age >= 30) | (User.name == "Iron Man")).all()

for user in users:
    print(f"{user.age} - {user.name}")


""
# Mengambil semua pengguna dengan umur lebih besar atau sama dengan 30
users = session.query(User).filter(User.age >= 30).all()

for user in users:
    print(f"User age: {user.age}")



# Mengambil semua pengguna dengan umur yang sama dengan 25
users = session.query(User).filter_by(age>=25).all()

for user in users:
    print(f"user age: {user.age}")
"""

"""
# Mengambil semua pengguna
users_all = session.query(User).all()

# Mengambil semua pengguna dengan umur lebih besar atau sama dengan 25 dan nama "Iron Man"
users_filtered = session.query(User).filter(User.age >= 25, User.name == "Iron Man").all()

print("All Users:", len(users_all))
print("Filtered Users:", len(users_filtered))


# Mengambil semua pengguna dan mengurutkannya berdasarkan umur dan nama secara ascending
users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print(f"User age : {user.age}, name: {user.name}, id: {user.id}")

# Mengambil semua pengguna dan mengurutkannya berdasarkan umur secara ascending
users = session.query(User).order_by(User.age).all()

for user in users:
    print(f"User age : {user.age}, name: {user.name}, id: {user.id}")

# Menambahkan data pengguna acak ke dalam database
names = ["Andrew Pip", "Iron Man", "John Doe", "Jane Doe"]
ages = [20, 21, 22, 23, 25, 27, 30, 35, 60]

for x in range(20):
    user = User(name=random.choice(names), age=random.choice(ages))
    session.add(user)

session.commit()
"""