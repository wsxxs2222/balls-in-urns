import easier_case as ez
import experiment_urns as expr
import most_general as mg
from matplotlib import pyplot as plt
prob_list1 = ez.pdf_function(30,100,100)
prob_list2 = mg.most_general(100,100,1,1,30)


x1 = [i for i in range(31)]
#plt.figure(figsize=(28,8))
figure, axis = plt.subplots(2,2)
axis[0,0].bar(x1, prob_list1, color='green')
axis[0,0].set_xlabel("i")
axis[0,0].set_ylabel("P(X=i)")
axis[0,0].set_title("pdf of super preferential, n=50,R=100,W=70")

axis[0,1].bar(x1,prob_list2, color="red")

plt.show()