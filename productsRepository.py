from pymongo import MongoClient
from bson.objectid import ObjectId

class ProductsRepository(object):
    
    def __init__(self):
        # Inicializar o MongoDB, configurando a porta, host e database, para ter acesso aos databases e collections
        self.client = MongoClient(host='localhost', port=27017)        
        self.database = self.client['devmarket']


    def create(self, product):
        #Cria se tem produto
        if product is not None:
            self.database.products.insert_one(product.get_as_json())            
        else:
            raise Exception("Sem parâmetro não tem como salvar")


    def read(self, _id = None):
        #Consultar todos os produtos
        if _id is not None:
            return self.database.products.find_one({"_id": ObjectId(_id)})
        else:
            return self.database.products.find()


    def update(self, product):
        if product is not None:
            # Atualizar se tiver produto
            return self.database.products.update_one(
                {"_id": ObjectId(product._id)},
                {"$set": {"name": product.name, "price": product.price, "fileName": ObjectId(product.fileName)}}                    
            )           
        else:
            raise Exception("Sem atualização, pois está sem parâmetro.")


    def delete(self, _id):
        print(_id)
        #Deletar se tiver parâmetro, pois será necessário o _id do produto para deletar
        if _id is not None:
            return self.database.products.delete_one({"_id": ObjectId(_id)})
        else:
            raise Exception("Sem parâmetro não tem como deletar.")