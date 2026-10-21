"""
VoltSynx - High-Performance Low-Latency Screen Mirroring & Streaming Application
Design System: Industrial Mechanical Minimalist
Product Name: Strictly "VoltSynx" everywhere
"""

import os
import sys
import subprocess
import re
from pathlib import Path
from typing import Optional, Tuple, Dict, Any, List

from PyQt6.QtCore import (
    Qt, QThread, pyqtSignal, QTimer, QSize, QSettings, QRect, QPoint, QRectF
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QLineEdit, QDialog, QRadioButton,
    QButtonGroup, QCheckBox, QFrame, QSizePolicy, QMessageBox, QSpacerItem,
    QGridLayout, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import (
    QPixmap, QFont, QColor, QPainter, QPainterPath, QIcon, QPen, QBrush,
    QPaintEvent, QResizeEvent
)

# ------------------------------------------------------------------------------
# 1. DESIGN TOKENS & STYLING CONSTANTS (Industrial Mechanical Minimalist)
# ------------------------------------------------------------------------------
APP_NAME = "VoltSynx"
APP_ORG = "VoltSynx"

# Exact Design Tokens from Design System
COLOR_BG = "#111111"                 # Canvas Dark (Never pure black #000000)
COLOR_CARD = "#161616"               # Elevated Card / Container
COLOR_CARD_HOVER = "#1C1C1C"         # Active / Hover Container
COLOR_BORDER = "rgba(231, 231, 231, 0.12)"  # Crisp 1px hairline border
COLOR_BORDER_STRONG = "rgba(231, 231, 231, 0.25)"
COLOR_TEXT_PRIMARY = "#E7E7E7"        # Crisp Alabaster
COLOR_TEXT_MUTED = "#8E8E8E"          # Technical Grey
COLOR_TEXT_FAINT = "#555555"          # Faint structural details
COLOR_AMBER = "#FFB020"               # Warm industrial amber / gold
COLOR_AMBER_HOVER = "#FFC64D"
COLOR_AMBER_PRESS = "#E09A10"
COLOR_AMBER_BG = "rgba(255, 176, 32, 0.12)"
COLOR_READY = "#4ADE80"               # Vibrant Ready Green
COLOR_READY_BG = "rgba(74, 222, 128, 0.12)"
COLOR_OFFLINE = "#F59E0B"             # Warning / Offline Amber
COLOR_OFFLINE_BG = "rgba(245, 158, 11, 0.12)"
COLOR_UNAUTH = "#EF4444"              # Unauthorized Red
COLOR_UNAUTH_BG = "rgba(239, 68, 68, 0.12)"

FONT_DISPLAY = '"Plus Jakarta Sans", "Segoe UI", "Inter", "Arial", sans-serif'
FONT_MONO = '"JetBrains Mono", "Cascadia Code", "Consolas", monospace'

# Windows creation flag to completely suppress CMD flashing
CREATE_NO_WINDOW_FLAG = 0x08000000 if sys.platform == "win32" else 0

GLOBAL_QSS = f"""
QWidget {{
    background-color: transparent;
    color: {COLOR_TEXT_PRIMARY};
    font-family: {FONT_DISPLAY};
    outline: none;
}}

QMainWindow {{
    background-color: {COLOR_BG};
}}

QDialog {{
    background-color: {COLOR_CARD};
    border: none;
    border-radius: 8px;
}}

/* Crisp hairline cards */
#leftPanelCard, #rightPanelCard, #headerCard, QFrame[class="hairline-card"], QFrame.hairline-card {{
    background-color: {COLOR_CARD};
    border: none;
    border-radius: 8px;
}}

QFrame[class="hairline-card"]:hover, QFrame.hairline-card:hover {{
    border: none;
}}

/* Top Navigation Header Buttons */
QPushButton[class="nav-btn"], QPushButton.nav-btn {{
    background-color: transparent;
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    color: {COLOR_TEXT_MUTED};
    font-family: {FONT_MONO};
    font-size: 11px;
    font-weight: 600;
    padding: 6px 14px;
    letter-spacing: 1px;
}}

QPushButton[class="nav-btn"]:hover, QPushButton.nav-btn:hover {{
    background-color: {COLOR_CARD_HOVER};
    color: {COLOR_TEXT_PRIMARY};
    border-color: {COLOR_BORDER_STRONG};
}}

QPushButton[class="nav-btn"]:pressed, QPushButton.nav-btn:pressed {{
    background-color: #222222;
}}

/* Premium / Accent Header Button */
QPushButton[class="nav-btn-accent"], QPushButton.nav-btn-accent {{
    background-color: {COLOR_AMBER_BG};
    border: 1px solid {COLOR_AMBER};
    border-radius: 4px;
    color: {COLOR_AMBER};
    font-family: {FONT_MONO};
    font-size: 11px;
    font-weight: 700;
    padding: 6px 14px;
    letter-spacing: 1.2px;
}}

QPushButton[class="nav-btn-accent"]:hover, QPushButton.nav-btn-accent:hover {{
    background-color: {COLOR_AMBER};
    color: #111111;
}}

/* Host Info Chip (Static) */
QLabel[class="host-chip"], QLabel.host-chip {{
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    color: {COLOR_TEXT_MUTED};
    font-family: {FONT_MONO};
    font-size: 11px;
    font-weight: 600;
    padding: 6px 12px;
    letter-spacing: 1px;
    background-color: rgba(255, 255, 255, 0.02);
}}

/* Platform Tabs */
QPushButton[class="platform-tab-active"], QPushButton.platform-tab-active {{
    background-color: #1E1E1E;
    border: 1px solid {COLOR_AMBER};
    border-radius: 4px;
    color: {COLOR_AMBER};
    font-family: {FONT_MONO};
    font-size: 12px;
    font-weight: 700;
    padding: 8px 18px;
    letter-spacing: 1.5px;
}}

QPushButton[class="platform-tab-disabled"], QPushButton.platform-tab-disabled {{
    background-color: transparent;
    border: 1px solid rgba(231, 231, 231, 0.06);
    border-radius: 4px;
    color: #4A4A4A;
    font-family: {FONT_MONO};
    font-size: 12px;
    font-weight: 600;
    padding: 8px 18px;
    letter-spacing: 1.5px;
}}

/* Segmented Connection Toggle Buttons */
QPushButton[class="seg-btn"], QPushButton.seg-btn {{
    background-color: #1A1A1A;
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    color: {COLOR_TEXT_MUTED};
    font-family: {FONT_MONO};
    font-size: 11px;
    font-weight: 600;
    padding: 8px 14px;
    letter-spacing: 0.5px;
}}

QPushButton[class="seg-btn"]:hover, QPushButton.seg-btn:hover {{
    background-color: #202020;
    color: {COLOR_TEXT_PRIMARY};
}}

QPushButton[class="seg-btn"][active="true"], QPushButton.seg-btn[active="true"] {{
    background-color: #242424;
    border: 1px solid {COLOR_TEXT_PRIMARY};
    color: {COLOR_TEXT_PRIMARY};
    font-weight: 700;
}}

/* Dropdowns / ComboBoxes */
QComboBox {{
    background-color: #181818;
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    color: {COLOR_TEXT_PRIMARY};
    font-family: {FONT_DISPLAY};
    font-size: 12px;
    padding: 7px 12px;
    min-height: 22px;
}}

QComboBox:hover {{
    border-color: {COLOR_BORDER_STRONG};
}}

QComboBox:focus {{
    border-color: {COLOR_AMBER};
}}

QComboBox::drop-down {{
    border: none;
    width: 24px;
}}

QComboBox::down-arrow {{
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid {COLOR_TEXT_MUTED};
    margin-right: 8px;
}}

QComboBox QAbstractItemView {{
    background-color: #161616;
    border: 1px solid {COLOR_BORDER_STRONG};
    border-radius: 4px;
    color: {COLOR_TEXT_PRIMARY};
    selection-background-color: #242424;
    selection-color: {COLOR_AMBER};
    padding: 4px;
    outline: none;
}}

/* Text Input Fields */
QLineEdit {{
    background-color: #181818;
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    color: {COLOR_TEXT_PRIMARY};
    font-family: {FONT_MONO};
    font-size: 12px;
    padding: 7px 10px;
}}

QLineEdit:focus {{
    border-color: {COLOR_AMBER};
}}

/* Primary Amber Action Button */
#actionBtn, QPushButton[class="action-btn"], QPushButton.action-btn {{
    background-color: {COLOR_AMBER};
    border: 1px solid {COLOR_AMBER};
    border-radius: 6px;
    color: #111111;
    font-family: {FONT_DISPLAY};
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 14px 20px;
}}

#actionBtn:hover, QPushButton[class="action-btn"]:hover {{
    background-color: {COLOR_AMBER_HOVER};
    border-color: {COLOR_AMBER_HOVER};
}}

#actionBtn:pressed, QPushButton[class="action-btn"]:pressed {{
    background-color: {COLOR_AMBER_PRESS};
    border-color: {COLOR_AMBER_PRESS};
}}

#actionBtn:disabled, QPushButton[class="action-btn"]:disabled {{
    background-color: #1C1C1C;
    border: 1px solid rgba(231, 231, 231, 0.08);
    color: #555555;
}}

/* Stop Streaming Active Button */
#actionBtn[mode="stop"], QPushButton[class="stop-btn"], QPushButton.stop-btn {{
    background-color: #DC2626;
    border: 1px solid #DC2626;
    border-radius: 6px;
    color: #FFFFFF;
    font-family: {FONT_DISPLAY};
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 14px 20px;
}}

#actionBtn[mode="stop"]:hover, QPushButton[class="stop-btn"]:hover {{
    background-color: #EF4444;
    border-color: #EF4444;
}}

/* Dialog Primary / Cancel Buttons */
QPushButton[class="dialog-save-btn"], QPushButton.dialog-save-btn {{
    background-color: {COLOR_AMBER};
    border: none;
    border-radius: 4px;
    color: #111111;
    font-family: {FONT_MONO};
    font-size: 12px;
    font-weight: 700;
    padding: 8px 18px;
    letter-spacing: 1px;
}}

QPushButton[class="dialog-save-btn"]:hover, QPushButton.dialog-save-btn:hover {{
    background-color: {COLOR_AMBER_HOVER};
}}

QPushButton[class="dialog-cancel-btn"], QPushButton.dialog-cancel-btn {{
    background-color: transparent;
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    color: {COLOR_TEXT_MUTED};
    font-family: {FONT_MONO};
    font-size: 12px;
    font-weight: 600;
    padding: 8px 18px;
    letter-spacing: 1px;
}}

QPushButton[class="dialog-cancel-btn"]:hover, QPushButton.dialog-cancel-btn:hover {{
    background-color: {COLOR_CARD_HOVER};
    color: {COLOR_TEXT_PRIMARY};
}}

/* CheckBoxes & Radio Buttons */
QCheckBox, QRadioButton {{
    color: {COLOR_TEXT_PRIMARY};
    font-size: 12px;
    spacing: 8px;
}}

QCheckBox::indicator, QRadioButton::indicator {{
    width: 16px;
    height: 16px;
    background-color: #181818;
    border: 1px solid {COLOR_BORDER};
    border-radius: 3px;
}}

QRadioButton::indicator {{
    border-radius: 8px;
}}

QCheckBox::indicator:hover, QRadioButton::indicator:hover {{
    border-color: {COLOR_AMBER};
}}

QCheckBox::indicator:checked, QRadioButton::indicator:checked {{
    background-color: {COLOR_AMBER};
    border-color: {COLOR_AMBER};
}}
"""


# ------------------------------------------------------------------------------
# 2. BINARY RESOLVER & ENVIRONMENT DETECTION
# ------------------------------------------------------------------------------
class BinaryResolver:
    """Safely locates local precompiled binaries for adb.exe and scrcpy.exe."""
    @staticmethod
    def get_base_dir() -> Path:
        return Path(__file__).resolve().parent

    @classmethod
    def get_bin_dir(cls) -> Path:
        base = cls.get_base_dir()
        candidate = base / "bin"
        if candidate.exists() and (candidate / "adb.exe").exists():
            return candidate

        # Check alternative common paths
        alt_paths = [
            Path("D:/My_Programs/VoltSynx-App/bin"),
            Path("C:/Users/garvi/.gemini/antigravity-ide/scratch/bin"),
        ]
        for p in alt_paths:
            if p.exists() and (p / "adb.exe").exists():
                return p
        return candidate

    @classmethod
    def get_adb_path(cls) -> str:
        exe = "adb.exe" if sys.platform == "win32" else "adb"
        p = cls.get_bin_dir() / exe
        return str(p)

    @classmethod
    def get_scrcpy_path(cls) -> str:
        exe = "scrcpy.exe" if sys.platform == "win32" else "scrcpy"
        p = cls.get_bin_dir() / exe
        return str(p)

    @classmethod
    def find_asset_image(cls) -> Optional[str]:
        base = cls.get_base_dir()
        search_dirs = [
            base / "assets",
            base.parent / "assets",
            Path("D:/My_Programs/VoltSynx-App/assets"),
        ]
        valid_exts = {".png", ".jpg", ".jpeg", ".webp"}
        for d in search_dirs:
            if d.exists() and d.is_dir():
                for item in d.iterdir():
                    if item.is_file() and item.suffix.lower() in valid_exts:
                        return str(item.resolve())
        return None


# ------------------------------------------------------------------------------
# 3. SETTINGS STORE (Persistent Configuration)
# ------------------------------------------------------------------------------
class AppConfig:
    def __init__(self):
        self.resolution: str = "1080p"
        self.bitrate: str = "16M"
        self.forward_audio: bool = True
        self.connection_mode: str = "usb"  # "usb" or "wireless"
        self.wireless_ip: str = ""
        self.capture_source: str = "screen"  # "screen", "cam_front", "cam_back"
        self.fps: int = 60
        self.load()

    def load(self):
        s = QSettings(APP_ORG, APP_NAME)
        self.resolution = str(s.value("stream/resolution", "1080p"))
        self.bitrate = str(s.value("stream/bitrate", "16M"))
        self.forward_audio = str(s.value("stream/forward_audio", "true")).lower() == "true"
        self.connection_mode = str(s.value("stream/connection_mode", "usb"))
        self.wireless_ip = str(s.value("stream/wireless_ip", ""))
        self.capture_source = str(s.value("stream/capture_source", "screen"))

    def save(self):
        s = QSettings(APP_ORG, APP_NAME)
        s.setValue("stream/resolution", self.resolution)
        s.setValue("stream/bitrate", self.bitrate)
        s.setValue("stream/forward_audio", str(self.forward_audio).lower())
        s.setValue("stream/connection_mode", self.connection_mode)
        s.setValue("stream/wireless_ip", self.wireless_ip)
        s.setValue("stream/capture_source", self.capture_source)


# ------------------------------------------------------------------------------
# 4. BACKGROUND ADB WORKER THREAD
# ------------------------------------------------------------------------------
class AdbWorkerThread(QThread):
    """
    Background worker thread polling `bin/adb.exe devices -l` every 1.5 seconds.
    Extracts device connection state and device model name cleanly without freezing the UI.
    """
    device_status_changed = pyqtSignal(str, str, str)  # status ("OFFLINE", "UNAUTHORIZED", "READY"), model_name, serial

    def __init__(self, parent=None):
        super().__init__(parent)
        self._running = True
        self.adb_path = BinaryResolver.get_adb_path()

    def run(self):
        while self._running:
            status, model, serial = self._query_devices()
            self.device_status_changed.emit(status, model, serial)
            self.msleep(1500)

    def stop(self):
        self._running = False
        self.wait(2000)

    def _query_devices(self) -> Tuple[str, str, str]:
        if not os.path.exists(self.adb_path):
            return "OFFLINE", "ADB BINARY NOT FOUND", ""

        # Strictly execute with shell=False and list of arguments
        cmd = [self.adb_path, "devices", "-l"]
        try:
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW_FLAG,
                timeout=4
            )
            out = res.stdout.strip()
            lines = out.splitlines()

            # Discard initial "List of devices attached" line
            device_lines = [l.strip() for l in lines if l.strip() and not l.startswith("List of devices")]
            if not device_lines:
                return "OFFLINE", "", ""

            # Check primary device
            for line in device_lines:
                parts = line.split()
                if len(parts) >= 2:
                    serial = parts[0]
                    state = parts[1].lower()

                    # Extract model:XXXX
                    model_match = re.search(r"model:([^\s]+)", line)
                    if model_match:
                        model_name = model_match.group(1).replace("_", " ")
                    else:
                        model_name = serial

                    if state == "device":
                        return "READY", model_name, serial
                    elif state == "unauthorized":
                        return "UNAUTHORIZED", model_name, serial
                    elif state == "offline":
                        return "OFFLINE", model_name, serial

            return "OFFLINE", "", ""

        except Exception:
            return "OFFLINE", "", ""


