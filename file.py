from bson.objectid import ObjectId

""" Classe da imagem, os dados da imagem serão usadas para armazenar no banco """
class Image(object):

    def __init__(self, _id = None, fileName = None, file = None):
        #Se não tem id, o construtor cria
        if _id is None:
            self._id = ObjectId()           
        else:
            self._id = _id        
        self.fileName = fileName
        self.file = file

    def get_as_json(self):
        """ Retorna o objeto da classe em JSON """
        return self.__dict__