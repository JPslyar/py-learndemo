import shelve
from ClassTest import Person
db = shelve.open('classdb')
for key in sorted(db):
    print(key,'--->',db[key])
sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()