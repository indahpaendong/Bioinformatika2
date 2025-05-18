import streamlit as st

st.title("Translasi DNA ke Protein")

# Tambahkan CSS ke dalam HTML menggunakan markdown
st.markdown("""
    <style>
    .main {
        background-color: #f7fafd;
        padding: 20px;
        border-radius: 15px;
    }
    h1 {
        color: #3a7bd5;
        text-align: center;
        font-size: 36px;
    }
    .stTextArea textarea {
        font-family: 'Courier New', monospace;
        font-size: 16px;
        background-color: #f0f5ff;
        border-radius: 8px;
    }
    .stTextInput input {
        background-color: #f0f5ff;
        border-radius: 8px;
    }
    .css-1d391kg {
        font-weight: bold;
        font-size: 20px;
        color: #1a1a1a;
    }
    </style>
""", unsafe_allow_html=True)

# Lanjutkan dengan input DNA
dna_seq = st.text_area("Masukkan urutan DNA (harus kelipatan 3):", height=150)

# Kamus kodon DNA → Asam amino
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

dna_seq = st.text_area("Masukkan urutan DNA (harus kelipatan 3):", height=150)

if dna_seq:
    dna_seq = dna_seq.upper().replace(" ", "").replace("\n", "")
    protein = ""
    
    if len(dna_seq) % 3 != 0:
        st.error("Panjang DNA harus kelipatan 3.")
    else:
        for i in range(0, len(dna_seq), 3):
            codon = dna_seq[i:i+3]
            amino_acid = codon_table.get(codon, "?")
            protein += amino_acid
        st.success("Hasil translasi:")
        st.code(protein)
