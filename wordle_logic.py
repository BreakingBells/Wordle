import random

# --- WORD LIST ---
WORDS = [
    "aback","abase","abate","abbey","abbot","abhor","abide","abled","abode","abort",
    "about","above","abuse","abyss","acorn","acrid","actor","acute","adage","adapt",
    # (you can keep your full list here)
]

GREEN = "green"
YELLOW = "yellow"
GRAY = "gray"

class WordleGame:
    def __init__(self):
        self.answer = random.choice(WORDS)
        self.attempts = []
        self.max_attempts = 6

    def check_guess(self, guess):
        guess = guess.lower()
        answer = self.answer

        result = []
        used = [False] * 5

        # First pass: greens
        for i, ch in enumerate(guess):
            if ch == answer[i]:
                result.append((ch, GREEN))
                used[i] = True
            else:
                result.append((ch, None))

        # Second pass: yellows
        for i, (ch, color) in enumerate(result):
            if color is not None:
                continue
            found = False
            for j, a_ch in enumerate(answer):
                if not used[j] and ch == a_ch:
                    used[j] = True
                    found = True
                    break
            result[i] = (ch, YELLOW if found else GRAY)

        self.attempts.append(result)
        return result

    def is_won(self):
        if not self.attempts:
            return False
        return all(color == GREEN for _, color in self.attempts[-1])

    def is_lost(self):
        return len(self.attempts) >= self.max_attempts and not self.is_won()
