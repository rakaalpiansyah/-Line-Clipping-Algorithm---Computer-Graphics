class LiangBarsky:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def clip(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        
        # Parameter p dan q sesuai rumus Liang-Barsky [cite: 406-409]
        p = [-dx, dx, -dy, dy]
        q = [x1 - self.x_min, self.x_max - x1, y1 - self.y_min, self.y_max - y1]
        
        u1, u2 = 0.0, 1.0

        for i in range(4):
            if p[i] == 0:
                if q[i] < 0: return None # Paralel di luar [cite: 412]
            else:
                r = q[i] / p[i]
                if p[i] < 0:
                    u1 = max(u1, r) # Titik masuk [cite: 421]
                else:
                    u2 = min(u2, r) # Titik keluar [cite: 422]

        if u1 > u2:
            return None
        
        nx1 = x1 + u1 * dx
        ny1 = y1 + u1 * dy
        nx2 = x1 + u2 * dx
        ny2 = y1 + u2 * dy
        
        return (nx1, ny1, nx2, ny2)