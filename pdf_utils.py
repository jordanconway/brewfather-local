from fpdf import FPDF, XPos, YPos

# RGB values for the provided color palette
COLOR_DEEP_CHARCOAL = (43, 46, 47)
COLOR_AMBER_GOLD = (232, 176, 66)
COLOR_HOP_GREEN = (118, 141, 93)
COLOR_CREAMY_FOAM = (248, 244, 225)
COLOR_BARLEY_TAN = (199, 161, 102)
COLOR_STEEL_SILVER = (169, 173, 176)

class PDF(FPDF):
    def header(self):
        # Logo
        # Assuming 'brewstepdaddy.png' is in the same directory or accessible path
        self.image('brewstepdaddy.png', 10, 8, 33)
        # Helvetica bold 15
        self.set_font('Helvetica', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        self.cell(30, 10, self.title, 0, 0, 'C')
        # Line break - increased for more space after logo
        self.ln(35) 

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(*COLOR_AMBER_GOLD) # Amber Gold
        self.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal for text on Amber Gold background
        self.cell(0, 6, title, 0, 1, "L", True)
        self.ln(4)
        self.set_text_color(0, 0, 0) # Reset text color to black for body

    def chapter_body(self, body):
        self.set_font("Times", "", 12)
        self.multi_cell(0, 5, body)
        self.ln()

    def ingredient_table(self, header, data, widths):
        self.set_font("Helvetica", "B", 10)
        self.set_fill_color(*COLOR_BARLEY_TAN) # Barley Tan for table headers
        self.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal for text on Barley Tan background
        # Header
        for col, width in zip(header, widths):
            self.cell(width, 7, col, 1, 0, "C", True)
        self.ln()
        # Data
        self.set_font("Times", "", 10)
        self.set_text_color(0, 0, 0) # Reset text color to black for data rows
        fill = False
        for row in data:
            self.set_fill_color(255, 255, 255) if not fill else self.set_fill_color(*COLOR_CREAMY_FOAM) # Creamy Foam for alternating rows
            for item, width in zip(row, widths):
                self.cell(width, 6, item, 1, 0, "L", fill)
            self.ln()
            fill = not fill
        self.ln(5)
