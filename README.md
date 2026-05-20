# Gerador de Contratos

Aplicação Streamlit para geração de contratos comerciais em `.docx` com regras condicionais de plano, pagamento, desconto, implantação e migração.

## Executar localmente

```powershell
cd "Projeto contrato dinamico"
python -m streamlit run app_streamlit.py
```

## Deploy online

Este projeto deve ser publicado no Streamlit Community Cloud, pois GitHub Pages não executa aplicações Python/Streamlit.

Configuração sugerida no Streamlit Cloud:

- Repository: `strongholder11/contratos-dinamicos`
- Branch: `main`
- Main file path: `Projeto contrato dinamico/app_streamlit.py`

Dependências necessárias estão em `requirements.txt`.

## Regras comerciais

- Planos SMART e Clinic por faixa de equipos.
- Formatos de pagamento: Recorrente, Plano Integral no Cartão, PIX e Mensal.
- Desconto digitável em percentual.
- Migração: Isento, Padrão ou Inteligente.
- Valores comerciais centralizados em `Projeto contrato dinamico/gerador_contratos.py`.
