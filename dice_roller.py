import random
import time

def main():
	print("你想掷几次骰子？")
	while True:
		try:
			dice_rolls = input()
			input_teyp = int(dice_rolls)
			break
		except:
			print("输入的内容不规范，请重新输入：")
	dice_sum = 0
	rolls_count = [0, 0, 0, 0, 0, 0]
	start_time = time.perf_counter()
	for i in range(0, int(dice_rolls)):
		roll = random.randint(1, 6)
		dice_sum += roll
		tab_roll = "●" * int(roll)
		rolls_count[int(roll)-1] += 1
		# print(f'第 {i+1}  次\t--->  {tab_roll}')
		# time.sleep(0.01)
	end_time = time.perf_counter()
	print(f"在{end_time - start_time:8.3f} 秒内，你一共掷到 {dice_sum} 点！")
	print(f"●\t\t掷到 {rolls_count[0]} 次;")
	print(f"●●\t\t掷到 {rolls_count[1]} 次;")
	print(f"●●●\t\t掷到 {rolls_count[2]} 次;")
	print(f"●●●●\t掷到 {rolls_count[3]} 次;")
	print(f"●●●●●\t掷到 {rolls_count[4]} 次;")
	print(f"●●●●●●\t掷到 {rolls_count[5]} 次;")
	enter_close = input("请按回车结束程序")

if __name__== "__main__":
	main()