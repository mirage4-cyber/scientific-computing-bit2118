"""Small helper used by every task: saves the figure into docs/images and
shows it on screen when a window is available."""
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt

IMG = Path(__file__).resolve().parent.parent / "docs" / "images"


def finish(name):
    IMG.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(IMG / name, dpi=130)
    if matplotlib.get_backend().lower() != "agg":
        plt.show()
    plt.close()
