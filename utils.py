from pathlib import Path

def read_input(day, split_lines=False):
    path = Path(__file__).parent / "inputs" / f"day{day:02d}.txt"
    text = path.read_text().strip()
    return text.split("\n") if split_lines else text