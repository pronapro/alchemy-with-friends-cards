from tkinter import *
import tkinter as tk
from datetime import datetime
import PIL 
import requests
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import json
import random

class Cardtoday():
	def random_select(self):
		white_cards =["The prosecutor fallacy","catastrophic forgetting","predatory bootcamps","Adversarial examples","Differential privacy","50+ billion parameters", "skipping on a multiple testing correction","Deep learning celebrities","Random noise","Optimizing the most convenient objective",
		"The Neurips random ballot","plush giraffe perturbation","pretraining","1000 GPUs", "information bottleneck","A theorem","Relational bias","Dataset selection","Learning more math", "Mathiness","Gradient explosion"
		"Non-parametric","Huggingface","Causality","Deep fakes","Checking arXiv obsessively","Data missing not at random", "meta-forgetting","Unsupervised auxiliary tasks","Geometric deep learning"
		"Moving sliders at http://distill.pub/","Sunday night deadlines","learning on the edge","Sparsity","OpenReview","a bigger, better Schmidhuler", "Deep learning for Dummies ", "Elmo and Bert"]
		black_cards =["Deep ___", "_______is the largest model trained yet","your baseline experiment should include____","All i want in life is ___",
		"_____ is the problem", "____is the solution","______ is just an attention mechanism","Deep Generative Models are all about____","Anyone else having problems with ____today, or is it just me","Training ______ is easy; just use _______","Artificial General Intelligence will be solved by ______","______ achieves superhuman performance", "My start-up applies ___ to solve _________"]
		#print(len(white_cards))
		#print(len(black_cards))
		all_cards =white_cards+black_cards
		#print(len(all_cards))
		self.seen ={ }
		self.file_name ="seen_cards.json"
		self.file =random.choice(all_cards)
		with open(self.file_name) as json_file:
			data =json.load(json_file)	
		if self.file not in data.keys():
			self.seen[self.file] =1
			data.update(self.seen)
			with open(self.file_name, 'r+') as fp:
				json.dump(data,fp)			
			self.re_card['text'] = self.file
			self.re_card['font'] =('verdana',20,'bold')
			self.message['text'] = len(data)
			self.message['font'] =('verdana',20,'bold')
			self.left['text'] = len(all_cards) -len(data)
			self.left['font'] =('verdana',20,'bold')
		elif self.file in data.keys():
					
			data[self.file] +=1
			self.file =random.choice(all_cards)

			with open(self.file_name, 'r+') as fp:
				json.dump(data,fp)	
			self.re_card['text'] = self.file
			self.re_card['font'] =('verdana',20,'bold')
			self.message['text'] = len(data)
			self.message['font'] =('verdana',20,'bold')
			l_data =lambda x: len(x) if len(x)<43 else 43
			self.left['text'] = len(all_cards) -l_data(data)
			self.left['font'] =('verdana',20,'bold')

	def __init__(self):
		self.root =tk.Tk()
		self.root.geometry('500x500')
		self.root.title("recommend card Application")
		self.root.maxsize(500,400)
		self.root.minsize(500,400)
		self.header =Label(self.root, width =100, height =2, bg = '#add8e6' )
		self.header.place(x=0,y=0)
		self.font =('verdana',10, 'bold')
		self.date =Label(self.root, text =datetime.now().date(), bg = '#add8e6',fg ="black", font =self.font)
		self.date.place(x=400,y =5)
		#self.heading =Label(self.root, text ='card recommended', bg='#00274c', fg ="white", font =self.font)
		#self.heading.place(x=180,y=5)
		self.napro =Label(self.root, text ='Napro Dev', bg = '#add8e6',fg ="black", font =self.font)
		self.napro.place(x=10,y=5)
		#self.img =ImageTk.PhotoImage(Image.open("icon.jpeg"))
		#self.image =Label(self.root, image =self.img)
		#self.image.place(x=20,y =40)

		self.name =Label(self.root, text ="Today's Topic",bg = '#add8e6', fg ="black", font =self.font)
		self.name.place(x=200,y=5)
		#self.car =Text(self.root, width =25, height =2)
		#self.car.place(x=140,y =70)
		self.button_label =Label(self.root, text ="Click button: ", fg ="black", font =self.font)
		self.button_label.place(x=100,y=73)
		self.button =Button(self.root,text ="Get Topic", bg ="#00274c",fg ="black", font =self.font,relief =RAISED, borderwidth =3, command =self.random_select)
		self.button.place(x =200,y =73)
		#self.line1 =Label(self.root,bg ="#00274c",width=20, height=0)
		#self.line1.place(x=0,y =150)
		#self.line2 =Label(self.root,bg ="#00274c",width=20, height=0)
		#self.line2.place(x=360,y =150)
		self.topic = Label(self.root, text="Topic",bg ="#add8e6", fg="black", padx=10)
		self.topic.place(x=200, y=150)
		self.re_card =Label(self.root, text ="NA/-", fg ="black", font =self.font)
		self.re_card.place(x=200,y=200)
		self.message_label =Label(self.root, text ="Seen Cards: ", fg ="black", font =self.font)
		self.message_label.place(x=30,y=250)
		self.message =Label(self.root, text ="NA/-", bg='#00274c', fg ="white", font =self.font)
		self.message.place(x=95,y=250)	
		self.left_cards =Label(self.root, text ="Remaining Cards: ",  fg ="black", font =self.font)
		self.left_cards.place(x=360,y=250)
		self.left =Label(self.root, text ="NA/-", bg='#00274c', fg ="white", font =self.font)
		self.left.place(x=450,y=250)
		self.text_ = "Learning something new daily"
		self.label_cards =Label(self.root, text =self.text_ ,  fg ="black", font =('verdana',25,'bold'))
		self.label_cards.place(x=50,y=300)		


		self.root.update()
		self.root.mainloop()
if __name__ == "__main__":
	Cardtoday()
