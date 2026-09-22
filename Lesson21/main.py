from fastapi import FastAPI

app = FastAPI
@app.get("/")
def root():
    return {"message":"Hello,World!"}


@app.get("/items")
def read_items():
    return{"items":["kursi1","kursi2","kursi3"]}

@app.get("/items/{item_id}")
def read_items(item_id:int):
    return {"item_id":item_id}

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id, "name": "Gerti"}

@app.put("/items/{item_id}")
def update_item(item_id:int, name:str,price:float):
    return {"item_id":item_iid,"item_name":name, "item_price":price}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"message":"U fshi me sukses"}

