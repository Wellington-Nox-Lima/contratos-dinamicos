import streamlit as st
from pathlib import Path
from gerador_contratos import Gerador, ValidadorDados
import os

# Configuração da página
st.set_page_config(
    page_title="Gerador de Contratos",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS customizado (opcional, para melhorar visual)
st.markdown("""
    <style>
    .main {
        max-width: 700px;
        margin: 0 auto;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título e descrição
st.title("📄 Gerador de Contratos")
st.markdown("---")
st.write("Preencha os dados do cliente abaixo e gere o contrato automaticamente.")

# Inicializa o gerador
gerador = Gerador()

# Abas para tipo de cliente
tab1, tab2 = st.tabs(["Pessoa Física", "Pessoa Jurídica"]) 

with tab1:
    st.subheader("Dados da Pessoa Física")
    
    nome = st.text_input(
        "Nome Completo",
        placeholder="João da Silva",
        key="pf_nome"
    )
    
    cpf = st.text_input(
        "CPF",
        placeholder="123.456.789-01 ou 12345678901",
        key="pf_cpf"
    )
    
    tipo_licenca_pf = st.selectbox(
        "Tipo de Licença",
        options=list(gerador.TIPOS_LICENCA.values()),
        key="pf_licenca"
    )
    
    if st.button("🔄 Gerar Contrato - PF", key="btn_pf"):
        # Validações
        if not nome.strip():
            st.error("❌ Por favor, preencha o nome completo.")
        elif not cpf.strip():
            st.error("❌ Por favor, preencha o CPF.")
        else:
            try:
                with st.spinner("⏳ Gerando contrato..."):
                    # Encontra a chave do tipo de licença
                    tipo_licenca_key = [k for k, v in gerador.TIPOS_LICENCA.items() 
                                       if v == tipo_licenca_pf][0]
                    
                    # Gera o contrato
                    caminho = gerador.gerar_contrato_pf(nome, cpf, tipo_licenca_key)
                
                st.success(f"✅ Contrato gerado com sucesso!")
                st.info(f"📁 Arquivo: `{caminho.name}`")
                
                # Botão de download
                with open(caminho, "rb") as arquivo:
                    st.download_button(
                        label="📥 Baixar Contrato",
                        data=arquivo.read(),
                        file_name=caminho.name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            
            except ValueError as e:
                st.error(f"❌ Erro de validação: {e}")
            except FileNotFoundError as e:
                st.error(f"❌ Template não encontrado: {e}")
                st.warning("Verifique se os templates estão na pasta `/templates/`")
            except Exception as e:
                st.error(f"❌ Erro ao gerar contrato: {e}")

with tab2:
    st.subheader("Dados da Pessoa Jurídica")
    
    razao_social = st.text_input(
        "Razão Social",
        placeholder="Empresa LTDA",
        key="pj_razao"
    )
    
    cnpj = st.text_input(
        "CNPJ",
        placeholder="12.345.678/0001-90 ou 12345678000190",
        key="pj_cnpj"
    )
    
    tipo_licenca_pj = st.selectbox(
        "Tipo de Licença",
        options=list(gerador.TIPOS_LICENCA.values()),
        key="pj_licenca"
    )
    
    if st.button("🔄 Gerar Contrato - PJ", key="btn_pj"):
        # Validações
        if not razao_social.strip():
            st.error("❌ Por favor, preencha a razão social.")
        elif not cnpj.strip():
            st.error("❌ Por favor, preencha o CNPJ.")
        else:
            try:
                with st.spinner("⏳ Gerando contrato..."):
                    # Encontra a chave do tipo de licença
                    tipo_licenca_key = [k for k, v in gerador.TIPOS_LICENCA.items() 
                                       if v == tipo_licenca_pj][0]
                    
                    # Gera o contrato
                    caminho = gerador.gerar_contrato_pj(razao_social, cnpj, tipo_licenca_key)
                
                st.success(f"✅ Contrato gerado com sucesso!")
                st.info(f"📁 Arquivo: `{caminho.name}`")
                
                # Botão de download
                with open(caminho, "rb") as arquivo:
                    st.download_button(
                        label="📥 Baixar Contrato",
                        data=arquivo.read(),
                        file_name=caminho.name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            
            except ValueError as e:
                st.error(f"❌ Erro de validação: {e}")
            except FileNotFoundError as e:
                st.error(f"❌ Template não encontrado: {e}")
                st.warning("Verifique se os templates estão na pasta `/templates/`")
            except Exception as e:
                st.error(f"❌ Erro ao gerar contrato: {e}")

# Rodapé
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
    📂 Contratos gerados são salvos em <code>contratos_gerados/</code>
    </div>
    """, unsafe_allow_html=True)