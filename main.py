from src.logic import calcular_status_saude
from src.api_service import buscar_frase_motivacional

def executar():
    print("--- 🛡️ ZenithSentry v1.1.0 ---")
    try:
        horas = float(input("Horas trabalhadas hoje: "))
        status, mensagem = calcular_status_saude(horas)
        
        print(f"\n[{status}] {mensagem}")
        
        # Novo: Integração com API
        print("\n💡 Pensamento do dia para o seu equilíbrio:")
        print(buscar_frase_motivacional())
        
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    executar()
