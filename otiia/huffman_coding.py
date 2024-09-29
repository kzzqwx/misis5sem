import heapq

class Node:
    # класс для создания узла древа
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(chars, freq):
    # создание приоритетов
    priority_queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    # построение древа
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def generate_huffman_codes(node, code="", huffman_codes={}):
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

def get_freq(string, chars):
    freq = [0] * len(chars)

    # Проходим по каждому символу в строке
    for char in string:
        if char in chars:
            index = chars.index(char)  # Находим индекс символа
            freq[index] += 1  # Увеличиваем частоту

    return freq


# пример
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
example = "aabbbbbcdeeggggg"
freq = get_freq(example, chars)

root = build_huffman_tree(chars, freq)

huffman_codes = generate_huffman_codes(root)
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")