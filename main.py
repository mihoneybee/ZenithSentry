from src.logic import calcular_status_saude, obter_cor_ansi, obter_reset_ansi

st.set_page_config(page_title="ZenithSentry",page_icon="🛡️")

def executar():
    print("--- 🛡️ ZenithSentry: Monitor de Saúde Mental ---")
    while True:
        try:
            horas = float(input("Digite o total de horas trabalhadas hoje: "))
            status, mensagem = calcular_status_saude(horas)
            
            # Obter código de cor ANSI para o nível
            cor = obter_cor_ansi(status)
            reset = obter_reset_ansi()
            
            print(f"\n{cor}[{status}]{reset}")
            print(f"{cor}{mensagem}{reset}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
    

if __name__ == "__main__":
    executar()
