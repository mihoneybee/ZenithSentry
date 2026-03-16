from src.logic import calcular_status_saude

def executar():
    print("--- 🛡️ ZenithSentry: Monitor de Saúde Mental ---")
    while True:
        try:
            horas = float(input("Digite o total de horas trabalhadas hoje: "))
            status, mensagem = calcular_status_saude(horas)
            
            print(f"\n[{status}]")
            print(mensagem)
            break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
    

if __name__ == "__main__":
    executar()