# ------------------------------------------------------------------------------
# 5. LEFT PANEL: RESPONSIVE ASSET IMAGE VISUALIZER
# ------------------------------------------------------------------------------
class AspectImageWidget(QWidget):
    """
    Smoothly renders hero mockup visualizer image maintaining aspect ratio without distortion.
    Gracefully displays a styled dark placeholder if no asset image is available.
    """
    def __init__(self, image_path: Optional[str] = None, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.pixmap: Optional[QPixmap] = None
        if self.image_path and os.path.exists(self.image_path):
            loaded = QPixmap(self.image_path)
            if not loaded.isNull():
                self.pixmap = loaded

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(320, 260)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        rect = self.rect()

        if self.pixmap and not self.pixmap.isNull():
            # Scale smoothly keeping aspect ratio
            scaled = self.pixmap.scaled(
                rect.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            x = (rect.width() - scaled.width()) // 2
            y = (rect.height() - scaled.height()) // 2
            painter.drawPixmap(x, y, scaled)
        else:
            # Draw industrial minimal placeholder card
            painter.fillRect(rect, QColor("#141414"))
            pen = QPen(QColor(231, 231, 231, 25))
            pen.setStyle(Qt.PenStyle.DashLine)
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawRoundedRect(rect.adjusted(12, 12, -12, -12), 4, 4)

            painter.setPen(QColor(COLOR_TEXT_MUTED))
            font = QFont("JetBrains Mono")
            font.setPixelSize(11)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "HARDWARE PREVIEW // NO ASSET FOUND")


# ------------------------------------------------------------------------------
# 6. MODAL DIALOGS (Settings, Login, Premium)
# ------------------------------------------------------------------------------
class SettingsDialog(QDialog):
    """Advanced Settings Dialog featuring Resolution, Bitrate, and Audio controls."""
    def __init__(self, config: AppConfig, parent=None):
        super().__init__(parent)
        self.config = config
        self.setWindowTitle("VoltSynx // Settings")
        self.setFixedSize(480, 430)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(GLOBAL_QSS)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        # Title Header
        title_box = QHBoxLayout()
        title_lbl = QLabel("STREAMING ENGINE // SETTINGS")
        title_lbl.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 13px;
            font-weight: 800;
            color: {COLOR_AMBER};
            letter-spacing: 1.5px;
        """)
        title_box.addWidget(title_lbl)
        title_box.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(28, 28)
        close_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                border-radius: 4px;
                color: {COLOR_TEXT_MUTED};
                font-size: 12px;
                font-weight: 700;
            }}
            QPushButton:hover {{
                background-color: {COLOR_CARD_HOVER};
                color: {COLOR_TEXT_PRIMARY};
            }}
        """)

        close_btn.clicked.connect(self.reject)
        title_box.addWidget(close_btn)
        layout.addLayout(title_box)

        # Hairline divider
        div = QFrame()
        div.setFixedHeight(1)
        div.setStyleSheet(f"background-color: {COLOR_BORDER};")
        layout.addWidget(div)

        # Resolution Selection Card
        res_card = QFrame()
        res_card.setFrameShape(QFrame.Shape.NoFrame)
        res_card.setProperty("class", "hairline-card")
        res_layout = QVBoxLayout(res_card)
        res_layout.setContentsMargins(14, 12, 14, 12)
        res_layout.setSpacing(10)

        res_lbl = QLabel("MAX ENCODING RESOLUTION")
        res_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; font-weight: 700; color: {COLOR_TEXT_MUTED}; letter-spacing: 1px;")
        res_layout.addWidget(res_lbl)

        self.res_group = QButtonGroup(self)
        res_btn_layout = QHBoxLayout()
        self.res_radios = {}
        for r in ["720p", "1080p", "2K/4K"]:
            rb = QRadioButton(r)
            if self.config.resolution == r:
                rb.setChecked(True)
            self.res_group.addButton(rb)
            self.res_radios[r] = rb
            res_btn_layout.addWidget(rb)
        res_layout.addLayout(res_btn_layout)
        layout.addWidget(res_card)

        # Bitrate Selection Card
        bit_card = QFrame()
        bit_card.setFrameShape(QFrame.Shape.NoFrame)
        bit_card.setProperty("class", "hairline-card")
        bit_layout = QVBoxLayout(bit_card)
        bit_layout.setContentsMargins(14, 12, 14, 12)
        bit_layout.setSpacing(10)

        bit_lbl = QLabel("STREAM BITRATE ALLOCATION")
        bit_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; font-weight: 700; color: {COLOR_TEXT_MUTED}; letter-spacing: 1px;")
        bit_layout.addWidget(bit_lbl)

        self.bit_group = QButtonGroup(self)
        bit_btn_layout = QHBoxLayout()
        self.bit_radios = {}
        for b in ["8M", "16M", "30M", "50M"]:
            rb = QRadioButton(b)
            if self.config.bitrate == b:
                rb.setChecked(True)
            self.bit_group.addButton(rb)
            self.bit_radios[b] = rb
            bit_btn_layout.addWidget(rb)
        bit_layout.addLayout(bit_btn_layout)
        layout.addWidget(bit_card)

        # Audio Forwarding Card
        audio_card = QFrame()
        audio_card.setFrameShape(QFrame.Shape.NoFrame)
        audio_card.setProperty("class", "hairline-card")
        audio_layout = QHBoxLayout(audio_card)
        audio_layout.setContentsMargins(14, 12, 14, 12)

        self.audio_chk = QCheckBox("FORWARD SYSTEM AUDIO VIA OPUS CODEC")
        self.audio_chk.setChecked(self.config.forward_audio)
        self.audio_chk.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 600; color: {COLOR_TEXT_PRIMARY};")
        audio_layout.addWidget(self.audio_chk)
        layout.addWidget(audio_card)

        layout.addStretch()

        # Action Buttons
        btn_box = QHBoxLayout()
        btn_box.addStretch()

        cancel_btn = QPushButton("CANCEL")
        cancel_btn.setProperty("class", "dialog-cancel-btn")
        cancel_btn.clicked.connect(self.reject)
        btn_box.addWidget(cancel_btn)

        save_btn = QPushButton("SAVE SETTINGS")
        save_btn.setProperty("class", "dialog-save-btn")
        save_btn.clicked.connect(self._save_and_close)
        btn_box.addWidget(save_btn)

        layout.addLayout(btn_box)

    def _save_and_close(self):
        for r, rb in self.res_radios.items():
            if rb.isChecked():
                self.config.resolution = r
                break
        for b, rb in self.bit_radios.items():
            if rb.isChecked():
                self.config.bitrate = b
                break
        self.config.forward_audio = self.audio_chk.isChecked()
        self.config.save()
        self.accept()


