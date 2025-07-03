
d={}  # Emppty dictionary

marks={ 
  "Harry":100,
  "Pradip":95,
  "Subham":92,
  0:"Madhu"
}
# print(marks["Harry"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())


marks.update({"Harry":99,"Renuka":99})
print(marks)
print(marks.get("Harry2"))#prints none
print(marks["Harry2"])  #Returns an error