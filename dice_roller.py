import random
import time

def main():
	dice_rolls = int(input("你想掷几次骰子？"))
	dice_size = int(input("骰子最高设置几点？"))
	dice_sum = 0
	for i in range(0, dice_rolls):
		roll = random.randint(1, dice_size)
		dice_sum += roll
		if roll == 1:
			print(f'差劲，掷到 {roll} 点了。。。')
		elif roll == 6:
			print(f'不错，掷到 {roll} 点了!')
		else:
			print(f'你掷到了 {roll} 点')
		time.sleep(0.5)
	print(f"你一共掷到 {dice_sum} 点！")

if __name__== "__main__":
	main()