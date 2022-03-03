
# In-memory databse
### simple in-memory databse written in python


### how to run project:
```
git clone https://github.com/alinowrouzii/in-memory-db.git in-Memory-db && cd in-Memory-db
virtualenv venv && source venv/bin/activate
pip install -r requirements.txt
python inMemoryDB/main.py
```


### Example of commands:


Set value to a key
```
# set key value
set city_tehran_lat 35.715298
> OK
```


get value from a key
```
# get key
get city_tehran_lat
> 35.715298
```
delete key from db
```
# del key
del city_tehran_lat
> OK
```

search keys in db by regex
```
# keys regex
keys city_tehran.*
> ["city_tehran_lat", "city_tehran_lng"]
```
create or use db
```
# use db_name
use users_db
> OK
```

retrieve databases list
```
# list
list
> ["default", "users_db"]
```

show which database is in use
```
db
> default
```
get dump from db
```
# dump db_name path
dump default ./dumps/default
> OK
```

load db
```
# load path db_name
load ./dumps/default default
> OK
```
