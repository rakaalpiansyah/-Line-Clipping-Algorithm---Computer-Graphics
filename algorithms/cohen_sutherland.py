class CohenSutherland:
    # Definisi Region Codes (diambil dari materi kuliah) [cite: 208, 213, 214]
    INSIDE = 0  # 0000
    LEFT = 1    # 0001
    RIGHT = 2   # 0010
    BOTTOM = 4  # 0100
    TOP = 8     # 1000

    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def compute_code(self, x, y):
        code = self.INSIDE
        if x < self.x_min: code |= self.LEFT
        elif x > self.x_max: code |= self.RIGHT
        if y < self.y_min: code |= self.BOTTOM
        elif y > self.y_max: code |= self.TOP
        return code

    def clip(self, x1, y1, x2, y2):
        code1 = self.compute_code(x1, y1)
        code2 = self.compute_code(x2, y2)
        accept = False

        while True:
            # Jika kedua titik di dalam (OR = 0) [cite: 257]
            if code1 == 0 and code2 == 0:
                accept = True
                break
            # Jika kedua titik di luar wilayah yang sama (AND != 0) [cite: 280]
            elif (code1 & code2) != 0:
                break
            else:
                # Pilih titik di luar untuk diklip [cite: 297]
                code_out = code1 if code1 != 0 else code2
                
                # Menghitung titik potong menggunakan persamaan garis [cite: 372, 382]
                if code_out & self.TOP:
                    x = x1 + (x2 - x1) * (self.y_max - y1) / (y2 - y1)
                    y = self.y_max
                elif code_out & self.BOTTOM:
                    x = x1 + (x2 - x1) * (self.y_min - y1) / (y2 - y1)
                    y = self.y_min
                elif code_out & self.RIGHT:
                    y = y1 + (y2 - y1) * (self.x_max - x1) / (x2 - x1)
                    x = self.x_max
                elif code_out & self.LEFT:
                    y = y1 + (y2 - y1) * (self.x_min - x1) / (x2 - x1)
                    x = self.x_min

                if code_out == code1:
                    x1, y1 = x, y
                    code1 = self.compute_code(x1, y1)
                else:
                    x2, y2 = x, y
                    code2 = self.compute_code(x2, y2)

        return (x1, y1, x2, y2) if accept else None