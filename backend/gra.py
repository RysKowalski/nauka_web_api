from typing import Self
import os
import yaml

class Game:
	def __init__(self: Self, elements: list[str], name: str) -> None:
		with open(os.path.join('data', 'nauka_user_data.yaml'), 'r') as plik:
			user_data: dict = yaml.safe_load(plik)[name]
		
		if '|'.join(elements) in user_data['points']:
			self.max_points: int = user_data['points']['|'.join(elements)]['max_points']
			
			self.chances: list[str] = user_data['points']['|'.join(elements)]['chances']
			
		else:
			print('nie ma')
			
		self.points: int = 0
		
		self.questions: list[str] = []
		self.answers: list[str] = []

		with open(os.path.join('data', 'nauka_questions.yaml')) as plik:
			questions: dict = yaml.safe_load(plik)
			for element in elements:
				self.questions.append(questions[element]['names'])
				self.answers.append(questions[element]['data'])

		
		print(f'{user_data = } \n')
		print(f'{self.max_points = } \n')
		print(f'{self.chances = } \n')
		print(f'{self.questions = } \n')
		print(f'{self.answers = } \n')

class Instances:
	def __init__(self: Self) -> None:
		self.instances: dict[str, Game] = {}
	
	def new_instance(self: Self, name: str, elements: list[str]) -> None:
		new_instance: Game = Game(elements, name)
		self.instances[name] = new_instance


if __name__ == '__main__':
	instances: Instances = Instances()
	
	instances.new_instance('example_user', ['example', 'question'])
	
	print(instances.instances)
	
