import json
import random
def random_select():
	white_cards =["The prosecutor fallacy","catastrophic forgetting","predatory bootcamps","Adversarial examples","Differential privacy","50+ billion parameters", "skipping on a multiple testing correction","Deep learning celebrities","Random noise","Optimizing the most convenient objective",
	"The Neurips random ballot","plush giraffe perturbation","pretraining","1000 GPUs", "information bottleneck","A theorem","Relational bias","Dataset selection","Learning more math", "Mathiness","Gradient explosion"
	"Non-parametric","Huggingface","Causality","Deep fakes","Checking arXiv obsessively","Moving sliders at http://distill.pub/","Sunday night deadlines","learning on the edge","Sparsity","OpenReview"]
	black_cards =["Deep ___", "_______is the largest model trained yet","your baseline experiment should include____","All i want in life is ___",
	"_____ is the problem, ____is the solution","______ is just an attention mechanism","Deep Generative Models are all about____","Anyone else having problems with ____today, or is it just me","Training ______ is easy; just use _______","Artificial General Intelligence will be solved by ______","______ achieves superhuman performance", "My start-up applies ___ to solve _________"]
	#print(len(white_cards))
	#print(len(black_cards))
	all_cards =white_cards+black_cards
	#print(len(all_cards))
	seen ={ }
	file_name ="seen_cards.json"
	file =random.choice(all_cards)
	with open(file_name) as json_file:
		data =json.load(json_file)	
	if file not in data.keys():
		seen[file] =0
		data.update(seen)
		with open(file_name, 'r+') as fp:
			json.dump(data,fp)			
	
	else:
		file =random.choice(all_cards)		
		data[file] +=0
		with open(file_name, 'r+') as fp:
			json.dump(data,fp)	
	recommended ='{} is the topic you are exploring today. '.format(file)		
	return recommended
print(random_select())