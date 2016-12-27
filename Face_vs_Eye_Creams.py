
# coding: utf-8

# In[37]:

face = input('List of ingredients for face cream? ')
facelist = face.split(", ")

eye = input('List of ingredients for eye cream? ')
eyelist = eye.split(", ")

count = 0

print("--------------------------")

diff_ing_face = []
diff_ing_eye = []

for item in facelist:
    if item not in eyelist:
        diff_ing_face.append(item)
        count+=1
        
for item in eyelist:
    if item not in facelist:
        diff_ing_eye.append(item)
        count+=1
        
print("Unique ingredients in the face cream: \n" + str(diff_ing_face) + "\n")
print("Unique ingredients in the eye cream: \n" + str(diff_ing_eye) + "\n")
print("Number of differing ingredients: ")
print(count)


# In[ ]:




# In[ ]:




# In[ ]:



