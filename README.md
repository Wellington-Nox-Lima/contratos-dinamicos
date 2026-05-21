# Gerador de Contratos

Aplicacao Streamlit para geracao de contratos comerciais em `.docx` com regras condicionais de plano, pagamento, desconto, implantacao e migracao.

## Executar localmente

```powershell
python -m streamlit run app_streamlit.py
```

## Deploy online

Este projeto deve ser publicado no Streamlit Community Cloud, pois GitHub Pages nao executa aplicacoes Python/Streamlit.

Configuracao sugerida no Streamlit Cloud:

- Repository: `strongholder11/contratos-dinamicos`
- Branch: `main`
- Main file path: `app_streamlit.py`

Dependencias necessarias estao em `requirements.txt`, na raiz do repositorio.
Nao cadastre `Projeto contrato dinamico/requirements.txt` como pacote no deploy. Se for instalar manualmente, o comando correto e:

```powershell
pip install -r requirements.txt
```

## Regras comerciais

- Planos SMART e Clinic por faixa de equipos.
- Formatos de pagamento: Recorrente, Plano Integral no Cartao, PIX e Mensal.
- Desconto digitavel em percentual.
- Migracao: Isento, Padrao ou Inteligente.
- Valores comerciais centralizados em `Projeto contrato dinamico/gerador_contratos.py`.
