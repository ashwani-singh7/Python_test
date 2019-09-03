
class LotteryPlayer(object):
	"""docstring for LotteryPlayer"""
	def __init__(self, name):
		self.name = name
		self.number = (45,68,74,29)

	def sum(self):
		return sum(self.number)

player = LotteryPlayer('ashu')
player2 = LotteryPlayer('mohan')

print(player.name)
print(player.number)
print(player2.name)
print(player.sum())