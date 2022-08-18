#!/usr/bin/env python
# coding: utf-8

# In[52]:


from flask import Flask, request, render_template


# In[53]:


# __ by default is : reserved kw
app = Flask(__name__)


# In[54]:


import joblib


# In[55]:


# decorator: means can only run all these first then can run the function (todo before running function)

@app.route("/",methods=["GET", "POST"])
        

def index():
    if request.method == "POST": 
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html",result1=r1[0],result2=r2[0]))

    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[56]:


if __name__ == "__main__":
    app.run()


# In[ ]:




