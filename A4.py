Ddk=input()
Qt=[]
for X in Ddk:
  if X not in Qt:
    Qt.append(X)
  else:
    break  
print(len(Qt))
