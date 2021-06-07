from flask import abort
class Post():
    
    POSTS=[
            {'id':1,'title':'First Post','content':' This is My First Post' },
            {'id':2,'title':'Second Post','content':' This is My Second Post' },
            {'id':3,'title':'third Post','content':' This is My Third Post' }
        ]

    @classmethod
    def all(cls):
        return cls.POSTS    

    @classmethod
    def find(cls,id):
        try:
            return cls.POSTS[int(id) - 1] 
        except:
            abort(404)  
