import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Categories, Items, Users

# Configure SQLAlchemy engine
engine = create_engine('sqlite:///catalog.db')

# Bind engine to metadata of Base class
Base.metadata.bind = engine

# Create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# User
if os.environ.get('USER_NAME') and os.environ.get('USER_EMAIL'):
    user_name = os.environ.get('USER_NAME')
    user_email = os.environ.get('USER_EMAIL')
else:
    # Request input from user
    print('\n', 'Provide credentials to be used when populating the database')
    user_name = input('Please enter your name: ')
    user_email = input('Please enter your email address: ')
# Query database for user email
user_email_in_db = (session.query(Users.email)
                    .filter_by(email=user_email)
                    .all())
if user_email_in_db:
    print('User {} already in database.'.format(user_email))
    user = Users(name=user_name, email=user_email)
else:
    # Create new user
    new_user = Users(name=user_name, email=user_email)
    session.add(new_user)
    session.commit()
    print('User {} successfully added to database.'.format(new_user.email))
    user = new_user


# Categories
def check_db_for_category(category):
    """Helper function to check database for category before adding."""
    # Query database for category
    category_in_db = (session.query(Categories.name)
                      .filter_by(name=category.name)
                      .all())
    # If the category name is already present in the database, don't add it
    if category_in_db:
        print('Category "{}" already in database.'.format(category.name))
    # Else, add category to database
    else:
        session.add(category)
        session.commit()
        print('Category "{}" added to database.'.format(category.name))


category = Categories(name='Jackets and coats', user=user)
check_db_for_category(category)
# Create object for database category so items below can be added
Jackets = session.query(Categories).filter_by(name='Jackets and coats').one()

category = Categories(name='Trousers and shorts', user=user)
check_db_for_category(category)
# Create object for database category so items below can be added
Trousers = session.query(Categories).filter_by(name='Trousers and shorts').one()

category = Categories(name='Underwear', user=user)
check_db_for_category(category)
# Create object for database category so items below can be added
Underwear = session.query(Categories).filter_by(name='Underwear').one()


category = Categories(name='Suits', user=user)
check_db_for_category(category)
# Create object for database category so items below can be added
Suits = session.query(Categories).filter_by(name='Suits').one()

# Items
def check_db_for_item(item):
    """Helper function to check database for item before adding."""
    # Check database for item
    item_in_db = (session.query(Items.name)
                  .filter_by(name=item.name)
                  .all())
    # If the item name is already present in the database, don't add it
    if item_in_db:
        print('Item "{}" already in database.'.format(item.name))
    # Else, add item to database
    else:
        session.add(item)
        session.commit()
        print('Item "{}" added to database.'.format(item.name))

item = Items(name='ASOS DESIGN trousers ',
             description=('ASOS DESIGN utility trousers '
                          ' ASOS DESIGN utility trousers .'),
             category=Trousers,
             user=user)
check_db_for_item(item)


print('Database population complete.', '\n')
