import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# RDKit
from rdkit import Chem
from rdkit.Chem import (
    Draw,
    AllChem,
    Descriptors,
    Crippen,
    Lipinski,
    rdMolDescriptors
)

# 3D Visualization
import py3Dmol
import streamlit.components.v1 as components

# PDF
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image,
    Preformatted
)
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
import tempfile
import os


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cheminformatics Virtual Laboratory",
    page_icon="🧪",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
/* =========================================================
   CHEMINFORMATICS VIRTUAL LABORATORY - VISUAL THEME
   Navy + blue + teal, with readable typography
   ========================================================= */
:root {
    --cv-primary: #17365D;
    --cv-blue: #2463A6;
    --cv-teal: #008C95;
    --cv-light: #EDF5FF;
    --cv-text: #243447;
    --cv-border: #D5E3F2;
}

/* Main page */
.stApp {
    color: var(--cv-text);
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #F8FBFF 0%, #FFFFFF 35%, #F4F9FF 100%);
}
[data-testid="stHeader"] {
    background: rgba(248, 251, 255, 0.92);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #17365D 0%, #214D78 100%);
}
[data-testid="stSidebar"] * {
    color: #FFFFFF;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    font-size: 17px;
}

/* Typography */
.main-title {
