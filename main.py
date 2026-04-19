import matplotlib.pyplot as plt
from algorithms.cohen_sutherland import CohenSutherland
from algorithms.liang_barsky import LiangBarsky
from utils.config import WINDOW, TEST_LINES, THEME

class ClippingApp:
    def __init__(self):
        self.win = WINDOW
        # Inisialisasi Clipper
        self.clippers = {
            "Cohen-Sutherland": CohenSutherland(**WINDOW),
            "Liang-Barsky": LiangBarsky(**WINDOW)
        }

    def render(self):
        fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor='#F4F7F6')
        
        # Metadata Header
        fig.text(0.5, 0.95, "Tugas Grafika Komputer: Line Clipping Implementation", 
                 ha='center', fontsize=16, fontweight='bold', color='#2C3E50')

        for ax, (name, clipper) in zip(axes, self.clippers.items()):
            self._setup_plot(ax, name)
            
            for line in TEST_LINES:
                p1, p2 = line["p1"], line["p2"]
                
                # Plot Garis Asli (Shadow)
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=THEME["original_line"], 
                        linestyle=':', alpha=0.5, label='_nolegend_')
                
                # Proses Kliping
                result = clipper.clip(p1[0], p1[1], p2[0], p2[1])
                
                if result:
                    ax.plot([result[0], result[2]], [result[1], result[3]], 
                            color=THEME["clipped_line"], linewidth=2.5, marker='o', markersize=4)
                    # Label teks di tengah garis
                    ax.text((result[0]+result[2])/2, (result[1]+result[3])/2, line["name"], 
                            fontsize=8, fontweight='bold')

        plt.subplots_adjust(top=0.85, bottom=0.1)
        plt.show()

    def _setup_plot(self, ax, title):
        # Window Area [cite: 86]
        rect = plt.Rectangle((self.win["x_min"], self.win["y_min"]), 
                             self.win["x_max"]-self.win["x_min"], 
                             self.win["y_max"]-self.win["y_min"], 
                             edgecolor=THEME["window_edge"], fill=False, 
                             linewidth=2, linestyle='--', label='Clip Region')
        ax.add_patch(rect)
        
        ax.set_title(f"Metode: {title}", pad=15, fontsize=12, fontweight='bold')
        ax.set_xlim(-1, 12)
        ax.set_ylim(-1, 11)
        ax.grid(True, color=THEME["grid_color"], alpha=0.5)
        ax.set_xlabel("X Coordinate")
        ax.set_ylabel("Y Coordinate")
        ax.legend(loc='upper right', fontsize='small')

if __name__ == "__main__":
    app = ClippingApp()
    app.render()