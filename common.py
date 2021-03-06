from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

name = getenv("NAME")
assert name is not None

output = Path("output")
output.mkdir(exist_ok=True)

data = Path(f"MyFitbitData/{name}")
assert data.exists()


def save_plot(fig, name):
    fig.savefig(output / f"{name}.png", dpi=300, bbox_inches="tight")
