from pymongo import MongoClient
from bson.objectid import ObjectId
import gridfs
import codecs

class ImagesRepository(object):
    
    def __init__(self):
        # Inicializar o MongoDB, configurando a porta, host e database, para ter acesso aos databases e collections
        self.client = MongoClient(host='localhost', port=27017)        
        self.database = self.client['devmarket']
        #Conectar gridFs com o banco para salvar a imagem no database devmarket
        self.fs = gridfs.GridFS(self.database)


    def create(self, image):
        #Cria se tem imagem
        if image is not None:
            self.fs.put(image.file, filename = image._id)                     
        else:
            raise Exception("Sem parâmetro não tem como salvar.")

    def read(self, _id):
        #Consultar imagem que contém id no filename
        file = self.fs.find_one({"filename": ObjectId(_id)})

        #Transformar a imagem em string binário. 
        #A tag "img" no front-end vai decodificar a string e transformar na imagem
        base64_data = codecs.encode(file.read(), 'base64')
        image = base64_data.decode('utf-8')

        return { "file_id": str(file._id), "img_code": image}

    def delete(self, _id):
        
        #Deletar se tiver parâmetro, pois será necessário o _id do produto para deletar
        if _id is not None:
            file_id = self.fs.find_one({"filename": ObjectId(_id)})._id        
            self.fs.delete(file_id)
        else:
            raise Exception("Sem parâmetro não tem como deletar.")