from .puzzle.puzzle import Puzzle

quote = 'There is something that is much more scarce, something rarer than ability. It is the ability to recognize ability.'
legend = {3:'E',7:'O',8:'M'}
cipher = Puzzle(quote, legend)

code = cipher.get_puzzle()

print(code)