class LoginModal(QDialog):
    """User account authentication modal."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("VoltSynx // Account Login")
        self.setFixedSize(420, 360)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(GLOBAL_QSS)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(14)

        # Header
        top = QHBoxLayout()
        lbl = QLabel("VOLTSYNX // ACCOUNT LOGIN")
        lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 12px; font-weight: 800; color: {COLOR_AMBER}; letter-spacing: 1.5px;")
        top.addWidget(lbl)
        top.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(26, 26)
        close_btn.setStyleSheet(f"background: transparent; border: none; color: {COLOR_TEXT_MUTED}; font-size: 12px;")
        close_btn.clicked.connect(self.reject)
        top.addWidget(close_btn)
        layout.addLayout(top)

        sub = QLabel("AUTHENTICATE HARDWARE PROFILE & CLOUD REPOS")
        sub.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; color: {COLOR_TEXT_MUTED}; letter-spacing: 0.5px;")
        layout.addWidget(sub)

        div = QFrame()
        div.setFixedHeight(1)
        div.setStyleSheet(f"background-color: {COLOR_BORDER}; margin: 4px 0;")
        layout.addWidget(div)

        # Inputs
        usr_lbl = QLabel("OPERATOR IDENTITY / EMAIL")
        usr_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; color: {COLOR_TEXT_MUTED}; font-weight: 700;")
        layout.addWidget(usr_lbl)
        self.usr_in = QLineEdit()
        self.usr_in.setPlaceholderText("engineer@voltsynx.io")
        layout.addWidget(self.usr_in)

        pwd_lbl = QLabel("ACCESS TOKEN / PASSWORD")
        pwd_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; color: {COLOR_TEXT_MUTED}; font-weight: 700;")
        layout.addWidget(pwd_lbl)
        self.pwd_in = QLineEdit()
        self.pwd_in.setEchoMode(QLineEdit.EchoMode.Password)
        self.pwd_in.setPlaceholderText("••••••••••••••••")
        layout.addWidget(self.pwd_in)

        layout.addStretch()

        submit_btn = QPushButton("AUTHENTICATE SESSION")
        submit_btn.setProperty("class", "dialog-save-btn")
        submit_btn.clicked.connect(self._handle_login)
        layout.addWidget(submit_btn)

    def _handle_login(self):
        QMessageBox.information(self, "Session Initialized", "Hardware link authenticated successfully.")
        self.accept()


class PremiumModal(QDialog):
    """VIP Premium Upgrade Modal."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("VoltSynx // VIP Upgrade")
        self.setFixedSize(480, 420)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(GLOBAL_QSS)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(14)

        top = QHBoxLayout()
        lbl = QLabel("VOLTSYNX // PRO ARCHITECTURE")
        lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 13px; font-weight: 800; color: {COLOR_AMBER}; letter-spacing: 1.5px;")
        top.addWidget(lbl)
        top.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(26, 26)
        close_btn.setStyleSheet(f"background: transparent; border: 1px solid {COLOR_BORDER}; color: {COLOR_TEXT_MUTED};")
        close_btn.clicked.connect(self.reject)
        top.addWidget(close_btn)
        layout.addLayout(top)

        div = QFrame()
        div.setFixedHeight(1)
        div.setStyleSheet(f"background-color: {COLOR_BORDER};")
        layout.addWidget(div)

        features = [
            ("DIRECT3D 11 ULTRA LOW-LATENCY SWAPCHAIN", "Sub-0.8ms screen frame rendering pipeline directly on GPU"),
            ("120 FPS HIGH-REFRESH STREAMING", "Native uncompressed capture for competitive tactical gaming"),
            ("PRO DUAL-FACING CAMERA FEEDS", "Simultaneous front & back multi-angle hardware input loopback"),
            ("VIRTUAL OBS WEBCAM EMULATION", "System driver level hook for Discord, OBS Studio, and Twitch")
        ]

        for title, desc in features:
            card = QFrame()
            card.setProperty("class", "hairline-card")
            c_lay = QVBoxLayout(card)
            c_lay.setContentsMargins(12, 10, 12, 10)
            c_lay.setSpacing(4)

            t = QLabel(f"⚡ {title}")
            t.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 800; color: {COLOR_TEXT_PRIMARY};")
            d = QLabel(desc)
            d.setStyleSheet(f"font-size: 11px; color: {COLOR_TEXT_MUTED};")
            c_lay.addWidget(t)
            c_lay.addWidget(d)
            layout.addWidget(card)

        layout.addStretch()

        up_btn = QPushButton("ACTIVATE VOLTSYNX ENTERPRISE PRO")
        up_btn.setProperty("class", "dialog-save-btn")
        up_btn.clicked.connect(self._handle_upgrade)
        layout.addWidget(up_btn)

    def _handle_upgrade(self):
        QMessageBox.information(self, "Enterprise License", "VoltSynx Enterprise Pipeline active on this workstation.")
        self.accept()


