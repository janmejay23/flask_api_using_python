
# coding: utf-8

# In[1]:


from flask import Flask
from flask_restful import Api,Resource,reqparse

app=Flask(__name__)
api=Api(app)






# In[2]:


users=[{"name":"jay",
      "age": 29
      },
     {"name":"jay1",
     "age" : 28
     }
]


# In[3]:


users


# In[5]:


class User(Resource):
    def get(self,name):
        for user in users:
            if (name==user["name"]):
                return user,200
            return "user not found",404
            
    def put(self,name):
        parser=reqparse.ReqParser()
        parser.add_argument("age")
        args=parser.parse_args()
        for user in users:
            if(name==user["name"]):
                user["age"]=args["age"]
                return user,200
        user={
            "name":name,
        "age":args["age"]
        }
        users.append(user)
        return user,201
        
    def post(self,name):
        parser=reqparse.RequestParser()
        parser.add_argument("age")
        args=parser.parse_args()
        
        for user in users:
            if(name==user["name"]):
                return "user with name{} already exist".format(name),400
        user={
            "name":name,
            "age":args["age"],
        }
        users.append(user)
        return user,201
        
    def delete(self,name):
        global users
        users=[user for user in users if user["name"]!=name]
        return"{}is deleted".format(name),200


# In[6]:


api.add_resource(User,"/user/<string:name>")
app.run(debug=True)

