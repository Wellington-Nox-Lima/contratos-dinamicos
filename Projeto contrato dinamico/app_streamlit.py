from pathlib import Path

import streamlit as st

from gerador_contratos import Gerador


st.set_page_config(
    page_title="Gerador de Contratos",
    page_icon=":page_facing_up:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def aplicar_tema(modo_escuro: bool) -> None:
    if modo_escuro:
        cores = {
            "bg": "#090d16",
            "surface": "rgba(17, 24, 39, 0.86)",
            "surface_2": "rgba(30, 41, 59, 0.82)",
            "text": "#f8fafc",
            "muted": "#a8b3c7",
            "line": "rgba(148, 163, 184, 0.22)",
            "accent": "#22c55e",
            "accent_2": "#38bdf8",
            "button_text": "#03120a",
            "shadow": "rgba(0, 0, 0, 0.36)",
            "input": "rgba(15, 23, 42, 0.92)",
        }
    else:
        cores = {
            "bg": "#f6f8fb",
            "surface": "rgba(255, 255, 255, 0.92)",
            "surface_2": "rgba(239, 246, 255, 0.86)",
            "text": "#111827",
            "muted": "#526173",
            "line": "rgba(15, 23, 42, 0.12)",
            "accent": "#0f9f6e",
            "accent_2": "#2563eb",
            "button_text": "#ffffff",
            "shadow": "rgba(15, 23, 42, 0.12)",
            "input": "#ffffff",
        }

    st.markdown(
        f"""
        <style>
            :root {{
                --app-bg: {cores["bg"]};
                --app-surface: {cores["surface"]};
                --app-surface-2: {cores["surface_2"]};
                --app-text: {cores["text"]};
                --app-muted: {cores["muted"]};
                --app-line: {cores["line"]};
                --app-accent: {cores["accent"]};
                --app-accent-2: {cores["accent_2"]};
                --app-button-text: {cores["button_text"]};
                --app-shadow: {cores["shadow"]};
                --app-input: {cores["input"]};
            }}

            .stApp {{
                color: var(--app-text);
                background:
                    radial-gradient(circle at 10% 12%, rgba(34, 197, 94, 0.16), transparent 28%),
                    radial-gradient(circle at 88% 8%, rgba(37, 99, 235, 0.16), transparent 30%),
                    linear-gradient(135deg, var(--app-bg), var(--app-bg));
            }}

            .block-container {{
                max-width: 1180px;
                padding-top: 2.2rem;
                padding-bottom: 2rem;
            }}

            [data-testid="stSidebar"] {{
                background: var(--app-surface);
                border-right: 1px solid var(--app-line);
            }}

            [data-testid="stSidebar"] * {{
                color: var(--app-text);
            }}

            h1, h2, h3, p, label, span, div {{
                color: var(--app-text);
            }}

            .hero {{
                position: relative;
                overflow: hidden;
                padding: 34px;
                border: 1px solid var(--app-line);
                border-radius: 8px;
                background:
                    linear-gradient(135deg, rgba(34, 197, 94, 0.18), rgba(56, 189, 248, 0.16)),
                    var(--app-surface);
                box-shadow: 0 24px 70px var(--app-shadow);
            }}

            .hero-kicker {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                margin-bottom: 14px;
                padding: 7px 11px;
                border: 1px solid var(--app-line);
                border-radius: 999px;
                color: var(--app-muted);
                font-size: 0.84rem;
                font-weight: 700;
                text-transform: uppercase;
            }}

            .hero-title {{
                margin: 0;
                color: var(--app-text);
                font-size: clamp(2.3rem, 5vw, 4.6rem);
                line-height: 0.95;
                font-weight: 900;
                letter-spacing: 0;
            }}

            .hero-copy {{
                max-width: 760px;
                margin-top: 18px;
                color: var(--app-muted);
                font-size: 1.08rem;
                line-height: 1.7;
            }}

            .metric-row {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 14px;
                margin-top: 24px;
            }}

            .metric-card {{
                min-height: 94px;
                padding: 17px;
                border: 1px solid var(--app-line);
                border-radius: 8px;
                background: var(--app-surface-2);
            }}

            .metric-label {{
                color: var(--app-muted);
                font-size: 0.82rem;
                font-weight: 700;
                text-transform: uppercase;
            }}

            .metric-value {{
                margin-top: 8px;
                color: var(--app-text);
                font-size: 1.55rem;
                font-weight: 850;
            }}

            .panel {{
                padding: 24px;
                border: 1px solid var(--app-line);
                border-radius: 8px;
                background: var(--app-surface);
                box-shadow: 0 18px 55px var(--app-shadow);
            }}

            .panel-title {{
                margin: 0 0 5px;
                font-size: 1.35rem;
                font-weight: 850;
            }}

            .panel-copy {{
                margin: 0 0 18px;
                color: var(--app-muted);
            }}

            .stTextInput input,
            .stSelectbox div[data-baseweb="select"] > div {{
                min-height: 48px;
                color: var(--app-text);
                background: var(--app-input);
                border-color: var(--app-line);
                border-radius: 8px;
            }}

            .stTextInput input:focus {{
                border-color: var(--app-accent);
                box-shadow: 0 0 0 1px var(--app-accent);
            }}

            .stTabs [data-baseweb="tab-list"] {{
                gap: 10px;
                padding: 7px;
                border: 1px solid var(--app-line);
                border-radius: 8px;
                background: var(--app-surface);
            }}

            .stTabs [data-baseweb="tab"] {{
                height: 46px;
                padding: 0 20px;
                border-radius: 8px;
                color: var(--app-muted);
                font-weight: 750;
            }}

            .stTabs [aria-selected="true"] {{
                color: var(--app-button-text);
                background: linear-gradient(135deg, var(--app-accent), var(--app-accent-2));
            }}

            .stButton > button,
            .stDownloadButton > button {{
                width: 100%;
                min-height: 52px;
                border: 0;
                border-radius: 8px;
                color: var(--app-button-text);
                background: linear-gradient(135deg, var(--app-accent), var(--app-accent-2));
                box-shadow: 0 14px 32px rgba(37, 99, 235, 0.22);
                font-weight: 850;
                transition: transform 160ms ease, box-shadow 160ms ease, filter 160ms ease;
            }}

            .stButton > button:hover,
            .stDownloadButton > button:hover {{
                color: var(--app-button-text);
                transform: translateY(-1px);
                filter: brightness(1.04);
                box-shadow: 0 18px 44px rgba(37, 99, 235, 0.32);
            }}

            [data-testid="stAlert"] {{
                border-radius: 8px;
                border: 1px solid var(--app-line);
            }}

            .footer {{
                margin-top: 26px;
                padding: 16px 0;
                color: var(--app-muted);
                text-align: center;
                font-size: 0.9rem;
            }}

            @media (max-width: 760px) {{
                .block-container {{
                    padding-top: 1rem;
                }}

                .hero {{
                    padding: 23px;
                }}

                .metric-row {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def encontrar_chave_licenca(gerador: Gerador, nome_licenca: str) -> str:
    return next(chave for chave, valor in gerador.TIPOS_LICENCA.items() if valor == nome_licenca)


def mostrar_download(caminho: Path) -> None:
    st.success("Contrato gerado com sucesso.")
    st.info(f"Arquivo criado: `{caminho.name}`")
    with open(caminho, "rb") as arquivo:
        st.download_button(
            label="Baixar contrato",
            data=arquivo.read(),
            file_name=caminho.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )


def gerar_pf(gerador: Gerador, nome: str, cpf: str, tipo_licenca: str) -> None:
    if not nome.strip():
        st.error("Preencha o nome completo.")
        return
    if not cpf.strip():
        st.error("Preencha o CPF.")
        return

    try:
        with st.spinner("Preparando documento..."):
            chave = encontrar_chave_licenca(gerador, tipo_licenca)
            caminho = gerador.gerar_contrato_pf(nome.strip(), cpf.strip(), chave)
        mostrar_download(caminho)
    except ValueError as erro:
        st.error(f"Erro de validacao: {erro}")
    except FileNotFoundError as erro:
        st.error(f"Template nao encontrado: {erro}")
        st.warning("Verifique se os arquivos de modelo estao dentro da pasta `templates/`.")
    except Exception as erro:
        st.error(f"Erro ao gerar contrato: {erro}")


def gerar_pj(gerador: Gerador, razao_social: str, cnpj: str, tipo_licenca: str) -> None:
    if not razao_social.strip():
        st.error("Preencha a razao social.")
        return
    if not cnpj.strip():
        st.error("Preencha o CNPJ.")
        return

    try:
        with st.spinner("Montando contrato empresarial..."):
            chave = encontrar_chave_licenca(gerador, tipo_licenca)
            caminho = gerador.gerar_contrato_pj(razao_social.strip(), cnpj.strip(), chave)
        mostrar_download(caminho)
    except ValueError as erro:
        st.error(f"Erro de validacao: {erro}")
    except FileNotFoundError as erro:
        st.error(f"Template nao encontrado: {erro}")
        st.warning("Verifique se os arquivos de modelo estao dentro da pasta `templates/`.")
    except Exception as erro:
        st.error(f"Erro ao gerar contrato: {erro}")


gerador = Gerador()

with st.sidebar:
    st.markdown("### Aparencia")
    modo_escuro = st.toggle("Modo escuro", value=True)
    st.markdown("---")
    st.markdown("### Status")
    st.caption("Contratos gerados ficam em `contratos_gerados/`.")
    st.caption("Modelos devem ficar em `templates/`.")

aplicar_tema(modo_escuro)

total_templates = len(list(Path("templates").glob("*.docx")))
total_gerados = len(list(Path("contratos_gerados").glob("*.docx")))

st.markdown(
    f"""
    <section class="hero">
        <div class="hero-kicker">Automacao de documentos</div>
        <h1 class="hero-title">Gerador de Contratos</h1>
        <p class="hero-copy">
            Crie contratos com visual profissional em poucos segundos, usando dados validados,
            modelos padronizados e download imediato do arquivo em Word.
        </p>
        <div class="metric-row">
            <div class="metric-card">
                <div class="metric-label">Modelos disponiveis</div>
                <div class="metric-value">{total_templates}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Contratos gerados</div>
                <div class="metric-value">{total_gerados}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Tipos de licenca</div>
                <div class="metric-value">{len(gerador.TIPOS_LICENCA)}</div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

col_form, col_preview = st.columns([1.35, 0.85], gap="large")

with col_form:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<h2 class="panel-title">Novo contrato</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="panel-copy">Escolha o perfil, informe os dados e gere o documento final.</p>',
        unsafe_allow_html=True,
    )

    tab_pf, tab_pj = st.tabs(["Pessoa Fisica", "Pessoa Juridica"])

    with tab_pf:
        nome = st.text_input("Nome completo", placeholder="Joao da Silva", key="pf_nome")
        cpf = st.text_input("CPF", placeholder="123.456.789-01 ou 12345678901", key="pf_cpf")
        tipo_licenca_pf = st.selectbox(
            "Tipo de licenca",
            options=list(gerador.TIPOS_LICENCA.values()),
            key="pf_licenca",
        )
        if st.button("Gerar contrato PF", key="btn_pf"):
            gerar_pf(gerador, nome, cpf, tipo_licenca_pf)

    with tab_pj:
        razao_social = st.text_input(
            "Razao social",
            placeholder="Empresa LTDA",
            key="pj_razao",
        )
        cnpj = st.text_input(
            "CNPJ",
            placeholder="12.345.678/0001-90 ou 12345678000190",
            key="pj_cnpj",
        )
        tipo_licenca_pj = st.selectbox(
            "Tipo de licenca",
            options=list(gerador.TIPOS_LICENCA.values()),
            key="pj_licenca",
        )
        if st.button("Gerar contrato PJ", key="btn_pj"):
            gerar_pj(gerador, razao_social, cnpj, tipo_licenca_pj)

    st.markdown("</div>", unsafe_allow_html=True)

with col_preview:
    st.markdown(
        """
        <div class="panel">
            <h2 class="panel-title">Fluxo do documento</h2>
            <p class="panel-copy">Entrada validada, modelo aplicado e arquivo final pronto para baixar.</p>
            <div class="metric-card">
                <div class="metric-label">1. Dados</div>
                <div class="metric-value">Cliente</div>
            </div>
            <br>
            <div class="metric-card">
                <div class="metric-label">2. Modelo</div>
                <div class="metric-value">Template</div>
            </div>
            <br>
            <div class="metric-card">
                <div class="metric-label">3. Saida</div>
                <div class="metric-value">DOCX</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer">Contratos gerados sao salvos automaticamente em <code>contratos_gerados/</code>.</div>',
    unsafe_allow_html=True,
)
