from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from flask_cors import CORS
from product import Product
from productsRepository import ProductsRepository
from file import Image
from filesRepository import ImagesRepository

app = Flask(__name__) 
repository_product = ProductsRepository()
repository_image = ImagesRepository()

#Autorizar o front-end de realizar o CRUD com back-end
CORS(app)

##################################################################

#GET Endpoint - consultar dados de todos os produtos no banco
@app.route("/products", methods=["GET"])
def get_all_products():
    try:
        data = list(repository_product.read())

        for product in data:
            product["_id"] = str(product["_id"])
            product["fileName"] = str(product["fileName"])
            product["image"] = repository_image.read(product["fileName"])  
            
        
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    #Se houver erros no meio do processo
    except Exception as ex:
        print("********************************")
        print(ex)  
        print("********************************") 
        return Response(
            response=json.dumps({ "message": "Error ao consultar dados dos produtos!" }),
            status=500,
            mimetype="application/json"
        )

##################################################################

#POST Endpoint - Criar produto no banco
@app.route("/products", methods=["POST"])
def create_product():
    try:   
        #Criar uma instância nova da imagem para criar os dados no banco    
        image = Image(None, request.files["file"].filename, request.files["file"])  
        #Criar os dados no banco      
        repository_image.create(image)

        #Criar uma instância nova do produto para criar os dados no banco, com o id da imagem
        new_product = Product(None, request.form["name"], request.form["price"], image._id)
        #Criar os dados no banco 
        repository_product.create(new_product)

        #Responder para o front-end que foi criado os dados no banco
        return Response(
            response=json.dumps({ "message": "Produto criado com sucesso!" }),
            status=200,
            mimetype="application/json"
        )
    #Se houver erros no meio do processo
    except Exception as ex:
        print("********************************")
        print(ex)  
        print("********************************")
        return Response(
            response=json.dumps({ "message": "Error ao criar o produto" }),
            status=500,
            mimetype="application/json"
        )  

##################################################################

#PUT Endpoint - Atualização do produto no banco
@app.route("/products/<id>", methods=["PUT"])
def update_product(id):
    try:
        if not request.files.get('file', None):
            #Verificar se o usuário não enviou imagem
            #Após verificar, criar uma instância nova do projeto para atualizar os dados no banco
            new_product = Product(request.form["_id"], request.form["name"], request.form["price"], request.form["fileName"])
            dbResponse = repository_product.update(new_product)            
        else:
            #Verificar se o usuário enviou imagem  
            # Após verificar, deletar a imagem antiga no banco de dados,                    
            repository_image.delete(request.form["fileName"])

            # depois criar nova instância da imagem para enviar para o banco
            image = Image(None, request.files["file"].filename, request.files["file"])        
            repository_image.create(image)

            # após o envio dos dados, instânciar um novo produto com a nova id da imagem para atualizar o banco
            new_product = Product(request.form["_id"], request.form["name"], request.form["price"], image._id)
            dbResponse = repository_product.update(new_product) 

        #Verificar se atualizou no banco para enviar uma resposta ao front-end
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps({ "message": "Produto atualizado com sucesso!" }),
                status=200,
                mimetype="application/json"
            )
        #Se não atualizou, responder message "Sem atualização"
        return Response(
            response=json.dumps({ "message": "Sem atualização" }),
            status=200,
            mimetype="application/json"
        )
    #Se houver erros no meio do processo
    except Exception as ex:
        print("********************************")
        print(ex)  
        print("********************************")
        return Response(
            response=json.dumps({ "message": "Error ao atualizar o produto" }),
            status=500,
            mimetype="application/json"
        )
##################################################################

#DELETE Endpoint - Deletar o produto no banco
@app.route("/products/<id>", methods=["DELETE"])
def delete_product(id):
    try:    
        data = repository_product.read(id)        
        repository_image.delete(data["fileName"])
        dbResponse = repository_product.delete(id)

        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps({ "message": "Produto deletado com sucesso!" }),
                status=200,
                mimetype="application/json"
            )

        return Response(
                response=json.dumps({ "message": "Produto não encontrado!" }),
                status=400,
                mimetype="application/json"
            )
    #Se houver erros no meio do processo
    except Exception as ex:
        print("********************************")
        print(ex)  
        print("********************************") 
        return Response(
            response=json.dumps({ "message": "Error ao deletar o produto" }),
            status=500,
            mimetype="application/json"
        )

##################################################################

if __name__ == "__main__":
    app.run(port=80, debug=True)