# ------------------------------------------------------------------------------
# 7. MAIN WINDOW (Full Desktop App UI & Engine Workflow)
# ------------------------------------------------------------------------------
class VoltSynxMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VoltSynx")
        self.resize(1180, 760)
        self.setMinimumSize(960, 620)
        self.setStyleSheet(GLOBAL_QSS)

        self.config = AppConfig()
        self.scrcpy_proc: Optional[subprocess.Popen] = None
        self.current_status: str = "OFFLINE"
        self.current_model: str = ""
        self.current_serial: str = ""

        # Central Layout
        central_widget = QWidget(self)
        central_widget.setObjectName("centralWidget")
        self.setCentralWidget(central_widget)

        self.root_layout = QVBoxLayout(central_widget)
        self.root_layout.setContentsMargins(28, 20, 28, 28)
        self.root_layout.setSpacing(20)

        # Build UI Components
        self._build_top_header()
        self._build_main_split_view()

        # Stream monitoring timer
        self.stream_monitor_timer = QTimer(self)
        self.stream_monitor_timer.setInterval(800)
        self.stream_monitor_timer.timeout.connect(self._check_stream_process)

        # Background ADB Worker
        self.adb_worker = AdbWorkerThread(self)
        self.adb_worker.device_status_changed.connect(self._on_device_status_updated)
        self.adb_worker.start()

        # Initial UI state sync
        self._update_status_ui("OFFLINE", "", "")

    # --------------------------------------------------------------------------
    # TOP HEADER NAVIGATION BAR
    # --------------------------------------------------------------------------
    def _build_top_header(self):
        header_container = QFrame()
        header_container.setObjectName("headerCard")
        header_container.setFrameShape(QFrame.Shape.StyledPanel)
        header_container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        header_layout = QHBoxLayout(header_container)
        header_layout.setContentsMargins(18, 10, 18, 10)
        header_layout.setSpacing(12)

        # Brand Wordmark (Strictly "VoltSynx" everywhere)
        wordmark_box = QHBoxLayout()
        wordmark_box.setSpacing(8)

        brand_lbl = QLabel("VOLTSYNX")
        brand_lbl.setStyleSheet(f"""
            font-family: {FONT_DISPLAY};
            font-size: 20px;
            font-weight: 900;
            color: {COLOR_TEXT_PRIMARY};
            letter-spacing: -0.5px;
        """)
        wordmark_box.addWidget(brand_lbl)

        # Subtle hardware telemetry badge next to brand
        telemetry_badge = QLabel("60 FPS // D3D11")
        telemetry_badge.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 10px;
            font-weight: 700;
            color: {COLOR_AMBER};
            border: 1px solid rgba(255, 176, 32, 0.3);
            border-radius: 3px;
            padding: 2px 6px;
            letter-spacing: 1px;
            background-color: {COLOR_AMBER_BG};
        """)
        wordmark_box.addWidget(telemetry_badge)
        header_layout.addLayout(wordmark_box)

        header_layout.addStretch()

        # Right items (Clickable chips / buttons)
        host_badge = QLabel("HOST // WINDOWS 11")
        host_badge.setProperty("class", "host-chip")
        header_layout.addWidget(host_badge)

        day_night_btn = QPushButton("DAY / NIGHT")
        day_night_btn.setProperty("class", "nav-btn")
        day_night_btn.clicked.connect(self._on_day_night_clicked)
        header_layout.addWidget(day_night_btn)

        login_btn = QPushButton("LOG IN")
        login_btn.setProperty("class", "nav-btn")
        login_btn.clicked.connect(self._open_login_dialog)
        header_layout.addWidget(login_btn)

        premium_btn = QPushButton("PREMIUM")
        premium_btn.setProperty("class", "nav-btn-accent")
        premium_btn.clicked.connect(self._open_premium_dialog)
        header_layout.addWidget(premium_btn)

        settings_btn = QPushButton("SETTINGS")
        settings_btn.setProperty("class", "nav-btn")
        settings_btn.clicked.connect(self._open_settings_dialog)
        header_layout.addWidget(settings_btn)

        self.root_layout.addWidget(header_container)

        # 1px Hairline divider under header
        header_divider = QFrame()
        header_divider.setFixedHeight(1)
        header_divider.setStyleSheet(f"background-color: {COLOR_BORDER};")
        self.root_layout.addWidget(header_divider)

    # --------------------------------------------------------------------------
    # MAIN SPLIT VIEW (Left Visualizer & Right Workflow)
    # --------------------------------------------------------------------------
    def _build_main_split_view(self):
        split_layout = QHBoxLayout()
        split_layout.setContentsMargins(0, 8, 0, 0)
        split_layout.setSpacing(24)

        # Left Panel (Image Visualizer)
        left_panel = self._create_left_panel()
        split_layout.addWidget(left_panel, 5)

        # Right Panel (Dashboard Workflow & Onboarding)
        right_panel = self._create_right_panel()
        split_layout.addWidget(right_panel, 6)

        self.root_layout.addLayout(split_layout)

    # --------------------------------------------------------------------------
    # LEFT PANEL: ASSET IMAGE VISUALIZER
    # --------------------------------------------------------------------------
    def _create_left_panel(self) -> QWidget:
        container = QFrame()
        container.setObjectName("leftPanelCard")
        container.setFrameShape(QFrame.Shape.NoFrame)
        container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        container.setProperty("class", "hairline-card")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 16)
        layout.setSpacing(14)

        # Panel Subtitle / Hardware Tag
        top_tag = QLabel("HARDWARE PIPELINE // DIRECT USB TRANSPORT")
        top_tag.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 10px;
            font-weight: 700;
            color: {COLOR_TEXT_MUTED};
            letter-spacing: 1.5px;
        """)
        layout.addWidget(top_tag)

        # Asset Image Loading
        asset_file = BinaryResolver.find_asset_image()
        self.image_widget = AspectImageWidget(asset_file, self)
        layout.addWidget(self.image_widget)

        # Monospaced Telemetry Footer
        footer_telemetry = QLabel("• WIRED LINK  •  USB-C  •  ZERO CLOUD, ZERO ACCOUNT")
        footer_telemetry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_telemetry.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 10px;
            font-weight: 700;
            color: {COLOR_TEXT_MUTED};
            letter-spacing: 1.2px;
            padding: 8px;
            border-top: 1px solid rgba(231, 231, 231, 0.08);
        """)
        layout.addWidget(footer_telemetry)

        return container

    # --------------------------------------------------------------------------
    # RIGHT PANEL: WORKFLOW & 3-STEP ONBOARDING
    # --------------------------------------------------------------------------
    def _create_right_panel(self) -> QWidget:
        container = QFrame()
        container.setObjectName("rightPanelCard")
        container.setFrameShape(QFrame.Shape.NoFrame)
        container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        container.setProperty("class", "hairline-card")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(16)

        # 1. Tab Switcher: [ ANDROID ] (active) | [ IPHONE - SOON ] (disabled)
        tab_layout = QHBoxLayout()
        tab_layout.setSpacing(10)

        self.android_tab = QPushButton("[ ANDROID ]")
        self.android_tab.setProperty("class", "platform-tab-active")
        tab_layout.addWidget(self.android_tab)

        self.iphone_tab = QPushButton("[ IPHONE — SOON ]")
        self.iphone_tab.setProperty("class", "platform-tab-disabled")
        self.iphone_tab.setEnabled(False)
        tab_layout.addWidget(self.iphone_tab)

        tab_layout.addStretch()
        layout.addLayout(tab_layout)

        # 2. Connection Mode & Capture Source Row
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(14)

        # Connection Mode Toggle
        mode_box = QVBoxLayout()
        mode_box.setSpacing(6)
        mode_title = QLabel("CONNECTION TRANSPORT")
        mode_title.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 9px; font-weight: 700; color: {COLOR_TEXT_MUTED}; letter-spacing: 1px;")
        mode_box.addWidget(mode_title)

        seg_box = QHBoxLayout()
        seg_box.setSpacing(4)
        self.btn_wired = QPushButton("🔌 Wired USB")
        self.btn_wired.setProperty("class", "seg-btn")
        self.btn_wired.setProperty("active", "true" if self.config.connection_mode == "usb" else "false")
        self.btn_wired.clicked.connect(lambda: self._set_conn_mode("usb"))
        seg_box.addWidget(self.btn_wired)

        self.btn_wireless = QPushButton("📶 Wireless Wi-Fi")
        self.btn_wireless.setProperty("class", "seg-btn")
        self.btn_wireless.setProperty("active", "true" if self.config.connection_mode == "wireless" else "false")
        self.btn_wireless.clicked.connect(lambda: self._set_conn_mode("wireless"))
        seg_box.addWidget(self.btn_wireless)
        mode_box.addLayout(seg_box)
        controls_layout.addLayout(mode_box, 1)

        # Capture Source Dropdown
        source_box = QVBoxLayout()
        source_box.setSpacing(6)
        source_title = QLabel("CAPTURE SOURCE")
        source_title.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 9px; font-weight: 700; color: {COLOR_TEXT_MUTED}; letter-spacing: 1px;")
        source_box.addWidget(source_title)

        self.source_combo = QComboBox()
        self.source_combo.addItem("📱 Screen Mirroring (Default)", "screen")
        self.source_combo.addItem("📷 Phone Camera (Front)", "cam_front")
        self.source_combo.addItem("📸 Phone Camera (Back)", "cam_back")
        self.source_combo.currentIndexChanged.connect(self._on_source_changed)
        source_box.addWidget(self.source_combo)
        controls_layout.addLayout(source_box, 1)

        layout.addLayout(controls_layout)

        # Wireless IP Input Box (Revealed when wireless mode is selected)
        self.ip_container = QWidget()
        ip_layout = QHBoxLayout(self.ip_container)
        ip_layout.setContentsMargins(0, 0, 0, 0)
        ip_layout.setSpacing(8)

        ip_lbl = QLabel("PHONE IP:")
        ip_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 700; color: {COLOR_AMBER};")
        ip_layout.addWidget(ip_lbl)

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("e.g. 192.168.1.100:5555")
        self.ip_input.setText(self.config.wireless_ip)
        self.ip_input.textChanged.connect(self._on_ip_changed)
        ip_layout.addWidget(self.ip_input)

        connect_ip_btn = QPushButton("CONNECT")
        connect_ip_btn.setProperty("class", "nav-btn-accent")
        connect_ip_btn.clicked.connect(self._connect_wireless_adb)
        ip_layout.addWidget(connect_ip_btn)

        self.ip_container.setVisible(self.config.connection_mode == "wireless")
        layout.addWidget(self.ip_container)

        # 3. Dynamic 3-Step Guide (01, 02, 03)
        guide_label = QLabel("HARDWARE ONBOARDING SEQUENCE")
        guide_label.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 9px; font-weight: 800; color: {COLOR_TEXT_MUTED}; letter-spacing: 1.5px; margin-top: 4px;")
        layout.addWidget(guide_label)

        self.step_cards = []
        steps_data = [
            ("01", "ENABLE DEVELOPER MODE", "Settings > About phone > Tap Build number 7 times"),
            ("02", "TURN ON USB DEBUGGING", "Settings > System > Developer options"),
            ("03", "PLUG IN & AUTHORIZE", "Tap 'Allow USB debugging' when prompted on device")
        ]

        for num, title, desc in steps_data:
            card, num_lbl, text_lbl = self._create_step_row(num, title, desc)
            layout.addWidget(card)
            self.step_cards.append((card, num_lbl, text_lbl))

        layout.addStretch()

        # 4. Dynamic Status Bar
        self.status_card = QFrame()
        self.status_card.setStyleSheet(f"""
            QFrame {{
                background-color: #171717;
                border: none;
                border-radius: 6px;
                padding: 6px 10px;
            }}
        """)
        status_layout = QHBoxLayout(self.status_card)
        status_layout.setContentsMargins(12, 10, 12, 10)
        status_layout.setSpacing(12)

        self.status_dot = QLabel("●")
        self.status_dot.setStyleSheet(f"font-size: 14px; color: {COLOR_OFFLINE};")
        status_layout.addWidget(self.status_dot)

        self.status_text = QLabel("NO DEVICE DETECTED — CONNECT THE USB CABLE")
        self.status_text.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 11px;
            font-weight: 700;
            color: {COLOR_OFFLINE};
            letter-spacing: 0.8px;
        """)
        status_layout.addWidget(self.status_text, 1)

        self.status_badge = QLabel("OFFLINE")
        self.status_badge.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 10px;
            font-weight: 800;
            color: #8E8E8E;
            background-color: #222222;
            border: 1px solid rgba(231, 231, 231, 0.1);
            border-radius: 3px;
            padding: 3px 8px;
            letter-spacing: 1px;
        """)
        status_layout.addWidget(self.status_badge)

        layout.addWidget(self.status_card)

        # 5. Primary Action Button
        self.action_btn = QPushButton("START SCREENING")
        self.action_btn.setObjectName("actionBtn")
        self.action_btn.setProperty("class", "action-btn")
        self.action_btn.setProperty("mode", "start")
        self.action_btn.setEnabled(False)
        self.action_btn.clicked.connect(self._handle_action_button)
        layout.addWidget(self.action_btn)

        return container

    def _create_step_row(self, num: str, title: str, desc: str) -> Tuple[QFrame, QLabel, QLabel]:
        card = QFrame()
        card.setFrameShape(QFrame.Shape.NoFrame)
        card.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        row = QHBoxLayout(card)
        row.setContentsMargins(8, 6, 8, 6)
        row.setSpacing(8)

        num_lbl = QLabel(num)
        num_lbl.setStyleSheet(f"""
            font-family: {FONT_MONO};
            font-size: 13px;
            font-weight: 800;
            color: {COLOR_TEXT_MUTED};
            letter-spacing: 1px;
        """)
        row.addWidget(num_lbl)

        txt_box = QVBoxLayout()
        txt_box.setSpacing(2)

        t_lbl = QLabel(title)
        t_lbl.setStyleSheet(f"""
            font-family: {FONT_DISPLAY};
            font-size: 11px;
            font-weight: 800;
            color: {COLOR_TEXT_PRIMARY};
            letter-spacing: 0.5px;
        """)
        txt_box.addWidget(t_lbl)

        d_lbl = QLabel(desc)
        d_lbl.setStyleSheet(f"font-size: 10px; color: {COLOR_TEXT_MUTED};")
        txt_box.addWidget(d_lbl)

        row.addLayout(txt_box, 1)

        return card, num_lbl, t_lbl

    # --------------------------------------------------------------------------
    # INTERACTIVE CONTROLS & STATE LOGIC
    # --------------------------------------------------------------------------
    def _set_conn_mode(self, mode: str):
        self.config.connection_mode = mode
        self.config.save()
        self.btn_wired.setProperty("active", "true" if mode == "usb" else "false")
        self.btn_wireless.setProperty("active", "true" if mode == "wireless" else "false")
        self.btn_wired.style().unpolish(self.btn_wired)
        self.btn_wired.style().polish(self.btn_wired)
        self.btn_wireless.style().unpolish(self.btn_wireless)
        self.btn_wireless.style().polish(self.btn_wireless)

        self.ip_container.setVisible(mode == "wireless")

    def _on_source_changed(self, index: int):
        source_data = self.source_combo.currentData()
        self.config.capture_source = str(source_data)
        self.config.save()

    def _on_ip_changed(self, text: str):
        self.config.wireless_ip = text.strip()
        self.config.save()

    def _connect_wireless_adb(self):
        ip = self.config.wireless_ip.strip()
        if not ip:
            QMessageBox.warning(self, "Input Required", "Please enter phone IP address (e.g. 192.168.1.100:5555)")
            return

        adb = BinaryResolver.get_adb_path()
        if not os.path.exists(adb):
            QMessageBox.critical(self, "Binary Error", f"adb.exe not found at:\n{adb}")
            return

        cmd = [adb, "connect", ip]
        try:
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW_FLAG,
                timeout=5
            )
            QMessageBox.information(self, "Wireless Connect", f"ADB output:\n{res.stdout.strip()}")
        except Exception as e:
            QMessageBox.critical(self, "Connect Error", str(e))

    def _on_device_status_updated(self, status: str, model_name: str, serial: str):
        self.current_status = status
        self.current_model = model_name
        self.current_serial = serial

        # Only update status bar if scrcpy is not actively running
        if self.scrcpy_proc is None or self.scrcpy_proc.poll() is not None:
            self._update_status_ui(status, model_name, serial)

    def _update_status_ui(self, status: str, model_name: str, serial: str):
        is_streaming = (self.scrcpy_proc is not None and self.scrcpy_proc.poll() is None)

        if is_streaming:
            self.status_dot.setText("⚡")
            self.status_dot.setStyleSheet(f"font-size: 14px; color: {COLOR_AMBER};")
            self.status_text.setText(f"SCREENING ACTIVE: {self.current_model or 'ANDROID'}")
            self.status_text.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 700; color: {COLOR_AMBER}; letter-spacing: 0.8px;")
            self.status_badge.setText("LIVE")
            self.status_badge.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; font-weight: 800; color: {COLOR_AMBER}; background-color: {COLOR_AMBER_BG}; border: 1px solid {COLOR_AMBER}; border-radius: 3px; padding: 3px 8px;")

            self.action_btn.setEnabled(True)
            self.action_btn.setText("STOP SCREENING")
            self.action_btn.setProperty("mode", "stop")
            self.action_btn.setProperty("class", "stop-btn")
            self.action_btn.style().unpolish(self.action_btn)
            self.action_btn.style().polish(self.action_btn)
            return

        if status == "READY":
            display_name = model_name if model_name else "DEVICE"
            self.status_dot.setText("●")
            self.status_dot.setStyleSheet(f"font-size: 14px; color: {COLOR_READY};")
            self.status_text.setText(f"DEVICE CONNECTED: {display_name}")
            self.status_text.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 700; color: {COLOR_READY}; letter-spacing: 0.8px;")

            self.status_badge.setText("READY")
            self.status_badge.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; font-weight: 800; color: {COLOR_READY}; background-color: {COLOR_READY_BG}; border: 1px solid {COLOR_READY}; border-radius: 3px; padding: 3px 8px;")

            # Highlight 3-step guide in vibrant ready green
            for card, num_lbl, text_lbl in self.step_cards:                card.setStyleSheet(f"QFrame {{ background-color: #121E16; border: none; border-radius: 4px; }}")
                num_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 13px; font-weight: 800; color: {COLOR_READY};")
                text_lbl.setStyleSheet(f"font-family: {FONT_DISPLAY}; font-size: 11px; font-weight: 800; color: #FFFFFF;")

            self.action_btn.setEnabled(True)
            self.action_btn.setText("START SCREENING")
            self.action_btn.setProperty("mode", "start")
            self.action_btn.setProperty("class", "action-btn")
            self.action_btn.style().unpolish(self.action_btn)
            self.action_btn.style().polish(self.action_btn)

        elif status == "UNAUTHORIZED":
            self.status_dot.setText("●")
            self.status_dot.setStyleSheet(f"font-size: 14px; color: {COLOR_UNAUTH};")
            self.status_text.setText("DEVICE DETECTED — UNCONFIRMED USB DEBUGGING")
            self.status_text.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 700; color: {COLOR_UNAUTH}; letter-spacing: 0.8px;")

            self.status_badge.setText("UNAUTHORIZED")
            self.status_badge.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; font-weight: 800; color: {COLOR_UNAUTH}; background-color: {COLOR_UNAUTH_BG}; border: 1px solid {COLOR_UNAUTH}; border-radius: 3px; padding: 3px 8px;")

            # Step 1 & 2 muted green, Step 3 amber highlight
            self.step_cards[0][0].setStyleSheet(f"QFrame {{ background-color: #141414; border: none; border-radius: 4px; }}")
            self.step_cards[1][0].setStyleSheet(f"QFrame {{ background-color: #141414; border: none; border-radius: 4px; }}")
            self.step_cards[2][0].setStyleSheet(f"QFrame {{ background-color: #1E1B12; border: none; border-radius: 4px; }}")
            self.step_cards[2][1].setStyleSheet(f"font-family: {FONT_MONO}; font-size: 13px; font-weight: 800; color: {COLOR_AMBER};")

            self.action_btn.setEnabled(False)
            self.action_btn.setText("START SCREENING")
            self.action_btn.setProperty("mode", "start")
            self.action_btn.setProperty("class", "action-btn")
            self.action_btn.style().unpolish(self.action_btn)
            self.action_btn.style().polish(self.action_btn)

        else:  # OFFLINE
            self.status_dot.setText("●")
            self.status_dot.setStyleSheet(f"font-size: 14px; color: {COLOR_OFFLINE};")
            self.status_text.setText("NO DEVICE DETECTED — CONNECT THE USB CABLE")
            self.status_text.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 11px; font-weight: 700; color: {COLOR_OFFLINE}; letter-spacing: 0.8px;")

            self.status_badge.setText("OFFLINE")
            self.status_badge.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 10px; font-weight: 800; color: #8E8E8E; background-color: #222222; border: 1px solid rgba(231, 231, 231, 0.1); border-radius: 3px; padding: 3px 8px;")

            # Reset step cards to muted styling
            for card, num_lbl, text_lbl in self.step_cards:
                card.setStyleSheet(f"QFrame {{ background-color: #141414; border: none; border-radius: 4px; }}")

                num_lbl.setStyleSheet(f"font-family: {FONT_MONO}; font-size: 13px; font-weight: 800; color: {COLOR_TEXT_MUTED};")
                text_lbl.setStyleSheet(f"font-family: {FONT_DISPLAY}; font-size: 11px; font-weight: 800; color: {COLOR_TEXT_PRIMARY};")

            self.action_btn.setEnabled(False)
            self.action_btn.setText("START SCREENING")
            self.action_btn.setProperty("mode", "start")
            self.action_btn.setProperty("class", "action-btn")
            self.action_btn.style().unpolish(self.action_btn)
            self.action_btn.style().polish(self.action_btn)

    # --------------------------------------------------------------------------
    # SCRCPY STREAM EXECUTION & PROCESS SUPERVISION
    # --------------------------------------------------------------------------
    def _handle_action_button(self):
        if self.scrcpy_proc is not None and self.scrcpy_proc.poll() is None:
            self._stop_stream()
        else:
            self._start_stream()

    def _start_stream(self):
        scrcpy_exe = BinaryResolver.get_scrcpy_path()
        if not os.path.exists(scrcpy_exe):
            QMessageBox.critical(self, "Binary Error", f"scrcpy.exe not found at:\n{scrcpy_exe}")
            return

        cmd: List[str] = [scrcpy_exe]

        # Resolution & Source handling
        source = self.config.capture_source
        if source == "screen":
            # Screen Mirroring: pass --max-size based on selected resolution
            if self.config.resolution == "720p":
                cmd.append("--max-size=1280")
            elif self.config.resolution == "1080p":
                cmd.append("--max-size=1920")
            elif self.config.resolution == "2K/4K":
                cmd.append("--max-size=3840")
        elif source == "cam_front":
            # Camera mode: do NOT pass --max-size
            cmd.extend([
                "--video-source=camera",
                "--camera-facing=front",
                "--camera-size=1920x1080"
            ])
        elif source == "cam_back":
            # Camera mode: do NOT pass --max-size
            cmd.extend([
                "--video-source=camera",
                "--camera-facing=back",
                "--camera-size=1920x1080"
            ])

        # Bitrate & Framerate
        cmd.append(f"--video-bit-rate={self.config.bitrate}")
        cmd.append(f"--max-fps={self.config.fps}")

        # Audio routing
        if self.config.forward_audio:
            cmd.append("--audio-codec=opus")
        else:
            cmd.append("--no-audio")

        # Exclusive target transport
        if self.config.connection_mode == "wireless" and self.config.wireless_ip:
            cmd.extend(["-s", self.config.wireless_ip])
        elif self.current_serial:
            cmd.extend(["-s", self.current_serial])
        else:
            cmd.append("-d")

        # Custom window title
        device_title = self.current_model or "Mobile"
        cmd.append(f"--window-title=VoltSynx - {device_title}")

        bin_dir = BinaryResolver.get_bin_dir()
        env = os.environ.copy()
        env["ADB"] = BinaryResolver.get_adb_path()
        env["SCRCPY_SERVER_PATH"] = str(bin_dir / "scrcpy-server")

        # Strict Security Rule: Never use shell=True, pass arguments strictly as a Python list
        try:
            self.scrcpy_proc = subprocess.Popen(
                cmd,
                cwd=str(bin_dir),
                env=env,
                creationflags=CREATE_NO_WINDOW_FLAG
            )
            self.stream_monitor_timer.start()
            self._update_status_ui(self.current_status, self.current_model, self.current_serial)

        except Exception as e:
            QMessageBox.critical(self, "Stream Launch Failed", f"Could not start scrcpy:\n{str(e)}")

    def _stop_stream(self):
        if self.scrcpy_proc is not None:
            try:
                self.scrcpy_proc.terminate()
                self.scrcpy_proc.wait(timeout=2)
            except Exception:
                try:
                    self.scrcpy_proc.kill()
                except Exception:
                    pass
            self.scrcpy_proc = None

        self.stream_monitor_timer.stop()
        self._update_status_ui(self.current_status, self.current_model, self.current_serial)

    def _check_stream_process(self):
        if self.scrcpy_proc is not None:
            ret = self.scrcpy_proc.poll()
            if ret is not None:
                self.scrcpy_proc = None
                self.stream_monitor_timer.stop()
                self._update_status_ui(self.current_status, self.current_model, self.current_serial)

    # --------------------------------------------------------------------------
    # HEADER ACTIONS & MODALS
    # --------------------------------------------------------------------------
    def _open_settings_dialog(self):
        dlg = SettingsDialog(self.config, self)
        dlg.exec()

    def _open_login_dialog(self):
        dlg = LoginModal(self)
        dlg.exec()

    def _open_premium_dialog(self):
        dlg = PremiumModal(self)
        dlg.exec()

    def _on_day_night_clicked(self):
        QMessageBox.information(
            self,
            "VoltSynx Theme System",
            "Industrial Mechanical Minimalist (Dark Canvas #111111) is active.\n"
            "High-contrast OLED black borders and crisp 1px hairline cards are locked for zero glare."
        )

    def closeEvent(self, event):
        if self.scrcpy_proc is not None:
            try:
                self.scrcpy_proc.terminate()
            except Exception:
                pass
        if hasattr(self, "adb_worker"):
            self.adb_worker.stop()
        event.accept()


# ------------------------------------------------------------------------------
# 8. APPLICATION ENTRY POINT
# ------------------------------------------------------------------------------
def main():
    # Windows high DPI attributes
    if hasattr(Qt.ApplicationAttribute, "AA_EnableHighDpiScaling"):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(APP_ORG)
    app.setStyleSheet(GLOBAL_QSS)

    window = VoltSynxMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
