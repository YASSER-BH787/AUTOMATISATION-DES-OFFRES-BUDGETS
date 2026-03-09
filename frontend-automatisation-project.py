"""
Budget Offer Automation Interface
Baker Hughes Thermodyn - DTI Department
Professional interface for automatic budget offer generation
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os


class BudgetOfferInterface:
    """Main interface for budget offer generation"""
    
    # Baker Hughes Color Scheme
    BH_GREEN = "#00A499"  # Baker Hughes turquoise green
    BH_DARK = "#1E1E1E"   # Dark gray/black
    BH_LIGHT = "#F5F5F5"  # Light background
    BH_WHITE = "#FFFFFF"  # White
    BH_ACCENT = "#00D4C5" # Light turquoise accent
    
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Offer Generator - Baker Hughes Thermodyn")
        self.root.geometry("1600x900")  # Wider window
        self.root.configure(bg=self.BH_LIGHT)
        
        # Variables to store data
        self.setup_variables()
        
        # Create interface with scrollbar
        self.create_scrollable_interface()
        
        # Build interface sections
        self.build_interface()
        
    def setup_variables(self):
        """Initialize all tkinter variables"""
        # Section 1: Project type (DTI, BUDGET, or FIRM)
        self.offer_category = tk.StringVar(value="DTI")
        
        # Section 2: Project information
        self.opp_id = tk.StringVar()
        self.revision_number = tk.StringVar()
        self.general_comment = tk.StringVar()
        
        # Section 3: Application and gas
        self.application_type = tk.StringVar()
        self.gas_type = tk.StringVar(value="Natural Gas")
        self.custom_gas = tk.StringVar()
        
        # Section 4: Client information
        self.client_name = tk.StringVar()
        self.client_location = tk.StringVar()
        self.project_date = tk.StringVar(value=datetime.now().strftime("%m/%d/%Y"))
        
        # Section 5: Contacts
        self.ae_name = tk.StringVar()
        self.ae_phone = tk.StringVar()
        self.ae_email = tk.StringVar()
        self.sales_name = tk.StringVar()
        self.sales_phone = tk.StringVar()
        self.sales_email = tk.StringVar()
        
        # Section 6: NDA
        self.nda_signed = tk.BooleanVar(value=False)
        
        # Section 7: Documents
        self.doc_gad = tk.BooleanVar(value=False)
        self.doc_pid = tk.BooleanVar(value=False)
        self.doc_cooling = tk.BooleanVar(value=False)
        self.doc_scope = tk.BooleanVar(value=False)
        self.doc_extra1 = tk.BooleanVar(value=False)
        self.doc_extra2 = tk.BooleanVar(value=False)
        self.doc_extra3 = tk.BooleanVar(value=False)
        self.doc_extra4 = tk.BooleanVar(value=False)
        self.doc_extra5 = tk.BooleanVar(value=False)
        
        # Section 8: Configuration
        self.num_impellers = tk.StringVar(value="7")
        self.casing_size = tk.StringVar(value="450")
        self.num_phases = tk.StringVar(value="2")
        self.config_code = tk.StringVar()
        
        # Section 9: Motor and mechanical configuration
        self.motor_type = tk.StringVar(value="MGV1")
        self.back_to_back = tk.StringVar(value="Back to Back")
        
        # Section 10: Cooling
        self.motor_cooling_tcv = tk.BooleanVar(value=True)
        self.motor_cooling_fan = tk.BooleanVar(value=True)
        self.vfd_cooling = tk.StringVar(value="Cooler")
        
        # Section 11: Transformer
        self.transfo_type = tk.StringVar(value="Oil ONAN")
        
        # Section 12: Scope
        self.antisurge_valve = tk.BooleanVar(value=False)
        self.filter_type = tk.StringVar(value="Simplex")
        self.ehouse = tk.BooleanVar(value=False)
        self.mcc = tk.BooleanVar(value=False)
        self.compressor_enclosure = tk.BooleanVar(value=False)
        
        # Section 13: UCP and Safety
        self.ucp_type = tk.StringVar(value="Allen Bradley")
        self.plc_safety = tk.BooleanVar(value=True)
        
        # Section 14: Power and cooling system
        self.power = tk.StringVar()
        self.cooling_system = tk.StringVar(value="Baseline")
        
        # Section 15: Thrust bearing
        self.thrust_bearing = tk.BooleanVar(value=False)
        
        # Section 16: Clarifications
        self.general_clarification = tk.StringVar()
        
        # Section 17: Price and commercial conditions
        self.cost_base = tk.StringVar()
        self.margin_percent = tk.StringVar(value="20")
        self.final_price = tk.StringVar()
        self.shipping = tk.StringVar()
        self.lead_time = tk.StringVar()
        
    def create_scrollable_interface(self):
        """Create canvas with scrollbar for interface"""
        # Main frame with scrollbar
        main_frame = tk.Frame(self.root, bg=self.BH_LIGHT)
        main_frame.pack(fill=tk.BOTH, expand=1)
        
        # Canvas
        canvas = tk.Canvas(main_frame, bg=self.BH_LIGHT, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Inner frame for content
        self.content_frame = tk.Frame(canvas, bg=self.BH_LIGHT)
        canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        
        # Bind mousewheel
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
    def build_interface(self):
        """Build all interface sections"""
        # Header with logo
        self.create_header()
        
        # Section 1: Project type
        self.create_project_type_section()
        
        # Section 2: Project information
        self.create_project_info_section()
        
        # Section 3: Application and gas
        self.create_application_section()
        
        # Section 4: Client information
        self.create_client_section()
        
        # Section 5: Contacts
        self.create_contacts_section()
        
        # Section 6: NDA
        self.create_nda_section()
        
        # Section 7: Documents
        self.create_documents_section()
        
        # Section 8: Configuration
        self.create_configuration_section()
        
        # Section 9: Equipment
        self.create_equipment_section()
        
        # Section 10: Cooling
        self.create_cooling_section()
        
        # Section 11: Detailed scope
        self.create_scope_section()
        
        # Section 12: Clarifications
        self.create_clarification_section()
        
        # Section 14: Price and commercial conditions
        self.create_commercial_section()
        
        # Action buttons
        self.create_action_buttons()
        
    def create_header(self):
        """Create header with Baker Hughes logo"""
        header_frame = tk.Frame(self.content_frame, bg=self.BH_DARK, height=120)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Try to load and display logo
        try:
            logo_path = os.path.join(os.path.dirname(__file__), 'baker_hughes_logo.png')
            if os.path.exists(logo_path):
                logo_img = Image.open(logo_path)
                # Resize logo to fit header
                logo_img = logo_img.resize((400, 67), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                
                logo_label = tk.Label(header_frame, image=self.logo_photo, bg=self.BH_DARK)
                logo_label.pack(side=tk.LEFT, padx=30, pady=25)
        except Exception as e:
            print(f"Could not load logo: {e}")
        
        # Title
        title_frame = tk.Frame(header_frame, bg=self.BH_DARK)
        title_frame.pack(side=tk.LEFT, padx=30, pady=20, fill=tk.BOTH, expand=True)
        
        title = tk.Label(title_frame, text="BUDGET OFFER GENERATOR", 
                        font=("Arial", 24, "bold"), bg=self.BH_DARK, fg=self.BH_GREEN)
        title.pack(anchor=tk.W)
        
        subtitle = tk.Label(title_frame, text="Thermodyn - DTI Department", 
                           font=("Arial", 12), bg=self.BH_DARK, fg=self.BH_WHITE)
        subtitle.pack(anchor=tk.W)
        
    def create_section_frame(self, title):
        """Create frame for section with title"""
        frame = tk.LabelFrame(self.content_frame, text=title, font=("Arial", 11, "bold"),
                            padx=20, pady=15, relief=tk.GROOVE, borderwidth=2,
                            bg=self.BH_WHITE, fg=self.BH_DARK, 
                            highlightbackground=self.BH_GREEN, highlightthickness=1)
        frame.pack(fill=tk.X, padx=15, pady=8)
        return frame
    
    def create_project_type_section(self):
        """Section 1: Project type"""
        frame = self.create_section_frame("1. OFFER CATEGORY")
        
        # Single row with three options
        category_frame = tk.Frame(frame, bg=self.BH_WHITE)
        category_frame.pack(anchor=tk.W, pady=10)
        
        tk.Label(category_frame, text="Select Offer Category:", font=("Arial", 10, "bold"), 
                bg=self.BH_WHITE).pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(category_frame, text="DTI", variable=self.offer_category, 
                      value="DTI", font=("Arial", 10), bg=self.BH_WHITE,
                      selectcolor=self.BH_GREEN).pack(side=tk.LEFT, padx=20)
        
        tk.Radiobutton(category_frame, text="BUDGET", variable=self.offer_category, 
                      value="BUDGET", font=("Arial", 10), bg=self.BH_WHITE,
                      selectcolor=self.BH_GREEN).pack(side=tk.LEFT, padx=20)
        
        tk.Radiobutton(category_frame, text="FIRM", variable=self.offer_category, 
                      value="FIRM", font=("Arial", 10), bg=self.BH_WHITE,
                      selectcolor=self.BH_GREEN).pack(side=tk.LEFT, padx=20)
    
    def create_project_info_section(self):
        """Section 2: Project information"""
        frame = self.create_section_frame("2. PROJECT INFORMATION")
        
        # Create a more spacious grid layout
        info_frame = tk.Frame(frame, bg=self.BH_WHITE)
        info_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Row 1 - OPP ID and Revision
        tk.Label(info_frame, text="OPP ID:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(info_frame, textvariable=self.opp_id, width=35, font=("Arial", 10)).grid(row=0, column=1, pady=8, padx=10, sticky=tk.W)
        
        tk.Label(info_frame, text="Revision Number:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=2, sticky=tk.W, pady=8, padx=30)
        tk.Entry(info_frame, textvariable=self.revision_number, width=35, font=("Arial", 10)).grid(row=0, column=3, pady=8, padx=10, sticky=tk.W)
        
        # Row 2 - General Comment (full width)
        tk.Label(info_frame, text="General Comment:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=1, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(info_frame, textvariable=self.general_comment, width=120, font=("Arial", 10)).grid(row=1, column=1, columnspan=3, pady=8, padx=10, sticky=tk.EW)
        
        # Configure column weights for expansion
        info_frame.columnconfigure(1, weight=1)
        info_frame.columnconfigure(3, weight=1)
    
    def create_application_section(self):
        """Section 3: Application type and gas"""
        frame = self.create_section_frame("3. APPLICATION & GAS")
        
        app_frame = tk.Frame(frame, bg=self.BH_WHITE)
        app_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Application type - Left side
        tk.Label(app_frame, text="Application Type:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=8, padx=10)
        
        applications = [
            "Air Service", "Ammonia Synthesis", "Ethylene Synthesis", "FCC",
            "Fuel Gas", "LNG", "LPG", "Lubricant Production", "Methanol Synthesis",
            "Olefin", "Other", "Oxygen Service", "Pipeline", "Reforming",
            "Reinjection", "Urea Synthesis"
        ]
        
        app_combo = ttk.Combobox(app_frame, textvariable=self.application_type, values=applications, 
                                width=35, font=("Arial", 10), state="readonly")
        app_combo.grid(row=0, column=1, padx=10, pady=8, sticky=tk.W)
        app_combo.current(0)
        
        # Gas type - Right side
        tk.Label(app_frame, text="Gas Type:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=2, sticky=tk.W, pady=8, padx=30)
        
        gas_frame = tk.Frame(app_frame, bg=self.BH_WHITE)
        gas_frame.grid(row=0, column=3, sticky=tk.W, padx=10, pady=8)
        
        tk.Radiobutton(gas_frame, text="Natural Gas", variable=self.gas_type, 
                      value="Natural Gas", font=("Arial", 10), bg=self.BH_WHITE,
                      selectcolor=self.BH_GREEN).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(gas_frame, text="Other:", variable=self.gas_type, 
                      value="Custom", font=("Arial", 10), bg=self.BH_WHITE,
                      selectcolor=self.BH_GREEN).pack(side=tk.LEFT, padx=5)
        tk.Entry(gas_frame, textvariable=self.custom_gas, width=25, font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        # Configure column weights
        app_frame.columnconfigure(1, weight=1)
        app_frame.columnconfigure(3, weight=1)
    
    def create_client_section(self):
        """Section 4: Client information"""
        frame = self.create_section_frame("4. CLIENT INFORMATION")
        
        client_frame = tk.Frame(frame, bg=self.BH_WHITE)
        client_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Row 1 - Client Name and Location
        tk.Label(client_frame, text="Client Name:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(client_frame, textvariable=self.client_name, width=45, font=("Arial", 10)).grid(row=0, column=1, padx=10, pady=8, sticky=tk.W)
        
        tk.Label(client_frame, text="Location:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=2, sticky=tk.W, pady=8, padx=30)
        tk.Entry(client_frame, textvariable=self.client_location, width=45, font=("Arial", 10)).grid(row=0, column=3, padx=10, pady=8, sticky=tk.W)
        
        # Row 2 - Date
        tk.Label(client_frame, text="Date:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=1, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(client_frame, textvariable=self.project_date, width=25, font=("Arial", 10)).grid(row=1, column=1, padx=10, pady=8, sticky=tk.W)
        
        # Configure column weights
        client_frame.columnconfigure(1, weight=1)
        client_frame.columnconfigure(3, weight=1)
    
    def create_contacts_section(self):
        """Section 5: Contacts"""
        frame = self.create_section_frame("5. CONTACTS")
        
        contacts_frame = tk.Frame(frame, bg=self.BH_WHITE)
        contacts_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Left column - Application Engineer
        left_col = tk.Frame(contacts_frame, bg=self.BH_WHITE)
        left_col.grid(row=0, column=0, sticky=tk.NW, padx=10, pady=5)
        
        tk.Label(left_col, text="Application Engineer (AE)", font=("Arial", 11, "bold"), 
                bg=self.BH_WHITE, fg=self.BH_GREEN).grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=10)
        
        tk.Label(left_col, text="Name:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Entry(left_col, textvariable=self.ae_name, width=40, font=("Arial", 10)).grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        
        tk.Label(left_col, text="Phone:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=2, column=0, sticky=tk.W, pady=5)
        tk.Entry(left_col, textvariable=self.ae_phone, width=40, font=("Arial", 10)).grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        
        tk.Label(left_col, text="Email:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=3, column=0, sticky=tk.W, pady=5)
        tk.Entry(left_col, textvariable=self.ae_email, width=40, font=("Arial", 10)).grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Vertical separator
        separator = tk.Frame(contacts_frame, width=2, bg=self.BH_GREEN)
        separator.grid(row=0, column=1, sticky=tk.NS, padx=30, pady=10)
        
        # Right column - Sales
        right_col = tk.Frame(contacts_frame, bg=self.BH_WHITE)
        right_col.grid(row=0, column=2, sticky=tk.NW, padx=10, pady=5)
        
        tk.Label(right_col, text="Sales", font=("Arial", 11, "bold"), 
                bg=self.BH_WHITE, fg=self.BH_GREEN).grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=10)
        
        tk.Label(right_col, text="Name:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Entry(right_col, textvariable=self.sales_name, width=40, font=("Arial", 10)).grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        
        tk.Label(right_col, text="Phone:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=2, column=0, sticky=tk.W, pady=5)
        tk.Entry(right_col, textvariable=self.sales_phone, width=40, font=("Arial", 10)).grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        
        tk.Label(right_col, text="Email:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=3, column=0, sticky=tk.W, pady=5)
        tk.Entry(right_col, textvariable=self.sales_email, width=40, font=("Arial", 10)).grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Configure column weights
        contacts_frame.columnconfigure(0, weight=1)
        contacts_frame.columnconfigure(2, weight=1)
    
    def create_nda_section(self):
        """Section 6: NDA"""
        frame = self.create_section_frame("6. NDA (NON-DISCLOSURE AGREEMENT)")
        
        nda_frame = tk.Frame(frame, bg=self.BH_WHITE)
        nda_frame.pack(anchor=tk.W, pady=5)
        
        tk.Label(nda_frame, text="Has the client signed an NDA?", font=("Arial", 10), 
                bg=self.BH_WHITE).pack(side=tk.LEFT, padx=10)
        
        nda_button = tk.Checkbutton(nda_frame, text="NDA Signed", variable=self.nda_signed,
                                   font=("Arial", 10), command=self.update_nda_status,
                                   bg=self.BH_WHITE, selectcolor=self.BH_GREEN)
        nda_button.pack(side=tk.LEFT, padx=20)
        
        self.nda_status_label = tk.Label(nda_frame, text="✗ Not Signed", 
                                        font=("Arial", 10, "bold"), fg="red", bg=self.BH_WHITE)
        self.nda_status_label.pack(side=tk.LEFT, padx=10)
    
    def update_nda_status(self):
        """Update NDA status display"""
        if self.nda_signed.get():
            self.nda_status_label.config(text="✓ Signed", fg=self.BH_GREEN)
        else:
            self.nda_status_label.config(text="✗ Not Signed", fg="red")
    
    def create_documents_section(self):
        """Section 7: Documents"""
        frame = self.create_section_frame("7. DOCUMENTS TO PROVIDE")
        
        doc_frame = tk.Frame(frame, bg=self.BH_WHITE)
        doc_frame.pack(anchor=tk.W, pady=5)
        
        # Column 1
        col1 = tk.Frame(doc_frame, bg=self.BH_WHITE)
        col1.pack(side=tk.LEFT, padx=20)
        
        tk.Checkbutton(col1, text="GAD (General Arrangement Drawing)", variable=self.doc_gad,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col1, text="P&ID (Piping & Instrumentation Diagram)", variable=self.doc_pid,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col1, text="Cooling Concept", variable=self.doc_cooling,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col1, text="Scope of Supply", variable=self.doc_scope,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        
        # Column 2 - Future documents
        col2 = tk.Frame(doc_frame, bg=self.BH_WHITE)
        col2.pack(side=tk.LEFT, padx=20)
        
        tk.Checkbutton(col2, text="Extra Document 1 (TBD)", variable=self.doc_extra1,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col2, text="Extra Document 2 (TBD)", variable=self.doc_extra2,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col2, text="Extra Document 3 (TBD)", variable=self.doc_extra3,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col2, text="Extra Document 4 (TBD)", variable=self.doc_extra4,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
        tk.Checkbutton(col2, text="Extra Document 5 (TBD)", variable=self.doc_extra5,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).pack(anchor=tk.W, pady=3)
    
    def create_configuration_section(self):
        """Section 8: Compressor configuration"""
        frame = self.create_section_frame("8. COMPRESSOR CONFIGURATION")
        
        config_frame = tk.Frame(frame, bg=self.BH_WHITE)
        config_frame.pack(fill=tk.X, pady=5)
        
        # Line 1 - Configuration inputs in a more spacious layout
        tk.Label(config_frame, text="Number of Impellers:", font=("Arial", 10), 
                bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)
        tk.Entry(config_frame, textvariable=self.num_impellers, width=15, font=("Arial", 10)).grid(row=0, column=1, pady=5, padx=10, sticky=tk.W)
        
        tk.Label(config_frame, text="Casing Size:", font=("Arial", 10), 
                bg=self.BH_WHITE).grid(row=0, column=2, sticky=tk.W, pady=5, padx=10)
        tk.Entry(config_frame, textvariable=self.casing_size, width=15, font=("Arial", 10)).grid(row=0, column=3, pady=5, padx=10, sticky=tk.W)
        
        tk.Label(config_frame, text="Number of Phases:", font=("Arial", 10), 
                bg=self.BH_WHITE).grid(row=0, column=4, sticky=tk.W, pady=5, padx=10)
        
        phase_combo = ttk.Combobox(config_frame, textvariable=self.num_phases, values=["1", "2"], 
                                  width=8, font=("Arial", 10), state="readonly")
        phase_combo.grid(row=0, column=5, pady=5, padx=10, sticky=tk.W)
        
        # Bind phase change to auto-select Back to Back
        phase_combo.bind("<<ComboboxSelected>>", self.on_phase_change)
        
        # Line 2 - Generate button and code display
        tk.Button(config_frame, text="Generate Configuration Code", command=self.generate_config_code,
                 bg=self.BH_GREEN, fg=self.BH_WHITE, font=("Arial", 10, "bold"),
                 cursor="hand2", width=25).grid(row=1, column=0, columnspan=2, pady=15, padx=10, sticky=tk.W)
        
        # Display code
        tk.Label(config_frame, text="Configuration Code:", font=("Arial", 10, "bold"), 
                bg=self.BH_WHITE).grid(row=1, column=2, sticky=tk.E, pady=5, padx=10)
        config_entry = tk.Entry(config_frame, textvariable=self.config_code, width=25, 
                               font=("Arial", 12, "bold"), state="readonly", 
                               readonlybackground=self.BH_ACCENT, fg=self.BH_DARK)
        config_entry.grid(row=1, column=3, columnspan=3, pady=5, padx=10, sticky=tk.W)
    
    def on_phase_change(self, event=None):
        """Automatically select Back to Back when phases = 2"""
        if self.num_phases.get() == "2":
            self.back_to_back.set("Back to Back")
        else:
            self.back_to_back.set("Simple")
    
    def generate_config_code(self):
        """Automatically generate configuration code"""
        try:
            num_impellers = self.num_impellers.get()
            casing_size = self.casing_size.get()
            num_phases = self.num_phases.get()
            
            if not num_impellers or not casing_size or not num_phases:
                messagebox.showwarning("Warning", "Please fill all configuration fields")
                return
            
            # Generate code
            if num_phases == "2":
                code = f"{num_phases}ICL{casing_size}{num_impellers}"
            else:
                code = f"ICL{casing_size}{num_impellers}"
            
            self.config_code.set(code)
            messagebox.showinfo("Success", f"Configuration code generated: {code}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error during generation: {str(e)}")
    
    def create_equipment_section(self):
        """Section 9: Equipment"""
        frame = self.create_section_frame("9. EQUIPMENT")
        
        equip_frame = tk.Frame(frame, bg=self.BH_WHITE)
        equip_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Row 1 - Motor Type and Configuration
        tk.Label(equip_frame, text="Motor Type:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=8, padx=10)
        motor_combo = ttk.Combobox(equip_frame, textvariable=self.motor_type, 
                                  values=["MGV0", "MGV1", "MGV2", "MGV3"],
                                  width=18, font=("Arial", 10), state="readonly")
        motor_combo.grid(row=0, column=1, padx=10, pady=8, sticky=tk.W)
        motor_combo.current(1)
        
        tk.Label(equip_frame, text="Configuration:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=2, sticky=tk.W, pady=8, padx=30)
        config_combo = ttk.Combobox(equip_frame, textvariable=self.back_to_back,
                                   values=["Back to Back", "Simple"],
                                   width=18, font=("Arial", 10), state="readonly")
        config_combo.grid(row=0, column=3, padx=10, pady=8, sticky=tk.W)
        config_combo.current(0)
        
        # Row 2 - UCP and Safety PLC
        tk.Label(equip_frame, text="UCP (Unit Control Panel):", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=1, column=0, sticky=tk.W, pady=8, padx=10)
        ucp_combo = ttk.Combobox(equip_frame, textvariable=self.ucp_type,
                                values=["Allen Bradley", "Siemens"],
                                width=18, font=("Arial", 10), state="readonly")
        ucp_combo.grid(row=1, column=1, padx=10, pady=8, sticky=tk.W)
        ucp_combo.current(0)
        
        tk.Label(equip_frame, text="Safety & Control PLC:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=1, column=2, sticky=tk.W, pady=8, padx=30)
        tk.Checkbutton(equip_frame, text="Included", variable=self.plc_safety,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=1, column=3, padx=10, pady=8, sticky=tk.W)
        
        # Row 3 - Thrust Bearing
        tk.Label(equip_frame, text="Thrust Bearing:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=2, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Checkbutton(equip_frame, text="Included", variable=self.thrust_bearing,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=2, column=1, padx=10, pady=8, sticky=tk.W)
        
        # Configure column weights
        equip_frame.columnconfigure(1, weight=1)
        equip_frame.columnconfigure(3, weight=1)
    
    def create_cooling_section(self):
        """Section 10: Cooling systems"""
        frame = self.create_section_frame("10. COOLING SYSTEMS")
        
        cooling_frame = tk.Frame(frame, bg=self.BH_WHITE)
        cooling_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Motor cooling header
        tk.Label(cooling_frame, text="Motor Cooling:", font=("Arial", 11, "bold"), 
                bg=self.BH_WHITE, fg=self.BH_GREEN).grid(row=0, column=0, columnspan=4, sticky=tk.W, pady=10, padx=10)
        
        # Row 1 - Motor cooling options
        tk.Checkbutton(cooling_frame, text="TCV Standard", variable=self.motor_cooling_tcv,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=1, column=0, sticky=tk.W, pady=5, padx=20)
        tk.Checkbutton(cooling_frame, text="Fan Standard", variable=self.motor_cooling_fan,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=1, column=1, sticky=tk.W, pady=5, padx=20)
        
        tk.Label(cooling_frame, text="VFD Cooling:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=1, column=2, sticky=tk.W, pady=5, padx=30)
        vfd_combo = ttk.Combobox(cooling_frame, textvariable=self.vfd_cooling,
                                values=["Cooler", "Chiller"],
                                width=15, font=("Arial", 10), state="readonly")
        vfd_combo.grid(row=1, column=3, pady=5, padx=10, sticky=tk.W)
        vfd_combo.current(0)
        
        # Row 2 - Transformer and Cooling System
        tk.Label(cooling_frame, text="Transformer:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=2, column=0, sticky=tk.W, pady=8, padx=20)
        tk.Entry(cooling_frame, textvariable=self.transfo_type, width=18, font=("Arial", 10),
                state="readonly").grid(row=2, column=1, pady=8, padx=10, sticky=tk.W)
        
        tk.Label(cooling_frame, text="Required Power (kW):", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=2, column=2, sticky=tk.W, pady=8, padx=30)
        tk.Entry(cooling_frame, textvariable=self.power, width=18, font=("Arial", 10)).grid(row=2, column=3, padx=10, pady=8, sticky=tk.W)
        
        # Separator
        separator = tk.Frame(cooling_frame, height=2, bg=self.BH_GREEN)
        separator.grid(row=3, column=0, columnspan=4, sticky="ew", pady=10, padx=10)
        
        # Cooling system concept
        tk.Label(cooling_frame, text="Cooling System Concept:", font=("Arial", 11, "bold"), 
                bg=self.BH_WHITE, fg=self.BH_GREEN).grid(row=4, column=0, columnspan=4, sticky=tk.W, pady=10, padx=10)
        
        cooling_systems = [
            "Baseline",
            "Concept with Cooler",
            "Concept without Cooler",
            "Compact Piping",
            "Closed Loop",
            "External Fuel Gas without Cooler",
            "External Fuel Gas with Process Cooler"
        ]
        
        tk.Label(cooling_frame, text="System:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=5, column=0, sticky=tk.W, pady=8, padx=20)
        cooling_combo = ttk.Combobox(cooling_frame, textvariable=self.cooling_system,
                                    values=cooling_systems,
                                    width=40, font=("Arial", 10), state="readonly")
        cooling_combo.grid(row=5, column=1, columnspan=3, pady=8, padx=10, sticky=tk.W)
        cooling_combo.current(0)
        
        # Configure column weights
        cooling_frame.columnconfigure(1, weight=1)
        cooling_frame.columnconfigure(3, weight=1)
    
    def create_scope_section(self):
        """Section 11: Detailed scope"""
        frame = self.create_section_frame("11. DETAILED SCOPE")
        
        # Antisurge valve
        tk.Checkbutton(frame, text="Antisurge Valve", variable=self.antisurge_valve,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=0, column=0, sticky=tk.W, pady=5, padx=20)
        
        # Filter type
        tk.Label(frame, text="Filter Type:", font=("Arial", 10), bg=self.BH_WHITE).grid(row=1, column=0, sticky=tk.W, pady=5, padx=20)
        filter_combo = ttk.Combobox(frame, textvariable=self.filter_type,
                                   values=["Simplex", "Duplex"],
                                   width=15, font=("Arial", 10), state="readonly")
        filter_combo.grid(row=1, column=1, pady=5, padx=10, sticky=tk.W)
        filter_combo.current(0)
        
        # Extra scope
        tk.Label(frame, text="Extra Scope:", font=("Arial", 10, "bold"), 
                bg=self.BH_WHITE, fg=self.BH_GREEN).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=10, padx=20)
        
        tk.Checkbutton(frame, text="E-HOUSE", variable=self.ehouse,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=3, column=0, sticky=tk.W, pady=3, padx=40)
        tk.Checkbutton(frame, text="MCC (Motor Control Center)", variable=self.mcc,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=4, column=0, sticky=tk.W, pady=3, padx=40)
        tk.Checkbutton(frame, text="Compressor Enclosure", variable=self.compressor_enclosure,
                      font=("Arial", 10), bg=self.BH_WHITE, selectcolor=self.BH_GREEN).grid(row=5, column=0, sticky=tk.W, pady=3, padx=40)
    
    def create_power_section(self):
        """Section 12: Power"""
        frame = self.create_section_frame("12. POWER")
        
        tk.Label(frame, text="Required Power (kW):", font=("Arial", 10), bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=5)
        tk.Entry(frame, textvariable=self.power, width=20, font=("Arial", 10)).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
    
    def create_clarification_section(self):
        """Section 12: Clarifications"""
        frame = self.create_section_frame("12. GENERAL CLARIFICATIONS")
        
        tk.Label(frame, text="Clarifications and Notes:", font=("Arial", 10), bg=self.BH_WHITE).pack(anchor=tk.W, pady=5)
        
        text_frame = tk.Frame(frame, bg=self.BH_WHITE)
        text_frame.pack(fill=tk.X, pady=5)
        
        clarif_text = tk.Text(text_frame, height=5, width=100, font=("Arial", 10), wrap=tk.WORD)
        clarif_text.pack(side=tk.LEFT, padx=5)
        
        scrollbar = tk.Scrollbar(text_frame, command=clarif_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        clarif_text.config(yscrollcommand=scrollbar.set)
        
        # Bind with variable
        def update_clarification(*args):
            self.general_clarification.set(clarif_text.get("1.0", tk.END).strip())
        
        clarif_text.bind("<KeyRelease>", update_clarification)
    
    def create_commercial_section(self):
        """Section 13: Price and commercial conditions"""
        frame = self.create_section_frame("13. PRICE & COMMERCIAL CONDITIONS")
        
        commercial_frame = tk.Frame(frame, bg=self.BH_WHITE)
        commercial_frame.pack(fill=tk.X, pady=5, padx=10)
        
        # Row 1 - Base cost and Margin
        tk.Label(commercial_frame, text="Base Cost (€):", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(commercial_frame, textvariable=self.cost_base, width=25, font=("Arial", 10)).grid(row=0, column=1, padx=10, pady=8, sticky=tk.W)
        
        tk.Label(commercial_frame, text="Margin (%):", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=0, column=2, sticky=tk.W, pady=8, padx=30)
        margin_entry = tk.Entry(commercial_frame, textvariable=self.margin_percent, width=15, font=("Arial", 10))
        margin_entry.grid(row=0, column=3, padx=10, pady=8, sticky=tk.W)
        
        # Row 2 - Calculate button and Final Price
        tk.Button(commercial_frame, text="Calculate Final Price", command=self.calculate_final_price,
                 bg=self.BH_GREEN, fg=self.BH_WHITE, font=("Arial", 10, "bold"),
                 cursor="hand2", width=20).grid(row=1, column=0, columnspan=1, pady=10, padx=10, sticky=tk.W)
        
        tk.Label(commercial_frame, text="Final Price (€):", font=("Arial", 11, "bold"), 
                bg=self.BH_WHITE, fg=self.BH_GREEN).grid(row=1, column=1, sticky=tk.E, pady=8, padx=10)
        final_entry = tk.Entry(commercial_frame, textvariable=self.final_price, width=25, 
                              font=("Arial", 12, "bold"), bg="#FFFFCC", state="readonly",
                              readonlybackground="#FFFFCC")
        final_entry.grid(row=1, column=2, columnspan=2, padx=10, pady=8, sticky=tk.W)
        
        # Separator
        separator = tk.Frame(commercial_frame, height=2, bg=self.BH_GREEN)
        separator.grid(row=2, column=0, columnspan=4, sticky="ew", pady=10, padx=10)
        
        # Row 3 - Shipping and Lead Time
        tk.Label(commercial_frame, text="Shipping:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=3, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(commercial_frame, textvariable=self.shipping, width=70, font=("Arial", 10)).grid(row=3, column=1, columnspan=3, padx=10, pady=8, sticky=tk.EW)
        
        tk.Label(commercial_frame, text="Lead Time:", font=("Arial", 10, "bold"), bg=self.BH_WHITE).grid(row=4, column=0, sticky=tk.W, pady=8, padx=10)
        tk.Entry(commercial_frame, textvariable=self.lead_time, width=70, font=("Arial", 10)).grid(row=4, column=1, columnspan=3, padx=10, pady=8, sticky=tk.EW)
        
        # Configure column weights
        commercial_frame.columnconfigure(1, weight=1)
        commercial_frame.columnconfigure(3, weight=1)
    
    def calculate_final_price(self):
        """Calculate final price with margin"""
        try:
            cost = float(self.cost_base.get() or 0)
            margin = float(self.margin_percent.get() or 0)
            
            if cost <= 0:
                messagebox.showwarning("Warning", "Please enter a valid base cost")
                return
            
            final = cost * (1 + margin / 100)
            self.final_price.set(f"{final:,.2f}")
            
            messagebox.showinfo("Calculation Complete", 
                              f"Base cost: {cost:,.2f} €\n"
                              f"Margin: {margin}%\n"
                              f"Final price: {final:,.2f} €")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def create_action_buttons(self):
        """Create main action buttons"""
        button_frame = tk.Frame(self.content_frame, bg=self.BH_DARK, pady=25)
        button_frame.pack(fill=tk.X, padx=10, pady=20)
        
        # Generate PDF button (to be implemented later)
        tk.Button(button_frame, text="GENERATE PDF", command=self.generate_pdf,
                 bg=self.BH_GREEN, fg=self.BH_WHITE, font=("Arial", 14, "bold"),
                 width=20, height=2, cursor="hand2", relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=20)
        
        # Reset button
        tk.Button(button_frame, text="RESET", command=self.reset_form,
                 bg="#CC0000", fg=self.BH_WHITE, font=("Arial", 14, "bold"),
                 width=20, height=2, cursor="hand2", relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=20)
        
        # Save button
        tk.Button(button_frame, text="SAVE", command=self.save_data,
                 bg=self.BH_DARK, fg=self.BH_WHITE, font=("Arial", 14, "bold"),
                 width=20, height=2, cursor="hand2", relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=20)
    
    def generate_pdf(self):
        """Generate PDF budget offer (to be implemented)"""
        messagebox.showinfo("Information", 
                          "PDF generation will be implemented in the next phase.\n"
                          "All data is ready for export.")
    
    def save_data(self):
        """Save data to file"""
        messagebox.showinfo("Save", 
                          "Save function to be implemented.\n"
                          "Data will be exported to JSON or Excel.")
    
    def reset_form(self):
        """Reset all fields"""
        if messagebox.askyesno("Confirmation", "Do you really want to reset all fields?"):
            self.setup_variables()
            messagebox.showinfo("Reset", "All fields have been reset")
            # Restart interface
            self.root.destroy()
            main()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = BudgetOfferInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()                        