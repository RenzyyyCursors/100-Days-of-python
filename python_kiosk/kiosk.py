import csv
import datetime
import os
import re
import sys
import threading
import cv2
import customtkinter as ctk

# Optional dependency check for OCR
try:
  import pytesseract
  from PIL import Image, ImageTk

  HAS_OCR = True
except ImportError:
  HAS_OCR = False

# Robust execution path for PyInstaller / macOS bundles
if getattr(sys, "frozen", False):
  BASE_DIR = os.path.dirname(sys.executable)
else:
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE = os.path.join(BASE_DIR, "event_attendees.csv")
ADMIN_PASSWORD = "admin"

# Automatically find Tesseract path on macOS (Homebrew paths)
TERESERACT_MACOS_PATHS = [
    "/opt/homebrew/bin/tesseract",  # Apple Silicon (M1/M2/M3/M4)
    "/usr/local/bin/tesseract",  # Intel Macs
]

if HAS_OCR:
  for path in TERESERACT_MACOS_PATHS:
    if os.path.exists(path):
      pytesseract.pytesseract.tesseract_cmd = path
      break

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class IDScannerModal(ctk.CTkToplevel):
  """Robust, thread-safe webcam scanner modal for ID cards."""

  def __init__(self, parent, callback):
    super().__init__(parent)
    self.parent = parent
    self.callback = callback
    self.running = True
    self.current_frame = None

    self.title("Scan ID Card")
    self.geometry("640x540")
    self.resizable(False, False)

    sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
    self.geometry(f"640x540+{(sw//2)-320}+{(sh//2)-270}")

    self.protocol("WM_DELETE_WINDOW", self.on_close)
    self.transient(parent)
    self.grab_set()

    self.video_label = ctk.CTkLabel(self, text="Initializing Camera...")
    self.video_label.pack(pady=15)

    self.instruction_label = ctk.CTkLabel(
        self,
        text="Align ID card inside frame and click Capture",
        font=("Helvetica", 14),
    )
    self.instruction_label.pack(pady=5)

    self.capture_btn = ctk.CTkButton(
        self,
        text="📷 Capture & Extract",
        width=220,
        height=42,
        font=("Helvetica", 14, "bold"),
        command=self.capture_and_process,
    )
    self.capture_btn.pack(pady=10)

    # Open Camera on macOS
    self.cap = cv2.VideoCapture(0)
    if not self.cap.isOpened():
      self.video_label.configure(
          text="Error: Camera access denied or unavailable."
      )
      self.capture_btn.configure(state="disabled")
      return

    self.thread = threading.Thread(target=self._stream_camera, daemon=True)
    self.thread.start()
    self._update_gui_frame()

  def _stream_camera(self):
    while self.running and self.cap.isOpened():
      ret, frame = self.cap.read()
      if ret:
        self.current_frame = frame

  def _update_gui_frame(self):
    if self.running and self.current_frame is not None:
      frame_rgb = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2RGB)
      frame_resized = cv2.resize(frame_rgb, (520, 340))
      img = ImageTk.PhotoImage(image=Image.fromarray(frame_resized))
      self.video_label.imgtk = img
      self.video_label.configure(image=img, text="")

    if self.running:
      self.after(30, self._update_gui_frame)

  def capture_and_process(self):
    if self.current_frame is None or not HAS_OCR:
      self.on_close()
      return

    captured = self.current_frame.copy()
    self.on_close()

    gray = cv2.cvtColor(captured, cv2.COLOR_BGR2GRAY)
    processed = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    raw_text = pytesseract.image_to_string(processed)

    self.callback(raw_text)

  def on_close(self):
    self.running = False
    if hasattr(self, "cap") and self.cap.isOpened():
      self.cap.release()
    self.grab_release()
    self.destroy()


class AdminExitModal(ctk.CTkToplevel):

  def __init__(self, parent, password_check_callback):
    super().__init__(parent)
    self.parent = parent
    self.password_check_callback = password_check_callback

    self.title("Admin Access")
    self.geometry("360x220")
    self.resizable(False, False)

    screen_w = self.winfo_screenwidth()
    screen_h = self.winfo_screenheight()
    self.geometry(f"360x220+{(screen_w//2)-180}+{(screen_h//2)-110}")

    self.label = ctk.CTkLabel(
        self, text="Enter Admin Password", font=("Helvetica", 16, "bold")
    )
    self.label.pack(pady=(20, 10))

    self.pwd_entry = ctk.CTkEntry(
        self, show="*", width=260, height=40, font=("Helvetica", 14)
    )
    self.pwd_entry.pack(pady=10)
    self.pwd_entry.focus_set()
    self.pwd_entry.bind("<Return>", lambda event: self.verify())

    self.error_label = ctk.CTkLabel(
        self, text="", text_color="#FF5555", font=("Helvetica", 12)
    )
    self.error_label.pack(pady=(0, 5))

    self.confirm_btn = ctk.CTkButton(
        self,
        text="Unlock & Exit",
        width=260,
        height=38,
        font=("Helvetica", 14, "bold"),
        command=self.verify,
    )
    self.confirm_btn.pack(pady=5)

    self.transient(parent)
    self.grab_set()

  def verify(self):
    if self.pwd_entry.get() == ADMIN_PASSWORD:
      self.grab_release()
      self.destroy()
      self.password_check_callback(True)
    else:
      self.error_label.configure(text="Incorrect Password!")
      self.pwd_entry.delete(0, "end")


