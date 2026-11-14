class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)       # val -> current frequency
        self.stacks = defaultdict(list)    # frequency -> stack of vals
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        curr_freq = self.freq[val]

        self.stacks[curr_freq].append(val)
        self.max_freq = max(self.max_freq, curr_freq)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1

        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()