import re

def extract_and_average_it_per_s(file_path):
    pattern = r'Epoch 0:.*?(\d+\.\d+)it/s'
    it_per_s_values = []

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                it_per_s_values.append(float(match.group(1)))

    mean_it_per_s = sum(it_per_s_values) / len(it_per_s_values) if it_per_s_values else 0
    return mean_it_per_s

#Example usage:
mean_it_per_s = extract_and_average_it_per_s("C:\\Users\\Andi\\Desktop\\Bachelor\\etc\\a high quality rendering of a playmobil firefighter\\dreamfusion\\playmobil_Loss.txt")
print(mean_it_per_s)
