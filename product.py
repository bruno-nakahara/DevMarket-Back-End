from bson.objectid import ObjectId

""" Classe do Produto, os dados do produto serão usadas para armazenar no banco """
class Product(object):

    def __init__(self, _id = None, name = None, price = None, fileName = None):
        #Se não tem id, o construtor cria
        if _id is None:
            self._id = ObjectId()           
        else:
            self._id = _id
        self.name = name                                              
        self.price = price
        self.fileName = fileName        

    def get_as_json(self):
        """ Retorna o objeto da classe em JSON """
        return self.__dict__