class EventKiosk(ctk.CTk):

  def __init__(self):
    super().__init__()

    # macOS Fullscreen toggle setup
    self.attributes("-fullscreen", True)
    self.attributes("-topmost", True)

    self.protocol("WM_DELETE_WINDOW", self.prevent_close)
    self.bind("<Command-q>", self.prevent_close)
    self.bind("<Escape>", self.open_admin_modal)

    self.init_csv()

    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)

    self.card = ctk.CTkFrame(self, corner_radius=16, width=460, height=580)
    self.card.grid(row=0, column=0)
    self.card.grid_propagate(False)
    self.card.grid_columnconfigure(0, weight=1)

    self.title_label = ctk.CTkLabel(
        self.card, text="Event Check-In", font=("Helvetica", 26, "bold")
    )
    self.title_label.grid(row=0, column=0, pady=(30, 5))

    self.subtitle_label = ctk.CTkLabel(
        self.card,
        text="Scan your ID card or enter details",
        font=("Helvetica", 13),
        text_color="gray70",
    )
    self.subtitle_label.grid(row=1, column=0, pady=(0, 20))

    self.scan_btn = ctk.CTkButton(
        self.card,
        text="📷 Scan ID Card",
        width=360,
        height=40,
        fg_color="#2b5b84",
        hover_color="#1e3f5d",
        font=("Helvetica", 14, "bold"),
        command=self.open_scanner,
    )
    self.scan_btn.grid(row=2, column=0, pady=(0, 15))

    self.name_entry = ctk.CTkEntry(
        self.card,
        placeholder_text="Full Name",
        width=360,
        height=45,
        font=("Helvetica", 14),
    )
    self.name_entry.grid(row=3, column=0, pady=10)

    self.reg_entry = ctk.CTkEntry(
        self.card,
        placeholder_text="Registration Number",
        width=360,
        height=45,
        font=("Helvetica", 14),
    )
    self.reg_entry.grid(row=4, column=0, pady=10)

    self.submit_btn = ctk.CTkButton(
        self.card,
        text="Check In",
        width=360,
        height=48,
        font=("Helvetica", 15, "bold"),
        corner_radius=8,
        command=self.process_checkin,
    )
    self.submit_btn.grid(row=5, column=0, pady=(20, 10))

    self.status_label = ctk.CTkLabel(
        self.card, text="", font=("Helvetica", 13)
    )
    self.status_label.grid(row=6, column=0, pady=5)

    self.exit_btn = ctk.CTkButton(
        self,
        text="Admin Exit",
        width=90,
        height=30,
        fg_color="transparent",
        hover_color="#2B2B2B",
        text_color="gray50",
        command=self.open_admin_modal,
    )
    self.exit_btn.place(relx=0.99, rely=0.98, anchor="se")

  def init_csv(self):
    if not os.path.exists(CSV_FILE):
      with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Serial No", "Full Name", "Reg No", "Timestamp (Date & Time)"]
        )

  def get_next_serial(self):
    if not os.path.exists(CSV_FILE):
      return 1
    with open(CSV_FILE, mode="r", encoding="utf-8") as f:
      return len(list(csv.reader(f)))

  def open_scanner(self):
    self.attributes("-topmost", False)
    IDScannerModal(self, self.parse_scanned_text)

  def parse_scanned_text(self, raw_text):
    self.attributes("-topmost", True)
    self.focus_force()

    clean_lines = [
        line.strip()
        for line in raw_text.split("\n")
        if len(line.strip()) > 2
    ]

    if not clean_lines:
      self.show_status("Could not read ID. Try again.", color="#FF5555")
      return

    self.name_entry.delete(0, "end")
    self.reg_entry.delete(0, "end")

    reg_found = False
    name_found = False

    for line in clean_lines:
      if not reg_found and re.search(r"\d", line):
        self.reg_entry.insert(0, line)
        reg_found = True
      elif not name_found and not re.search(r"\d", line):
        self.name_entry.insert(0, line)
        name_found = True

    if not name_found and len(clean_lines) > 0:
      self.name_entry.insert(0, clean_lines[0])
    if not reg_found and len(clean_lines) > 1:
      self.reg_entry.insert(0, clean_lines[1])

    self.show_status("ID Scanned Successfully!", color="#50FA7B")

  def process_checkin(self):
    name = self.name_entry.get().strip()
    reg_no = self.reg_entry.get().strip()

    if not name or not reg_no:
      self.show_status("Please complete both fields.", color="#FF5555")
      return

    serial_no = self.get_next_serial()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow([serial_no, name, reg_no, timestamp])

    self.name_entry.delete(0, "end")
    self.reg_entry.delete(0, "end")
    self.show_status(
        f"Check-in #{serial_no} recorded successfully!", color="#50FA7B"
    )

  def show_status(self, message, color):
    self.status_label.configure(text=message, text_color=color)
    self.after(3500, lambda: self.status_label.configure(text=""))

  def prevent_close(self, event=None):
    return "break"

  def open_admin_modal(self, event=None):
    self.attributes("-topmost", False)
    AdminExitModal(self, self.handle_exit_decision)

  def handle_exit_decision(self, success):
    if success:
      self.destroy()
      sys.exit()
    else:
      self.attributes("-topmost", True)
      self.focus_force()


if __name__ == "__main__":
  app = EventKiosk()
  app.mainloop()