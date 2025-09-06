import matplotlib.pyplot as plt

def save_line_chart(x, y, out_path):
    plt.figure(figsize=(6,3))
    plt.plot(x, y)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
