from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentence1 = "Built a hotel booking website using react"
sentence2 = "experience with frontend Javascript framework"
sentence3 = "Managed a MySQL database for inventory tracking"

embeddings = model.encode([sentence1, sentence2, sentence3])

similarity_1_2 = util.cos_sim(embeddings[0],embeddings[1])
similarity_1_3 = util.cos_sim(embeddings[0],embeddings[2])

print("React vs Frontend JS frameworks:", similarity_1_2)
print("React vs MySQL database:", similarity_1_3)



