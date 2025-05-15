from pymongo import MongoClient

def paises():
    try:
        cliente = MongoClient('localhost', 27017)
        db = cliente['test_python']
        collection = db['info_paises']
        document = collection.find()
        return list(document)
    except Exception as e:
        print(f'[] ERROR: {e}')
    finally:
        cliente.close()

