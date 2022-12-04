from libros0 import libro 


def insertLibro(nombre, autor, precio):
    db = libro()
    cursor =db.cursor()
    st = 'INSERT INTO LIBROS(nombre, autor, precio) VALUES(?, ?, ?)' 
    cursor.execute(st, [nombre,autor,precio]) 
    db.commit()
    return True 

def updateLibros(id, nombre, autor, precio):
    db =libro()
    cursor =db.cursor()
    st ='UPDATE LIBROS set nombre =?, autor =?, precio=? WHERE id = ?'
    cursor.execute(st, [id, nombre, autor, precio])
    db.commit()
    return True


def deleteLibros(id):
    db=libro()
    cursor=db.cursor()
    st = 'DELETE FROM LIBROS WHERE id = ?'
    cursor.execute(st, [id])
    return True 

def selec_libros(id):
    db = libro()
    cursor = db.cursor()
    st = "SELECT id, nombre, autor, precio FROM LIBROS WHERE id = ?"
    cursor.execute(st, [id])
    return cursor.fetchone()



def get_libros():
    db =libro()
    cursor = db.cursor()
    query = 'SELECT id, nombre, autor, precio FROM LIBROS'
    cursor.execute(query)
    return cursor.fetchall()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    