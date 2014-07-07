from semanticpy.vector_space import VectorSpace

vector_space = VectorSpace(["The rat  in the hat disabled", "A cat is a fine pet ponies.", "cat and cats make good pets.","I haven't got a hat."])

#Search for cat
print vector_space.search(["cat rats rat"])

#Show score for relatedness against document 0
print vector_space.related(0)
